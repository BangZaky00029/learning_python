# Belajar List (Kumpulan datas)
Data_ku_string = [1, 2, 3, 4, 5, 6]
print(Data_ku_string)


# Kumpilan Data String
Data_string = ["ucup","Otong","Odah"]
print(Data_string)

# List Boolean 
data_boolean = [True, False, True, False, False]
print(data_boolean)

# list Campuran 
data_campuran = [1, "Duren", 2, "Cireng", False, "Iqbal", True]
print(data_campuran)


## Cara alternatif Membuat List
data_range = range(0, 10, 2) #range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)


## Membuat list dengan for loop, list comprehension
ListPakeFor = [i**3 for i in range(0, 10)]
print(ListPakeFor)


# Membuat list pake for pake if
listPakeForIf = [i for i in range(0, 10) if i != 5]
print(listPakeForIf)
# Output Genap
listPakeForIf = [i for i in range(0, 10) if i%2 == 0]
print(listPakeForIf)
# Output Ganjil
listPakeForIf = [i for i in range(0, 100) if i%2 == 1]
print(listPakeForIf)