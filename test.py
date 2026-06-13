import ghaly079

skalar_x = 61
skalar_y = 79
vektor_x = [0,6,1]
vektor_y = [0,7,9]
X = [[0,6,1],[0,7,9]]
Y = [[0,7,9],[0,6,1]]

jumlah_vektor = (ghaly079.penjumlahan_vektor(vektor_x, vektor_y))
pengurangan_vektor = (ghaly079.pengurangan_vektor(vektor_x, vektor_y))

print(f"Penjumlahan vektor: {jumlah_vektor}")
print(f"Pengurangan vektor: {pengurangan_vektor}")