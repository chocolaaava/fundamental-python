# Pengkondisian Elif
# digunakan untuk lebih dari 2 kondisi
hari_ini = ("sabtu")
if(hari_ini == "Senin"):
    print("saya kuliah")
elif(hari_ini == "Selasa"):
    print("saya kuliah")
elif(hari_ini == "Rabu"):
    print("saya libur")
elif(hari_ini == "Kamis"):
    print("saya sedang ujian")
else:
    print('Maaf, format hari tidak sesuai')

# contoh kedua
nilai = 70
if nilai == 50:
    print("kamu ga lulus")
elif nilai == 60:
    print("silahkan ikut remedial")
elif nilai == 70:
    print("lumayan bagus")
elif nilai == 80:
    print("bagus")
else:
    print("nilai tidak ditemukan")