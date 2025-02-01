import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog, ttk
from PIL import Image, ImageTk
import numpy as np
import json
import os

# Load translations from JSON file
with open('translations.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

def interpret_as_bitmap(file_path, width):
    with open(file_path, 'rb') as file:
        data = file.read()

    data = data.rstrip(b'\x00')

    bits = ''.join(f"{byte:08b}" for byte in data)
    pixels = np.array([int(b) for b in bits], dtype=np.uint8)

    height = len(pixels) // width
    if len(pixels) % width != 0:
        pixels = pixels[:height * width]

    image_array = pixels.reshape((height, width))
    image = Image.fromarray(image_array * 255, mode='L')

    return image

def open_file():
    global file_path, image, tk_image, zoom_level
    file_path = filedialog.askopenfilename(title=translations["open_file"][language.get()], filetypes=[("All Files", "*.*")])
    if file_path:
        file_label.configure(text=f"{translations['selected_file'][language.get()]} {file_path.split('/')[-1]}")
        try:
            # Проверка расширения
            if not file_path.lower().endswith('.bin'):
                messagebox.showerror(translations["error"][language.get()], translations["select_bin_file"][language.get()])
                return

            width = int(width_entry.get())
            image = interpret_as_bitmap(file_path, width)
            zoom_level = 1.0
            display_image()
        except Exception as e:
            messagebox.showerror(translations["error"][language.get()], f"{translations['file_processing_error'][language.get()]}: {e}")
    else:
        file_label.configure(text=translations["no_file_selected"][language.get()])

def reload_image():
    global image, tk_image
    if file_path:
        try:
            width = int(width_entry.get())
            image = interpret_as_bitmap(file_path, width)
            display_image()
        except Exception as e:
            messagebox.showerror(translations["error"][language.get()], f"{translations['image_reload_error'][language.get()]}: {e}")

def display_image():
    global tk_image
    if image:
        zoomed_image = image.resize((int(image.width * zoom_level), int(image.height * zoom_level)), Image.NEAREST)
        tk_image = ImageTk.PhotoImage(zoomed_image)
        canvas.configure(scrollregion=(0, 0, zoomed_image.width, zoomed_image.height))
        canvas.create_image(0, 0, anchor=ctk.NW, image=tk_image)

        # Clear existing grid lines
        canvas.delete("grid_line")

        # Draw grid lines
        width = int(width_entry.get())
        grid_color = grid_color_entry.get().split(',')
        if len(grid_color) == 3:
            try:
                r, g, b = map(int, grid_color)
                grid_color = f'#{r:02x}{g:02x}{b:02x}'
            except ValueError:
                grid_color = "red"
        else:
            grid_color = "red"

        for x in range(0, image.width, width):
            canvas.create_line(x * zoom_level, 0, x * zoom_level, zoomed_image.height, fill=grid_color, tags="grid_line")
        for y in range(0, image.height, width):
            canvas.create_line(0, y * zoom_level, zoomed_image.width, y * zoom_level, fill=grid_color, tags="grid_line")

def redraw_grid():
    display_image()

def start_drawing(event):
    global drawing, new_color
    drawing = True
    if event.num == 1:  # Left mouse button
        new_color = 255  # White
    elif event.num == 3:  # Right mouse button
        new_color = 0  # Black
    draw(event)

def stop_drawing(event):
    global drawing
    drawing = False

def draw(event):
    global image, new_color
    if drawing:
        x = int(canvas.canvasx(event.x) / zoom_level)
        y = int(canvas.canvasy(event.y) / zoom_level)
        if 0 <= x < image.width and 0 <= y < image.height:
            image.putpixel((x, y), new_color)
            display_image()

def save_image():
    save_path = filedialog.asksaveasfilename(defaultextension=".tiff",
                                             filetypes=[("TIFF files", "*.tiff"), ("All files", "*.*")])
    if save_path:
        image.save(save_path)
        messagebox.showinfo(translations["success"][language.get()], f"{translations['image_saved'][language.get()]} {save_path}")

def save_to_bin():
    save_path = filedialog.asksaveasfilename(defaultextension=".bin",
                                             filetypes=[("BIN files", "*.bin"), ("All files", "*.*")])
    if save_path:
        width, height = image.size
        pixels = np.array(image.convert('L')).flatten()
        bits = ''.join(str(int(p > 127)) for p in pixels)
        byte_array = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
        with open(save_path, 'wb') as file:
            file.write(byte_array)
        messagebox.showinfo(translations["success"][language.get()], f"{translations['data_saved'][language.get()]} {save_path}")

def open_table_window():
    if not image:
        messagebox.showerror(translations["error"][language.get()], translations["open_image_first"][language.get()])
        return

    table_window = ctk.CTkToplevel(root)
    table_window.title(translations["pixel_table"][language.get()])

    table_frame = ctk.CTkFrame(table_window)
    table_frame.pack(fill=ctk.BOTH, expand=True)

    columns = simpledialog.askinteger(translations["table_settings"][language.get()], translations["enter_columns"][language.get()], initialvalue=16)
    if not columns:
        columns = 16

    tree = ttk.Treeview(table_frame, columns=[f"col{i}" for i in range(columns)], show="headings")
    for i in range(columns):
        tree.heading(f"col{i}", text=f"{translations['column'][language.get()]} {i+1}")
        tree.column(f"col{i}", width=50, anchor='center')

    scrollbar_y = ttk.Scrollbar(table_frame, orient=ctk.VERTICAL, command=tree.yview)
    scrollbar_x = ttk.Scrollbar(table_frame, orient=ctk.HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_y.pack(side=ctk.RIGHT, fill=ctk.Y)
    scrollbar_x.pack(side=ctk.BOTTOM, fill=ctk.X)
    tree.pack(fill=ctk.BOTH, expand=True)

    pixels = np.array(image.convert('L'))
    rows = pixels.shape[0]
    cols = pixels.shape[1]

    for row in range(rows):
        values = []
        for col in range(columns):
            if col < cols:
                values.append(pixels[row, col])
            else:
                values.append('')
        tree.insert('', ctk.END, values=values)

def export_image():
    if not image:
        messagebox.showerror(translations["error"][language.get()], translations["open_image_first"][language.get()])
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".tiff",
                                             filetypes=[("TIFF files", "*.tiff"), ("All files", "*.*")])
    if save_path:
        image.save(save_path)
        messagebox.showinfo(translations["success"][language.get()], f"{translations['image_exported'][language.get()]} {save_path}")

def import_image():
    global image, tk_image
    file_path = filedialog.askopenfilename(title=translations["select_tiff_file"][language.get()], filetypes=[("TIFF files", "*.tiff"), ("All files", "*.*")])
    if file_path:
        try:
            imported_image = Image.open(file_path).convert('L')
            width = int(width_entry.get())
            expected_width = width
            expected_height = imported_image.height // (imported_image.width // width)

            print(f"Expected dimensions: {expected_width}x{expected_height}")
            print(f"Imported image dimensions: {imported_image.size}")

            if imported_image.size != (expected_width, expected_height):
                messagebox.showerror(translations["error"][language.get()], f"{translations['image_size_mismatch'][language.get()]} {expected_width}x{expected_height}.")
                return

            image = imported_image
            display_image()
        except Exception as e:
            messagebox.showerror(translations["error"][language.get()], f"{translations['image_import_error'][language.get()]}: {e}")

def zoom(event):
    global zoom_level
    if event.delta > 0:
        zoom_level *= 1.1
    else:
        zoom_level /= 1.1
    display_image()

def update_zoom_level(value):
    global zoom_level
    zoom_level = float(value) / 100
    display_image()

# Function to bind Ctrl + R for reloading the image
def bind_hot_reload(event):
    reload_image()

def update_language(*args):
    language_code = language.get()
    root.title(translations["title"][language_code])
    notebook.tab(editor_tab, text=translations["editor_tab"][language_code])
    notebook.tab(settings_tab, text=translations["settings_tab"][language_code])
    file_label.configure(text=translations["no_file_selected"][language_code])
    open_button.configure(text=translations["open_file_button"][language_code])
    width_label.configure(text=translations["width_label"][language_code])
    table_button.configure(text=translations["open_table_button"][language_code])
    save_button.configure(text=translations["save_image_button"][language_code])
    save_bin_button.configure(text=translations["save_bin_button"][language.get()])
    reload_button.configure(text=translations["reload_image_button"][language_code])
    redraw_grid_button.configure(text=translations["redraw_grid_button"][language_code])
    export_button.configure(text=translations["export_image_button"][language_code])
    import_button.configure(text=translations["import_image_button"][language.get()])
    language_label.configure(text=translations["language_label"][language_code])
    grid_color_label.configure(text=translations["grid_color_label"][language_code])
    show_kanji_button.configure(text=translations["show_kanji_button"][language_code])

def fromhex(a):
    hex_from_str = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
                    '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000',
                    '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101',
                    'E':'1110', 'F':'1111',}
    b = ''
    for char in a:
        b += hex_from_str[char]
    return int(b, 2)

