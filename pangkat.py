def perkalian(bil1,bil2):
    if bil2==1:
        print("%d = " %(bil1),end='')
        return bil1
    else: 
        print("%d + " %(bil1),end='')
        return bil1 * perkalian(bil1,bil2-1)
print(perkalian(2,4))