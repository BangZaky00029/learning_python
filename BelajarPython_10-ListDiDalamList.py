# Membuat list di dalam list

data_0 = [1,2]
data_1 = [3,4]

dataListBiasa = [1,2,3,4]
print(f"list biasa = {dataListBiasa}")


list_2D = [data_0, data_1, dataListBiasa]
print(f"list 2 D = {list_2D}")

list_2D = [data_0, data_1, 2,5,1,8]
print(f"list 2 D = {list_2D}")






# CONTOH PENGGUNAAN  
peserta_0 = ["ucup",24,"Laki - Laki"]
peserta_1 = ["otong",21,"Laki - Laki"]
peserta_2 = ["dedeh",26,"Perempuan"]

listPeserta = [peserta_0,peserta_1,peserta_2]

print(f" Peserta = {listPeserta}")

for peserta in listPeserta :
    print("\n===== Daftar List =====")
    print(f"Nama\t= {peserta[0]}")
    print(f"Umur\t= {peserta[1]}")
    print(f"Gender\t= {peserta[2]}")
    
    
    
# # Inisialisasi daftar peserta kosong
# listPeserta = []

# # Tentukan jumlah peserta yang akan dimasukkan
# jumlah_peserta = int(input("Masukkan jumlah peserta: "))

# # Loop untuk memasukkan data setiap peserta
# for i in range(jumlah_peserta):
#     print(f"\nMasukkan data peserta ke-{i + 1}:")
#     nama = input("Nama: ")
#     umur = int(input("Umur: "))
#     gender = input("Gender: ")
    
#     # Buat daftar untuk peserta saat ini dan tambahkan ke listPeserta
#     peserta = [nama, umur, gender]
#     listPeserta.append(peserta)

# # Cetak daftar peserta
# print(f"\nPeserta = {listPeserta}")

# # Loop untuk menampilkan data setiap peserta
# for peserta in listPeserta:
#     print("\n===== Daftar List =====")
#     print(f"Nama\t= {peserta[0]}")
#     print(f"Umur\t= {peserta[1]}")
#     print(f"Gender\t= {peserta[2]}")


# dengan reference 

listCopy = listPeserta.copy();
print(f"Peserta = {listCopy}")
peserta_0[0] = "UDIN"
print(f"peserta = {listCopy}")
print(f"peserta = {listPeserta}")