def show(kanji, file_path):
    RESIZE = 5
    name = kanji
    if kanji > 0x8000:
        kanji -= 0x8000
    else:
        messagebox.showerror(translations["error"][language.get()], translations["enter_hex_code"][language.get()])
        return
    with open(file_path, 'rb') as f:
        f = f.read()
        offset = kanji * 32
        tile = f[offset:offset + 32]
    picture = Image.new('1', (16, 16))
    x = 0
    y = 0
    for i in range(0, 32, 2):
        bitmap = int.from_bytes(tile[i:i + 2])
        bitmap = bin(bitmap)[2:].zfill(16)
        for number in bitmap:
            if number == '1':
                picture.putpixel((x, y), 1)
                x += 1
            else:
                x += 1
        y += 1
        x = 0
    picture = picture.resize((16 * RESIZE, 16 * RESIZE))
    picture.show(title=name)

def open_kanji_window():
    if not file_path:
        messagebox.showerror(translations["error"][language.get()], translations["open_file_first"][language.get()])
        return

    kanji_window = ctk.CTkToplevel(root)
    kanji_window.title(translations["show_kanji_button"][language.get()])

    kanji_label = ctk.CTkLabel(kanji_window, text=translations["enter_hex_code"][language.get()])
    kanji_label.pack(pady=5)

    kanji_entry = ctk.CTkEntry(kanji_window)
    kanji_entry.pack(pady=5)

    def show_kanji():
        kanji_hex = kanji_entry.get()
        try:
            kanji = fromhex(kanji_hex)
            show(kanji, file_path)
        except Exception as e:
            messagebox.showerror(translations["error"][language.get()], f"{translations['file_processing_error'][language.get()]}: {e}")

    show_button = ctk.CTkButton(kanji_window, text=translations["show_kanji_button"][language.get()], command=show_kanji)
    show_button.pack(pady=5)

