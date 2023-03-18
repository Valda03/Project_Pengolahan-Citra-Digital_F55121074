import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np

# Membuat GUI
root = tk.Tk()
root.title("GUI Aplikasi Penerapan Perbaikan Citra")
root.geometry("600x400")

# Membuat label pada hasil running
result_label = tk.Label(root, text="Perbaikan Citra", font=("Helvetica", 12))
result_label.pack(pady=10)

# Fungsi untuk memuat gambar dari folder
def open_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=(
    ("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))

    image = Image.open(file_path)

    gray_image = image.convert('L')

    binary_image = gray_image.point(lambda x: 0 if x<128 else 255, '1')

    # Menampilkan gambar Original menggunakan Tkinter
    tk_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, text="Original Image", image=tk_image)
    image_label.image = tk_image

    # Menampilkan gambar Grayscale menggunakan Tkinter
    gray_tk_image = ImageTk.PhotoImage(gray_image)
    gray_label = tk.Label(root, text="Grayscale Image", image=gray_tk_image)
    gray_label.image = gray_tk_image

    # Menampilkan gambar Binary menggunakan Tkinter
    binary_tk_image = ImageTk.PhotoImage(binary_image)
    binary_label = tk.Label(root, text="Binary Image", image=binary_tk_image)
    binary_label.image = binary_tk_image

    # Membuat frame
    frame = tk.Frame(root)
    frame.pack()

    # Menambahkan Label pada gambar
    image_label.pack(side=tk.LEFT, padx=10)
    tk.Label(frame, text="Original Image").pack(side=tk.LEFT)
    gray_label.pack(side=tk.LEFT, padx=10)
    tk.Label(frame, text="                                      Grayscale Image").pack(side=tk.LEFT)
    binary_label.pack(side=tk.LEFT, padx=10)
    tk.Label(frame, text="                                      Binary Image").pack(side=tk.LEFT)

# Membuat button untuk membuka gambar
open_button = tk.Button(root, text="Pilih Gambar", command=open_image)
open_button.pack(pady=10)

# Membuat frame untuk membatasi hasil running
box = tk.Frame(root, width=550, height=1, bg="black")
box.pack(pady=10)

# Membuat label untuk menampilkan nama pembuat
creator_label = tk.Label(root, text="Nama : Valda Laura Uswary     NIM : F55121074     Kelas : B", font=("Helvetica", 10))
creator_label.pack(side="bottom")

root.mainloop()