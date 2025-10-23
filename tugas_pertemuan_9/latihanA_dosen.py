class Dosen:
    def __init__(self, nidn, nama):
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")

# Buat dua objek dan panggil method info()
d1 = Dosen("1234567890", "Pak Triyono")
d2 = Dosen("0987654321", "Pak Joni")

d1.info()
d2.info()
