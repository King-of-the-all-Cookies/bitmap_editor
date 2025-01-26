# Bitmap Editor Documentation

## Table of Contents
- [English](#english)
- [Русский](#русский)
- [Esperanto](#esperanto)
- [日本語](#日本語)
- [Українська](#українська)

## Overview
The Bitmap Editor is a graphical user interface (GUI) application built using Python's `tkinter` library. It allows users to open, edit, and save bitmap images stored in `.bin` files. The application supports multiple languages, including English, Russian, Esperanto, Japanese, and Ukrainian.

## Features
- **Open and Save Images**: Open `.bin` files and save edited images as `.tiff` or `.bin` files.
- **Pixel Editing**: Toggle individual pixels on the image.
- **Grid Display**: Display a grid over the image for easier editing.
- **Zoom**: Zoom in and out of the image.
- **Language Support**: Switch between multiple languages for the user interface.
- **Pixel Table**: View pixel values in a tabular format.
- **Import/Export Images**: Import `.tiff` images and export edited images.

## User Interface
The user interface is divided into two main tabs:
1. **Editor Tab**: Contains tools for opening, editing, and saving images.
2. **Settings Tab**: Allows users to change the language and grid color.

### Editor Tab
- **Open File**: Open a `.bin` file to edit.
- **Width**: Specify the width of the image in pixels.
- **Open Pixel Table**: View the pixel values in a table.
- **Save Image**: Save the edited image as a `.tiff` file.
- **Save as BIN File**: Save the edited image as a `.bin` file.
- **Reload Image**: Reload the image from the file.
- **Redraw Grid**: Redraw the grid over the image.
- **Export Image**: Export the image as a `.tiff` file.
- **Import Image**: Import a `.tiff` image.
- **Canvas**: Display the image and allow pixel editing.
- **Zoom**: Adjust the zoom level of the image.

### Settings Tab
- **Language**: Select the language for the user interface.
- **Grid Color**: Specify the color of the grid in RGB format.

## Detailed Functionality

### Opening and Saving Images
- **Open File**: Use the "Open File" button to select a `.bin` file. The file is interpreted as a bitmap image based on the specified width.
- **Save Image**: Use the "Save Image" button to save the edited image as a `.tiff` file.
- **Save as BIN File**: Use the "Save as BIN File" button to save the edited image as a `.bin` file.

### Editing Pixels
- **Toggle Pixel**: Click on a pixel in the canvas to toggle its color between black and white.

### Grid Display
- **Redraw Grid**: Use the "Redraw Grid" button to redraw the grid over the image. The grid color can be specified in the settings.

### Zoom
- **Zoom Level**: Adjust the zoom level using the scrollbar or mouse wheel.

### Language Support
- **Language Selection**: Use the dropdown menu in the settings tab to select the language for the user interface.

### Pixel Table
- **Open Pixel Table**: Use the "Open Pixel Table" button to view the pixel values in a table. The number of columns in the table can be specified.

### Import/Export Images
- **Export Image**: Use the "Export Image" button to export the edited image as a `.tiff` file.
- **Import Image**: Use the "Import Image" button to import a `.tiff` image. The imported image must match the expected dimensions.

## Error Handling
- The application displays error messages for various scenarios, such as file processing errors, image reload errors, and image import errors.

## Language-Specific Documentation

### English
#### Open File
- **Button**: Open File
- **Description**: Open a `.bin` file to edit.

#### Save Image
- **Button**: Save Image
- **Description**: Save the edited image as a `.tiff` file.

#### Save as BIN File
- **Button**: Save as BIN File
- **Description**: Save the edited image as a `.bin` file.

#### Reload Image
- **Button**: Reload Image
- **Description**: Reload the image from the file.

#### Redraw Grid
- **Button**: Redraw Grid
- **Description**: Redraw the grid over the image.

#### Export Image
- **Button**: Export Image
- **Description**: Export the image as a `.tiff` file.

#### Import Image
- **Button**: Import Image
- **Description**: Import a `.tiff` image.

#### Language
- **Label**: Language
- **Description**: Select the language for the user interface.

#### Grid Color
- **Label**: Grid Color (RGB)
- **Description**: Specify the color of the grid in RGB format.

### Русский
#### Открыть файл
- **Кнопка**: Открыть файл
- **Описание**: Откройте `.bin` файл для редактирования.

#### Сохранить изображение
- **Кнопка**: Сохранить изображение
- **Описание**: Сохраните отредактированное изображение как `.tiff` файл.

#### Сохранить в BIN файл
- **Кнопка**: Сохранить в BIN файл
- **Описание**: Сохраните отредактированное изображение как `.bin` файл.

#### Перезагрузить изображение
- **Кнопка**: Перезагрузить изображение
- **Описание**: Перезагрузите изображение из файла.

#### Перерисовать сетку
- **Кнопка**: Перерисовать сетку
- **Описание**: Перерисуйте сетку над изображением.

#### Экспортировать изображение
- **Кнопка**: Экспортировать изображение
- **Описание**: Экспортируйте изображение как `.tiff` файл.

#### Импортировать изображение
- **Кнопка**: Импортировать изображение
- **Описание**: Импортируйте `.tiff` изображение.

#### Язык
- **Метка**: Язык
- **Описание**: Выберите язык для интерфейса.

#### Цвет сетки (RGB)
- **Метка**: Цвет сетки (RGB)
- **Описание**: Укажите цвет сетки в формате RGB.

### Esperanto
#### Malfermi Dosieron
- **Butono**: Malfermi Dosieron
- **Priskribo**: Malfermu `.bin` dosieron por redakti.

#### Konservi Bildon
- **Butono**: Konservi Bildon
- **Priskribo**: Konservu la redaktitan bildon kiel `.tiff` dosieron.

#### Konservi kiel BIN-dosiero
- **Butono**: Konservi kiel BIN-dosiero
- **Priskribo**: Konservu la redaktitan bildon kiel `.bin` dosieron.

#### Reŝargi Bildon
- **Butono**: Reŝargi Bildon
- **Priskribo**: Reŝargu la bildon el la dosiero.

#### Remalfermi Krado
- **Butono**: Remalfermi Krado
- **Priskribo**: Remalfermu la krado super la bildo.

#### Eksporti Bildon
- **Butono**: Eksporti Bildon
- **Priskribo**: Eksportu la bildon kiel `.tiff` dosieron.

#### Importi Bildon
- **Butono**: Importi Bildon
- **Priskribo**: Importu `.tiff` bildon.

#### Lingvo
- **Etikedo**: Lingvo
- **Priskribo**: Elektu la lingvon por la uzantinterfaco.

#### Krada Koloro (RGB)
- **Etikedo**: Krada Koloro (RGB)
- **Priskribo**: Specifu la koloron de la kradon en RGB formato.

### 日本語
#### ファイルを開く
- **ボタン**: ファイルを開く
- **説明**: `.bin` ファイルを開いて編集します。

#### 画像を保存
- **ボタン**: 画像を保存
- **説明**: 編集した画像を `.tiff` ファイルとして保存します。

#### BINファイルとして保存
- **ボタン**: BINファイルとして保存
- **説明**: 編集した画像を `.bin` ファイルとして保存します。

#### 画像を再読み込み
- **ボタン**: 画像を再読み込み
- **説明**: ファイルから画像を再読み込みます。

#### グリッドを再描画
- **ボタン**: グリッドを再描画
- **説明**: 画像の上にグリッドを再描画します。

#### 画像をエクスポート
- **ボタン**: 画像をエクスポート
- **説明**: 画像を `.tiff` ファイルとしてエクスポートします。

#### 画像をインポート
- **ボタン**: 画像をインポート
- **説明**: `.tiff` 画像をインポートします。

#### 言語
- **ラベル**: 言語
- **説明**: ユーザーインターフェースの言語を選択します。

#### グリッドの色 (RGB)
- **ラベル**: グリッドの色 (RGB)
- **説明**: RGB形式でグリッドの色を指定します。

### Українська
#### Відкрити файл
- **Кнопка**: Відкрити файл
- **Опис**: Відкрийте `.bin` файл для редагування.

#### Зберегти зображення
- **Кнопка**: Зберегти зображення
- **Опис**: Збережіть відредаговане зображення як `.tiff` файл.

#### Зберегти як BIN файл
- **Кнопка**: Зберегти як BIN файл
- **Опис**: Збережіть відредаговане зображення як `.bin` файл.

#### Перезавантажити зображення
- **Кнопка**: Перезавантажити зображення
- **Опис**: Перезавантажте зображення з файлу.

#### Перемалювати сітку
- **Кнопка**: Перемалювати сітку
- **Опис**: Перемалюйте сітку над зображенням.

#### Експортувати зображення
- **Кнопка**: Експортувати зображення
- **Опис**: Експортуйте зображення як `.tiff` файл.

#### Імпортувати зображення
- **Кнопка**: Імпортувати зображення
- **Опис**: Імпортуйте `.tiff` зображення.

#### Мова
- **Мітка**: Мова
- **Опис**: Виберіть мову для інтерфейсу.

#### Колір сітки (RGB)
- **Мітка**: Колір сітки (RGB)
- **Опис**: Вкажіть колір сітки в форматі RGB.
