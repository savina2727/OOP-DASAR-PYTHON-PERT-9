class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

# Simpan beberapa mahasiswa
daftar_mhs = [
    Mahasiswa("230103173", "Savina"),
    Mahasiswa("230103172", "Dyah"),
    Mahasiswa("230103171", "Arwiana"),
    Mahasiswa("230103174", "Sasa"),
]

# Cetak yang namanya huruf awal S atau A
print("Mahasiswa dengan huruf awal S atau A:")
for m in daftar_mhs:
    if m.nama.startswith(("S", "A")):
        print(f"{m.nim} - {m.nama}")
