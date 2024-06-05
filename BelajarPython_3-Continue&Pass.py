# Continue, Pass And Break




# Pass --> Dia berfungsi sebagai dummy, tidak di eksekusi 

# angka = 0 

# while angka < 5 :
#     angka += 1 
#     if angka == 3:
#         print("Waduh")
    
#     print(angka)
    
    
# angka = 0 

# while angka < 5 :
#     angka += 1 
#     if angka == 3:
#         pass # Ini tidak akan di eksekusi 
    
#     print(angka)




# Continue --> 

angka = 0 

print(f"angka sekarang --> {angka}")


while angka < 5 : 
    angka += 1 
    print(f"angka sekarang --> {angka}") # aksi 1

    if angka == 3: 
        print("Wadidau")
        continue # akan membuat loop melonjat ke stap selanjutnya
    
    print("WOIEAA") # aksi 2

print("nice")

