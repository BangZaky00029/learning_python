# Manipulasi List



#index 0(-3)   1(-2)   2(-1)
data = ["ucup", "otong", "Dudung"]

# cara mengambil data  list ini 
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"Data Terakhir = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")




# info Jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")


## manipulasi data list 
# menambahkan item pada list sesuai posisi
print(f"data Sebelum di tambah = \n{data}")
          #(Posisi, data)
data.insert(1, "Asep")
print(f"data Sesudah ditambah = \n {data}")

# menambah data di akhir list
data.append("jajang")
print(f"data ditambah lagi = \n {data}")

# menambahkan list (menggabung list data)
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n {data}")

## Merubah data
# merubah data Ke-2 --> michael
data[2] = "Michael"
print(f"Update = {data}")

# Menghilangkan data (Remove)
data.remove("Ujang")
print(f"Data Remove = \n {data}")


# Meremove Dara Peling belakang
data_akhir = data.pop()
print(f"remove data akhir = \n {data}")

print(f"Data Akhir yang dihapus = {data_akhir}")

 