# Menghitung luas permukaan dan volume limas segitiga
# dibuat oleh fauzan ramadhan

# Panjang alas, tinggi limas, dan tinggi segitiga
alas = 10
tinggi_limas = 18
tinggi_segitiga = 14

# Menghitung luas permukaan limas segitiga
luas_permukaan = (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)

# Menghitung volume limas segitiga
volume = (alas ** 2 * tinggi_segitiga) / 6

# Menampilkan hasil
print("Luas Permukaan Limas Segitiga: ", luas_permukaan)
print("Volume Limas Segitiga: ", volume)
