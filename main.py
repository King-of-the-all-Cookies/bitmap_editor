import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from PIL import Image, ImageTk
import numpy as np

# Translations dictionary
translations = {
    "title": {
        "en": "Bitmap Editor",
        "ru": "Редактор битмап изображений",
        "eo": "Bitmapa Redaktilo",
        "ja": "ビットマップエディタ",
        "uk": "Редактор бітмап зображень"
    },
    "editor_tab": {
        "en": "Editor",
        "ru": "Редактор",
        "eo": "Redaktilo",
        "ja": "エディタ",
        "uk": "Редактор"
    },
    "settings_tab": {
        "en": "Settings",
        "ru": "Настройки",
        "eo": "Agordoj",
        "ja": "設定",
        "uk": "Налаштування"
    },
    "open_file": {
        "en": "Open File",
        "ru": "Выберите файл",
        "eo": "Malfermi Dosieron",
        "ja": "ファイルを開く",
        "uk": "Відкрийте файл"
    },
    "selected_file": {
        "en": "Selected file:",
        "ru": "Выбранный файл:",
        "eo": "Elektita dosiero:",
        "ja": "選択されたファイル:",
        "uk": "Вибраний файл:"
    },
    "select_bin_file": {
        "en": "Select a file with the .bin or .BIN extension",
        "ru": "Выберите файл с расширением .bin или .BIN",
        "eo": "Elektu dosieron kun la .bin aŭ .BIN finiĝo",
        "ja": ".binまたは.BIN拡張子のファイルを選択してください",
        "uk": "Виберіть файл з розширенням .bin або .BIN"
    },
    "file_processing_error": {
        "en": "An error occurred while processing the file",
        "ru": "Произошла ошибка при обработке файла",
        "eo": "Okazis eraro dum la prilaborado de la dosiero",
        "ja": "ファイルの処理中にエラーが発生しました",
        "uk": "Сталася помилка під час обробки файлу"
    },
    "no_file_selected": {
        "en": "No file selected",
        "ru": "Файл не выбран",
        "eo": "Neniu dosiero elektita",
        "ja": "ファイルが選択されていません",
        "uk": "Файл не вибрано"
    },
    "image_reload_error": {
        "en": "An error occurred while reloading the image",
        "ru": "Произошла ошибка при перезагрузке изображения",
        "eo": "Okazis eraro dum la reŝarĝado de la bildo",
        "ja": "画像の再読み込み中にエラーが発生しました",
        "uk": "Сталася помилка під час перезавантаження зображення"
    },
    "open_file_button": {
        "en": "Open File",
        "ru": "Открыть файл",
        "eo": "Malfermi Dosieron",
        "ja": "ファイルを開く",
        "uk": "Відкрити файл"
    },
    "width_label": {
        "en": "Image width (px):",
        "ru": "Ширина изображения (px):",
        "eo": "Bildo larĝo (pl):",
        "ja": "画像の幅 (px):",
        "uk": "Ширина зображення (px):"
    },
    "open_table_button": {
        "en": "Open Pixel Table",
        "ru": "Открыть таблицу пикселей",
        "eo": "Malfermi Pikselan Tabelon",
        "ja": "ピクセルテーブルを開く",
        "uk": "Відкрити таблицю пікселів"
    },
    "save_image_button": {
        "en": "Save Image",
        "ru": "Сохранить изображение",
        "eo": "Konservi Bildon",
        "ja": "画像を保存",
        "uk": "Зберегти зображення"
    },
    "save_bin_button": {
        "en": "Save as BIN File",
        "ru": "Сохранить в BIN файл",
        "eo": "Konservi kiel BIN-dosiero",
        "ja": "BINファイルとして保存",
        "uk": "Зберегти як BIN файл"
    },
    "reload_image_button": {
        "en": "Reload Image",
        "ru": "Перезагрузить изображение",
        "eo": "Reŝargi Bildon",
        "ja": "画像を再読み込み",
        "uk": "Перезавантажити зображення"
    },
    "redraw_grid_button": {
        "en": "Redraw Grid",
        "ru": "Перерисовать сетку",
        "eo": "Remalfermi Krado",
        "ja": "グリッドを再描画",
        "uk": "Перемалювати сітку"
    },
    "export_image_button": {
        "en": "Export Image",
        "ru": "Экспортировать изображение",
        "eo": "Eksporti Bildon",
        "ja": "画像をエクスポート",
        "uk": "Експортувати зображення"
    },
    "import_image_button": {
        "en": "Import Image",
        "ru": "Импортировать изображение",
        "eo": "Importi Bildon",
        "ja": "画像をインポート",
        "uk": "Імпортувати зображення"
    },
    "language_label": {
        "en": "Language:",
        "ru": "Язык:",
        "eo": "Lingvo:",
        "ja": "言語:",
        "uk": "Мова:"
    },
    "grid_color_label": {
        "en": "Grid Color (RGB):",
        "ru": "Цвет сетки (RGB):",
        "eo": "Krada Koloro (RGB):",
        "ja": "グリッドの色 (RGB):",
        "uk": "Колір сітки (RGB):"
    },
    "error": {
        "en": "Error",
        "ru": "Ошибка",
        "eo": "Eraro",
        "ja": "エラー",
        "uk": "Помилка"
    },
    "success": {
        "en": "Success",
        "ru": "Успех",
        "eo": "Sukceso",
        "ja": "成功",
        "uk": "Успіх"
    },
    "image_saved": {
        "en": "Image saved as",
        "ru": "Изображение сохранено как",
        "eo": "Bildo konservita kiel",
        "ja": "画像は以下の名前で保存されました",
        "uk": "Зображення збережено як"
    },
    "data_saved": {
        "en": "Data saved in",
        "ru": "Данные сохранены в",
        "eo": "Datumoj konservitaj en",
        "ja": "データは以下に保存されました",
        "uk": "Дані збережені в"
    },
    "open_image_first": {
        "en": "Open an image first",
        "ru": "Сначала откройте изображение",
        "eo": "Unue malfermu bildon",
        "ja": "まず画像を開いてください",
        "uk": "Спочатку відкрийте зображення"
    },
    "pixel_table": {
        "en": "Pixel Table",
        "ru": "Таблица пикселей",
        "eo": "Piksela Tabelo",
        "ja": "ピクセルテーブル",
        "uk": "Таблиця пікселів"
    },
    "table_settings": {
        "en": "Table Settings",
        "ru": "Настройка таблицы",
        "eo": "Tabele Agordoj",
        "ja": "テーブル設定",
        "uk": "Налаштування таблиці"
    },
    "enter_columns": {
        "en": "Enter the number of columns:",
        "ru": "Введите количество столбцов:",
        "eo": "Enigu la nombron da kolumnoj:",
        "ja": "列の数を入力してください:",
        "uk": "Введіть кількість стовпців:"
    },
    "column": {
        "en": "Column",
        "ru": "Столбец",
        "eo": "Kolumno",
        "ja": "列",
        "uk": "Стовпець"
    },
    "image_exported": {
        "en": "Image exported as",
        "ru": "Изображение экспортировано как",
        "eo": "Bildo eksportita kiel",
        "ja": "画像は以下の名前でエクスポートされました",
        "uk": "Зображення експортовано як"
    },
    "select_tiff_file": {
        "en": "Select TIFF File",
        "ru": "Выберите файл TIFF",
        "eo": "Elektu TIFF-dosieron",
        "ja": "TIFFファイルを選択してください",
        "uk": "Виберіть файл TIFF"
    },
    "image_size_mismatch": {
        "en": "Image size does not match the expected dimensions",
        "ru": "Размер изображения не соответствует ожидаемым размерам",
        "eo": "La bilda grando ne kongruas kun la atenditaj dimensioj",
        "ja": "画像のサイズが期待される寸法と一致しません",
        "uk": "Розмір зображення не відповідає очікуваним розмірам"
    },
    "image_import_error": {
        "en": "An error occurred while importing the image",
        "ru": "Произошла ошибка при импорте изображения",
        "eo": "Okazis eraro dum la importado de la bildo",
        "ja": "画像のインポート中にエラーが発生しました",
        "uk": "Сталася помилка під час імпорту зображення"
    }
}

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
        file_label.config(text=f"{translations['selected_file'][language.get()]} {file_path.split('/')[-1]}")
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
        file_label.config(text=translations["no_file_selected"][language.get()])

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
        canvas.config(scrollregion=(0, 0, zoomed_image.width, zoomed_image.height))
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

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

