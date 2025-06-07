def is_prime(n, bagi=None):
    if n < 2:
        return False
    if bagi is None:
        bagi = n - 1
    if bagi == 1:
        return True
    if n % bagi == 0:
        return False
    return is_prime(n, bagi - 1)


bilangan = int(input("Masukkan bilangan: "))
if is_prime(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")