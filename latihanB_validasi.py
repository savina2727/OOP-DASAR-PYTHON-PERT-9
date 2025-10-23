class Dosen:
    def __init__(self, nidn, nama):
# Cek apakah NIDN hanya berisi angka dan panjangnya 10
        if not (nidn.isdigit() and len(nidn) == 10):
            raise ValueError(f"❌ NIDN tidak valid untuk {nama}! Harus berupa 10 digit angka.")
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")
try:
    d1 = Dosen("1234567890", "Pak Triyono")#Valid
    d1.info()

    d2 = Dosen("098765432102", "Pak Tri")#Invalid (12 digit)
    d2.info()

except ValueError as e:
    print(e)
