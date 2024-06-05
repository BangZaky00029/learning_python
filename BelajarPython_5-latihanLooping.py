# LATIHAN looping membuat segitiga


# Segitiga Siku - Siku

# sisi = 10

# # Dummy variabel
# # Dengan For
# count = 1
# for i in range(sisi): 
#     print("*" * count)
#     count += 1
    
# data_ku = {"manusia", "hewan", "Flora", "Fauna"}

# # Ubah data_ku menjadi list
# list_data_ku = list(data_ku)

# # Menggunakan range untuk mengulangi indeks list_data_ku
# for i in range(len(list_data_ku)):
#     print(f" - {list_data_ku[i]}")



# data_ku = {"Manusia", "hewan", "Flora", "Fauna", "Herbifora"}

# # Ubah data_ku menjadi list
# list_data_ku = list(data_ku)

# # Menggunakan enumerate untuk mendapatkan indeks dan nilai
# for i, item in enumerate(list_data_ku, start=1):
#     print(f"{i}. {item}")










# 1. Segitiga Siku - Siku


sisi = 9

# Dummy variabel
# Dengan For
print("awal For")
count = 1
for i in range(sisi): 
    print("*" * count)
    count += 1

print("\nAkhir For")
# 2. menggunakan While 
count = 1 
while True :
    print("*" * count)
    count += 1 

    if count > sisi:
        break


print("akhir While\n")



# 3. menggunakan While (Ganjil saja)
count = 1 
while True :
    if (count % 2):
        print("* " * count)
        count += 1
    else :
        count += 1
        continue
    
    if count > sisi:
        break







# SEGITIGA SAMA KAKI

count = 1 
space = int(sisi / 2)
while True :
    if (count % 2):
        print(" " * space, "+" * count)
        space -= 1
        count += 1
    else :
        count += 1
        continue
    
    if count > sisi:
        break