root = ctk.CTk()
root.title(translations["title"]["en"])

file_path = ""
image = None
tk_image = None
zoom_level = 1.0
drawing = False
new_color = None

# Language selection
language = ctk.StringVar(value="en")
language_options = ["en", "ru", "eo", "ja", "uk"]

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Editor Tab
editor_tab = ttk.Frame(notebook)
notebook.add(editor_tab, text=translations["editor_tab"]["en"])

file_label = ctk.CTkLabel(editor_tab, text=translations["no_file_selected"]["en"])
file_label.pack(pady=5)

open_button = ctk.CTkButton(editor_tab, text=translations["open_file_button"]["en"], command=open_file)
open_button.pack(pady=5)

width_label = ctk.CTkLabel(editor_tab, text=translations["width_label"]["en"])
width_label.pack(pady=5)

width_entry = ctk.CTkEntry(editor_tab)
width_entry.insert(0, "128")
width_entry.pack(pady=5)

table_button = ctk.CTkButton(editor_tab, text=translations["open_table_button"]["en"], command=open_table_window)
table_button.pack(pady=5)

save_button = ctk.CTkButton(editor_tab, text=translations["save_image_button"]["en"], command=save_image)
save_button.pack(pady=5)

save_bin_button = ctk.CTkButton(editor_tab, text=translations["save_bin_button"]["en"], command=save_to_bin)
save_bin_button.pack(pady=5)

reload_button = ctk.CTkButton(editor_tab, text=translations["reload_image_button"]["en"], command=reload_image)
reload_button.pack(pady=5)

redraw_grid_button = ctk.CTkButton(editor_tab, text=translations["redraw_grid_button"]["en"], command=redraw_grid)
redraw_grid_button.pack(pady=5)

export_button = ctk.CTkButton(editor_tab, text=translations["export_image_button"]["en"], command=export_image)
export_button.pack(pady=5)

import_button = ctk.CTkButton(editor_tab, text=translations["import_image_button"]["en"], command=import_image)
import_button.pack(pady=5)

show_kanji_button = ctk.CTkButton(editor_tab, text=translations["show_kanji_button"]["en"], command=open_kanji_window)
show_kanji_button.pack(pady=5)

canvas_frame = ctk.CTkFrame(editor_tab)
canvas_frame.pack(fill=ctk.BOTH, expand=True)

canvas = ctk.CTkCanvas(canvas_frame, bg="white")
canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

scrollbar_y = ctk.CTkScrollbar(canvas_frame, orientation="vertical", command=canvas.yview)
scrollbar_y.pack(side=ctk.RIGHT, fill=ctk.Y)
canvas.configure(yscrollcommand=scrollbar_y.set)

scrollbar_x = ctk.CTkScrollbar(editor_tab, orientation="horizontal", command=canvas.xview)
scrollbar_x.pack(side=ctk.BOTTOM, fill=ctk.X)
canvas.configure(xscrollcommand=scrollbar_x.set)

zoom_scale = ctk.CTkSlider(editor_tab, from_=100, to=500, orientation="horizontal", command=update_zoom_level)
zoom_scale.set(100)
zoom_scale.pack(side=ctk.BOTTOM, fill=ctk.X)

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)
canvas.bind("<Button-3>", start_drawing)
canvas.bind("<B3-Motion>", draw)
canvas.bind("<ButtonRelease-3>", stop_drawing)
root.bind('<Control-r>', bind_hot_reload)

# Settings Tab
settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text=translations["settings_tab"]["en"])

language_label = ctk.CTkLabel(settings_tab, text=translations["language_label"]["en"])
language_label.pack(pady=5)

language_menu = ctk.CTkOptionMenu(settings_tab, variable=language, values=language_options, command=update_language)
language_menu.pack(pady=5)

grid_color_label = ctk.CTkLabel(settings_tab, text=translations["grid_color_label"]["en"])
grid_color_label.pack(pady=5)

grid_color_entry = ctk.CTkEntry(settings_tab)
grid_color_entry.insert(0, "255,0,0")
grid_color_entry.pack(pady=5)

# Update language initially
update_language()

# Запуск основного цикла приложения
root.mainloop()
