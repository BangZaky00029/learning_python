# Mengkopi List (Teknik menduplikat list)

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a 
print(f"b = {b}")

## kita akan merubah member dari a
# ini akan merubah kedua list
a[0] = "Zaky"
b.sort()
print(f"a = {a}")
print(f"b = {b}")


# Cek Address Dari Kedua List a & b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c= a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")



print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "Dadang" # full duplikan / membuat data baru

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 2")
a[2] = "Aulia"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
