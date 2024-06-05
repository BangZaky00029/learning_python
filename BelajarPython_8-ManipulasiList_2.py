


dataAngka = [2, 5, 6, 2, 1, 4, 8, 4, 8, 9, 0, 8]
print(f"data Angka = {dataAngka} \n")

# count Data 
jumlahData_4 = dataAngka.count(4)
jumlahData_8 = dataAngka.count(8)
print(f"jumlah Angka 4 = {jumlahData_4}")
print(f"jumlah Angka 8 = {jumlahData_8}")



# Ambil Posisi data (index)
data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
index_Ujang = data.index("Ujang")
print(f"Posis si dudung = {index_dudung}")
print(f"Posis si Ujang = {index_Ujang}")

# mengurutkan data list
print(f"data Angka sebelum di urutkan = {dataAngka}")
dataAngka.sort()
print(f"data Angka Sort = {dataAngka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")


# Baliik list Descending
dataAngka.reverse()
data.reverse()
print(f" data di reverse  = {dataAngka} \n {data}")


#