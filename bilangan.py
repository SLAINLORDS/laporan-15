def digits(s):
    if not s:
        return 0
    first_char = s[0]
    if first_char.isdigit():
        return int(first_char) + digits(s[1:]) 
    return digits(s[1:]) 

# Contoh penggunaan
kalimat = input("Masukkan kalimat: ")
print(f"Jumlah digit dalam kalimat '{kalimat}' adalah {digits(kalimat)}")
