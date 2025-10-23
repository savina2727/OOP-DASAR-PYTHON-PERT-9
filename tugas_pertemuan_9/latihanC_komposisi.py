class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.peserta = []

    def tambah_peserta(self, nama):
        if len(self.peserta) >= self.ruang.kapasitas:
            print("Gagal: Ruang sudah penuh!")
        else:
            self.peserta.append(nama)
            print(f"{nama} berhasil ditambahkan ke {self.kode_kelas}")

    def list_peserta(self):
        print(f"Peserta di {self.kode_kelas}: {self.peserta}")

r1 = Ruang("LAB-02", 2)
kelas = KelasKuliah("TI23A5", r1)
kelas.tambah_peserta("Savina")
kelas.tambah_peserta("Dyah")
kelas.tambah_peserta("Arwiana")  # Harus gagal
kelas.list_peserta()