def toggle_pixel(event):
    global image
    x = int(canvas.canvasx(event.x) / zoom_level)
    y = int(canvas.canvasy(event.y) / zoom_level)
    if 0 <= x < image.width and 0 <= y < image.height:
        current_color = image.getpixel((x, y))
        new_color = 255 - current_color  # Инвертирование цвета
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

    table_window = tk.Toplevel(root)
    table_window.title(translations["pixel_table"][language.get()])

    table_frame = tk.Frame(table_window)
    table_frame.pack(fill=tk.BOTH, expand=True)

    columns = simpledialog.askinteger(translations["table_settings"][language.get()], translations["enter_columns"][language.get()], initialvalue=16)
    if not columns:
        columns = 16

    tree = ttk.Treeview(table_frame, columns=[f"col{i}" for i in range(columns)], show="headings")
    for i in range(columns):
        tree.heading(f"col{i}", text=f"{translations['column'][language.get()]} {i+1}")
        tree.column(f"col{i}", width=50, anchor='center')

    scrollbar_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    tree.pack(fill=tk.BOTH, expand=True)

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
        tree.insert('', tk.END, values=values)

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
    file_label.config(text=translations["no_file_selected"][language_code])
    open_button.config(text=translations["open_file_button"][language_code])
    width_label.config(text=translations["width_label"][language_code])
    table_button.config(text=translations["open_table_button"][language_code])
    save_button.config(text=translations["save_image_button"][language_code])
    save_bin_button.config(text=translations["save_bin_button"][language_code])
    reload_button.config(text=translations["reload_image_button"][language_code])
    redraw_grid_button.config(text=translations["redraw_grid_button"][language_code])
    export_button.config(text=translations["export_image_button"][language_code])
    import_button.config(text=translations["import_image_button"][language_code])
    language_label.config(text=translations["language_label"][language_code])
    grid_color_label.config(text=translations["grid_color_label"][language_code])

