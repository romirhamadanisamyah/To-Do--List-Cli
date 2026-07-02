# Project 2: To-Do List App CLI
# Dibuat oleh: Romi Rhamadani Samyah
# Belajar: CRUD, List of Dictionary, File Handling

DATA_FILE = "tugas.txt"
daftar_tugas = []

def load_data():
    """Ambil data tugas dari file.txt"""
    global daftar_tugas
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                status, tugas = line.strip().split("|", 1)
                daftar_tugas.append({"tugas": tugas, "selesai": status == "1"})
    except FileNotFoundError:
        pass

def save_data():
    """Simpan data tugas ke file.txt"""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for item in daftar_tugas:
            status = "1" if item["selesai"] else "0"
            file.write(f"{status}|{item['tugas']}\n")

def tambah_tugas():
    print("\n--- TAMBAH TUGAS BARU ---")
    tugas = input("Masukkan tugas: ")
    daftar_tugas.append({"tugas": tugas, "selesai": False})
    save_data()
    print(f"Tugas '{tugas}' berhasil ditambahkan!")

def lihat_tugas():
    print("\n--- DAFTAR TUGAS ---")
    if not daftar_tugas:
        print("Belum ada tugas. Santai dulu 😎")
        return
    for i, item in enumerate(daftar_tugas, 1):
        status = "[x]" if item["selesai"] else "[ ]"
        print(f"{i}. {status} {item['tugas']}")

def tandai_selesai():
    lihat_tugas()
    if not daftar_tugas: return
    try:
        nomor = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor <= len(daftar_tugas):
            daftar_tugas[nomor-1]["selesai"] = True
            save_data()
            print("Mantap! Tugas ditandai selesai ✅")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")

def hapus_tugas():
    lihat_tugas()
    if not daftar_tugas: return
    try:
        nomor = int(input("Masukkan nomor tugas yang mau dihapus: "))
        if 1 <= nomor <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor-1)["tugas"]
            save_data()
            print(f"Tugas '{tugas_dihapus}' berhasil dihapus 🗑️")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")

def main():
    load_data()
    while True:
        print("\n===== TO-DO LIST CLI =====")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")

        pilihan = input("Pilih menu 1-5: ")

        if pilihan == '1': lihat_tugas()
        elif pilihan == '2': tambah_tugas()
        elif pilihan == '3': tandai_selesai()
        elif pilihan == '4': hapus_tugas()
        elif pilihan == '5':
            print("Sampai jumpa! Jangan lupa kerjain tugasnya ya.")
            break
        else: print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
