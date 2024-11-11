#membuat tampilan gui
import tkinter as tk #mengimpor tkinter dan alias tk untuk gui
from tkinter import messagebox #mengimpor messagecox dari tkinter

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi(): #membuat fungsi memvalidasi nilai yg diinput 
    try:
        for entry in input_entries: #memeriksa nilai input
            nilai = int(entry.get()) # mengambil nilai input dan mengubah ke integer
            if not (0 <= nilai <= 100): #kondisi mengecek nilai berada 0 sampai 100
                raise ValueError("Nilai harus antara 0 dan 100") # mengirim pesan jika kondisi tidak sesuai
        output_label.config(text="Prediksi Prodi: Teknologi Informasi") #mengatur output untuk menampilkan hasil prediksi
    except ValueError as ve: #menangkap valueerror yang mungkin terjadi
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100") # menampilkan kotak pesan error

# Membuat jendela utama
root = tk.Tk() #membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan") # mengatur judul jendela aplikasi
root.geometry("500x600") # mengatur ukuran jendela
root.configure(bg="#007FFF")  # Mengatur warna latar belakang menjadi biru

# membuat teks ke tengah
root.grid_rowconfigure(0, weight=1) #mengatur distribusi ruang vertikal di grid pada baris
root.grid_rowconfigure(13, weight=1) #menambahkan bobot pada baris di atas 0 dan bawah 13 dari grid
root.grid_columnconfigure(0, weight=1) #mengatur distribusi ruang horizontal di grid pada kolom
root.grid_columnconfigure(1, weight=1) #mengatur distribusi ruang horizontal di grid pada kolom

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#007FFF", fg="white")
#membuat teks yang ditampilkan dengan font arial 16 warna label sama dengan jendela dan warna teks putih
judul_label.grid(row=1, column=0, columnspan=2, pady=10) #menempatkan label baris 1, kolom 0, melebar 2 kolom, jarak vertikal diatas bawah 10

# Membuat input untuk 10 nilai mata pelajaran
input_labels = [] #membuat list kosong label
input_entries = [] #membuat list kosong entries (kolom input)

for i in range(10):
    input_label = tk.Label(root, text=f"Nilai Mata Pelajaran {i + 1}:", bg="#007FFF", fg="white") #Membuat label teks menggunakan tk.Label
    input_entry = tk.Entry(root) #Membuat kolom input untuk nilai mata pelajaran, menggunakan tk.Entry
    input_label.grid(row=i + 2, column=0, padx=10, pady=5, sticky="e") #Menempatkan label di grid layout, di baris dan kolom yang ditentukan.
    input_entry.grid(row=i + 2, column=1, padx=10, pady=5) #Menempatkan kolom input di grid layout pada baris dan kolom yang sama dengan label terkait
    input_labels.append(input_label) # Menambahkan kolom input yang baru dibuat ke list
    input_entries.append(input_entry) # Menambahkan kolom input yang baru dibuat ke list

# Tombol Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi) #Membuat tombol untuk menampilkan hasil prediksi ketika diklik.
prediksi_button.grid(row=12, column=0, columnspan=2, pady=10) # Menempatkan tombol pada baris 12, melebar di dua kolom, dengan jarak vertikal pady=10

# Label untuk menampilkan hasil
output_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12), bg="#007FFF", fg="white") # membuat label untuk hasil prediksi
output_label.grid(row=13, column=0, columnspan=2, pady=10) #Menempatkan label di baris 13 dan melebar hingga dua kolom, dengan pady=10

# Menjalankan loop utama aplikasi
root.mainloop()







