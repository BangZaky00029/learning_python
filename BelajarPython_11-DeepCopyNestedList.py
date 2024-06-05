data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data Copy = {data_2D_copy}")



# Cara Mengambil data 
data = data_2D[1][0]
print((f"data = {data}"))

# output address
print(f"address Asli = {hex(id(data_2D))}")
print(f"address Copy = {hex(id(data_2D_copy))}")


print("address dari member ke-1")
print(f"Address Asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_copy[0]))}")


# data_2D[1][0] = 5
# data_2D[2] = 9
# print(f"data = {data_2D}")
# print(f"data copy = {data_2D_copy}") 

# menggunakan deepcopy

from copy import deepcopy 

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address Asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_copy[0]))}")


