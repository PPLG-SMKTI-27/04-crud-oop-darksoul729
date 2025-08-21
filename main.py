# data buku

from tabulate import tabulate


books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]



# data peminjaman
records = [
    {"isbn": "9786237121144", "status": "Selesai", "nama": "Andi", "tanggal_pinjam": "2023-10-01", "tanggal_kembali": "24-02-2009"},
    {"isbn": "9786026163905", "status" : "Belum" ,"nama": "Budi", "tanggal_pinjam": "2023-10-02", "tanggal_kembali": None},
]

def tampilkan_data():
    print("---=== DATA BUKU ===---")
    print(tabulate(books, headers="keys", tablefmt="grid"))
    if not books:
        print("Tidak ada data buku yang tersedia.")    
    print("-----------------------")

def tambah_data():
    print("---=== TAMBAH DATA BUKU ===---")
    isbn = input("Masukkan ISBN: ")
    judul = input("Masukkan Judul: ")
    pengarang = input("Masukkan Pengarang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    terpinjam = 0
    books.append({"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": jumlah, "terpinjam": terpinjam})
    print("Data buku berhasil ditambahkan.")
    tampilkan_data()


def edit_data():
    print("---=== EDIT DATA BUKU ===---")
    isbn = input("Masukkan ISBN buku yang ingin diedit: ")
    for book in books:
        if book['isbn'] == isbn:
            book['judul'] = input("Masukkan Judul baru: ")
            book['pengarang'] = input("Masukkan Pengarang baru: ")
            book['jumlah'] = int(input("Masukkan Jumlah baru: "))
            print("Data buku berhasil diubah.")
            tampilkan_data()
            return
    print("Buku dengan ISBN tersebut tidak ditemukan.")
    print("-----------------------")
    print("Data buku tidak ditemukan.")
    print("-----------------------")
    ...

def hapus_data():
    print("---=== HAPUS DATA BUKU ===---")
    isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
    for book in books:  
        if book['isbn'] == isbn:
            books.remove(book)
            print("Data buku berhasil dihapus.")
            tampilkan_data()
            return
    print("Buku dengan ISBN tersebut tidak ditemukan.")
    print("-----------------------")
    print("Data buku tidak ditemukan.")
    ...

def tampilkan_peminjaman():
    print("---=== DATA PEMINJAMAN ===---")
    print(tabulate(records, headers="keys", tablefmt="grid")) 
    print("-----------------------------")
    ...

def tampilkan_belum():
    print("---=== PEMINJAMAN BELUM KEMBALI ===---")
    print(tabulate([record for record in records if record['tanggal_kembali'] is None], headers="keys", tablefmt="grid"))    
    ...

def peminjaman():
    print("---=== PEMINJAMAN BUKU ===---")
    tampilkan_data()    
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    nama = input("Masukkan Nama Peminjam: ")
    tanggal_pinjam = input("Masukkan Tanggal Pinjam (YYYY-MM-DD): ")
    for book in books:
        if book['isbn'] == isbn:
            if book['jumlah'] > book['terpinjam']:
                book['jumlah'] -= 1
                book['terpinjam'] += 1
                records.append({"isbn": isbn, "nama": nama, "status": "Belum", "tanggal_pinjam": tanggal_pinjam, "tanggal_kembali": None})
                print("Buku berhasil dipinjam.")
                tampilkan_peminjaman()
                return
            else:
                print("Buku tidak tersedia untuk dipinjam.")
                return
    print("Buku dengan ISBN tersebut tidak ditemukan.")
    print("-----------------------")
    ...

def pengembalian():
    print("---=== PENGEMBALIAN BUKU ===---")
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    for book in books:
        if book['isbn'] == isbn:
            for record in records:
                if record['isbn'] == isbn and record['tanggal_kembali'] is None:
                    book['terpinjam'] -= 1
                    book['jumlah'] += 1
                    record['tanggal_kembali'] = input("Masukkan Tanggal Kembali (YYYY-MM-DD): ")
                    record['status'] = "Selesai"
                    print("Buku berhasil dikembalikan.")
                    tampilkan_peminjaman()
                    return
            print("Buku ini belum dipinjam atau sudah dikembalikan.")
            return
    print("Buku Dengan ISBN tersebut tidak ditemukan.")
    ...


while True :
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")

    if menu == "1":
        tampilkan_data()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "2":
        tambah_data()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "3":
        edit_data()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "4":
        hapus_data()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "5":
        tampilkan_peminjaman()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "6":
        tampilkan_belum()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "7":
        peminjaman()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu == "8":
        pengembalian()
        input("Tekan Enter untuk kembali ke menu...")
    elif menu.lower() == "x":   
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu...")
    