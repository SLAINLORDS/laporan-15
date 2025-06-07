def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
kalimat = input("Masukkan kalimat: ")
if is_palindrome(kalimat):
    print("Kalimat tersebut adalah palindrom.")
else:
    print("Kalimat tersebut bukan palindrom.")