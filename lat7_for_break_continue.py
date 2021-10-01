""" For Else, Range, Break """

# for loops range
number = 15
for x in range(0,11,3):
    print(x)
else:
    print("halo")

#for loops break
# fungsinya untuk mengakhiri for (terminasi)
number = 5
for x in range(0,7):
    print(x)
    if x == number:
        print('yeaah, angka ditemukan', x)
        break

#loop for continue
# fungsinya untuk melanjutkan ke langkah berikutnya.
for x in range (0,9):
    if x == 6:
        print("nilai ini adalah ", x)
        continue
    print("nilai saat ini adalah ", x)
else:
    print("akhir dari loop")
print("keluar dari loop")