# Menghitung luas permukaan dan volume prisma segitiga
# dibuat oleh fauzan ramadhan

# Panjang alas segitiga, tinggi segitiga, dan tinggi prisma
alas_segitiga = 9
tinggi_segitiga = 7
tinggi_prisma = 13

# Menghitung luas permukaan prisma segitiga
luas_permukaan = (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)

# Menghitung volume prisma segitiga
volume = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma

# Menampilkan hasil
print("Luas Permukaan Prisma Segitiga: ", luas_permukaan)
print("Volume Prisma Segitiga: ", volume)