root = tk.Tk()
root.title(translations["title"]["en"])

file_path = ""
image = None
tk_image = None
zoom_level = 1.0

# Language selection
language = tk.StringVar(value="en")
language_options = ["en", "ru", "eo", "ja", "uk"]

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Editor Tab
editor_tab = ttk.Frame(notebook)
notebook.add(editor_tab, text=translations["editor_tab"]["en"])

file_label = tk.Label(editor_tab, text=translations["no_file_selected"]["en"])
file_label.pack(pady=5)

open_button = tk.Button(editor_tab, text=translations["open_file_button"]["en"], command=open_file)
open_button.pack(pady=5)

width_label = tk.Label(editor_tab, text=translations["width_label"]["en"])
width_label.pack(pady=5)

width_entry = tk.Entry(editor_tab)
width_entry.insert(0, "128")
width_entry.pack(pady=5)

table_button = tk.Button(editor_tab, text=translations["open_table_button"]["en"], command=open_table_window)
table_button.pack(pady=5)

save_button = tk.Button(editor_tab, text=translations["save_image_button"]["en"], command=save_image)
save_button.pack(pady=5)

save_bin_button = tk.Button(editor_tab, text=translations["save_bin_button"]["en"], command=save_to_bin)
save_bin_button.pack(pady=5)

reload_button = tk.Button(editor_tab, text=translations["reload_image_button"]["en"], command=reload_image)
reload_button.pack(pady=5)

redraw_grid_button = tk.Button(editor_tab, text=translations["redraw_grid_button"]["en"], command=redraw_grid)
redraw_grid_button.pack(pady=5)

export_button = tk.Button(editor_tab, text=translations["export_image_button"]["en"], command=export_image)
export_button.pack(pady=5)

import_button = tk.Button(editor_tab, text=translations["import_image_button"]["en"], command=import_image)
import_button.pack(pady=5)

canvas_frame = tk.Frame(editor_tab)
canvas_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
canvas.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(editor_tab, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
canvas.config(xscrollcommand=scrollbar_x.set)

zoom_scale = tk.Scale(editor_tab, from_=100, to=500, orient=tk.HORIZONTAL, label="Zoom Level (%)", command=update_zoom_level)
zoom_scale.set(100)
zoom_scale.pack(side=tk.BOTTOM, fill=tk.X)

canvas.bind("<Button-1>", toggle_pixel)
root.bind('<Control-r>', bind_hot_reload)

# Settings Tab
settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text=translations["settings_tab"]["en"])

language_label = tk.Label(settings_tab, text=translations["language_label"]["en"])
language_label.pack(pady=5)

language_menu = tk.OptionMenu(settings_tab, language, *language_options, command=update_language)
language_menu.pack(pady=5)

grid_color_label = tk.Label(settings_tab, text=translations["grid_color_label"]["en"])
grid_color_label.pack(pady=5)

grid_color_entry = tk.Entry(settings_tab)
grid_color_entry.insert(0, "255,0,0")
grid_color_entry.pack(pady=5)

# Update language initially
update_language()

# Запуск основного цикла приложения
root.mainloop()
