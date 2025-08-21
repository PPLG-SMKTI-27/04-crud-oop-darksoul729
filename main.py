from tabulate import tabulate
from datetime import datetime

class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam
    
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "judul": self.judul,
            "pengarang": self.pengarang,
            "jumlah": self.jumlah,
            "terpinjam": self.terpinjam
        }

class Record:
    def __init__(self, isbn, nama, status, tanggal_pinjam, tanggal_kembali=None):
        self.isbn = isbn
        self.nama = nama
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "status": self.status,
            "nama": self.nama,
            "tanggal_pinjam": self.tanggal_pinjam,
            "tanggal_kembali": self.tanggal_kembali
        }

class Perpustakaan:
    def __init__(self):
        self.books = [
            Buku("9786237121144", "Kumpulan Solusi Pemrograman Python", "Budi Raharjo", 6),
            Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15),
            Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, terpinjam=1),
            Buku("9786022912828", "Animal Farm", "George Orwell", 4)
        ]
        self.records = [
            Record("9786237121144", "Andi", "Selesai", "2023-10-01", "2023-10-08"),
            Record("9786026163905", "Budi", "Belum", "2023-10-02")
        ]

    def mencari_buku(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def mencari_record_aktif(self, isbn):
        for record in self.records:
            if record.isbn == isbn and record.status == "Belum":
                return record
        return None

    def tampilkan_buku(self):
        print("---=== DATA BUKU ===---")
        if not self.books:
            print("Tidak ada data buku yang tersedia.")
        else:
            book_data = [book.to_dict() for book in self.books]
            print(tabulate(book_data, headers="keys", tablefmt="grid"))
        print("-----------------------")

    def menambahkan_buku(self):
        print("---=== TAMBAH DATA BUKU ===---")
        isbn = input("Masukkan ISBN: ")
        judul = input("Masukkan Judul: ")
        pengarang = input("Masukkan Pengarang: ")
        try:
            jumlah = int(input("Masukkan Jumlah: "))
            new_book = Buku(isbn, judul, pengarang, jumlah)
            self.books.append(new_book)
            print("Data buku berhasil ditambahkan.")
        except ValueError:
            print("Jumlah harus berupa angka.")
        self.tampilkan_buku()

    def edit_buku(self):
        print("---=== EDIT DATA BUKU ===---")
        isbn = input("Masukkan ISBN buku yang ingin diedit: ")
        book = self.mencari_buku(isbn)
        if book:
            book.judul = input(f"Masukkan Judul baru ({book.judul}): ") or book.judul
            book.pengarang = input(f"Masukkan Pengarang baru ({book.pengarang}): ") or book.pengarang
            try:
                new_jumlah = input(f"Masukkan Jumlah baru ({book.jumlah}): ")
                if new_jumlah:
                    book.jumlah = int(new_jumlah)
                print("Data buku berhasil diubah.")
            except ValueError:
                print("Jumlah harus berupa angka.")
            self.tampilkan_buku()
        else:
            print("Buku dengan ISBN tersebut tidak ditemukan.")
            print("-----------------------")
    
    def hapus_buku(self):
        print("---=== HAPUS DATA BUKU ===---")
        isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
        book = self.mencari_buku(isbn)
        if book:
            self.books.remove(book)
            print("Data buku berhasil dihapus.")
            self.tampilkan_buku()
        else:
            print("Buku dengan ISBN tersebut tidak ditemukan.")
            print("-----------------------")

    def tampilkan_semua_peminjaman(self):
        print("---=== DATA PEMINJAMAN ===---")
        record_data = [record.to_dict() for record in self.records]
        print(tabulate(record_data, headers="keys", tablefmt="grid"))
        print("-----------------------------")

    def tampilkan_peminjaman_belum_kembali(self):
        print("---=== PEMINJAMAN BELUM KEMBALI ===---")
        pending_records = [record.to_dict() for record in self.records if record.status == "Belum"]
        print(tabulate(pending_records, headers="keys", tablefmt="grid"))
        print("---------------------------------------")

    def peminjaman_buku(self):
        print("---=== PEMINJAMAN BUKU ===---")
        self.tampilkan_buku()
        isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
        book = self.mencari_buku(isbn)
        if book:
            if book.jumlah > book.terpinjam:
                nama = input("Masukkan Nama Peminjam: ")
                tanggal_pinjam = datetime.now().strftime("%Y-%m-%d")
                book.terpinjam += 1
                new_record = Record(isbn, nama, "Belum", tanggal_pinjam)
                self.records.append(new_record)
                print("Buku berhasil dipinjam.")
                self.tampilkan_semua_peminjaman()
            else:
                print("Buku tidak tersedia untuk dipinjam.")
        else:
            print("Buku dengan ISBN tersebut tidak ditemukan.")
            print("-----------------------")
    
    def pengembalian_buku(self):
        print("---=== PENGEMBALIAN BUKU ===---")
        isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
        book = self.mencari_buku(isbn)
        if book:
            record = self.mencari_record_aktif(isbn)
            if record:
                tanggal_kembali = datetime.now().strftime("%Y-%m-%d")
                record.tanggal_kembali = tanggal_kembali
                record.status = "Selesai"
                book.terpinjam -= 1
                book.jumlah += 1
                print("Buku berhasil dikembalikan.")
                self.tampilkan_semua_peminjaman()
            else:
                print("Buku ini belum dipinjam atau sudah dikembalikan.")
        else:
            print("Buku Dengan ISBN tersebut tidak ditemukan.")
            print("-----------------------")

def main_menu():
    perpustakaan = Perpustakaan()
    while True:
        print("\n---=== MENU ===---")
        print("[1] Tampilkan Data Buku")
        print("[2] Tambah Data Buku")
        print("[3] Edit Data Buku")
        print("[4] Hapus Data Buku")
        print("------------------")
        print("[5] Tampilkan Semua Peminjaman")
        print("[6] Tampilkan Peminjaman Belum Kembali")
        print("[7] Peminjaman Buku")
        print("[8] Pengembalian Buku")
        print("[X] Keluar")
        
        menu = input("Masukkan pilihan menu (1-8 atau x): ")

        if menu == "1":
            perpustakaan.tampilkan_buku()
        elif menu == "2":
            perpustakaan.menambahkan_buku()
        elif menu == "3":
            perpustakaan.edit_buku()
        elif menu == "4":
            perpustakaan.hapus_buku()
        elif menu == "5":
            perpustakaan.tampilkan_semua_peminjaman()
        elif menu == "6":
            perpustakaan.tampilkan_peminjaman_belum_kembali()
        elif menu == "7":
            perpustakaan.peminjaman_buku()
        elif menu == "8":
            perpustakaan.pengembalian_buku()
        elif menu.lower() == "x":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        if menu.lower() != "x":
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main_menu()