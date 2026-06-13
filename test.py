import ghaly079

vektor_x = [0,6,1]
vektor_y = [0,7,9]
X = [[0,6,1],[0,7,9]]
Y = [[0,7,9],[0,6,1]]

print(f"\nVektor X: {vektor_x}")
print(f"Vektor Y: {vektor_y}")
print(f"Matriks X: {X}")
print(f"Matriks Y: {Y}")

print(f"\n1. Penjumlahan vektor x dan y: {ghaly079.penjumlahan_vektor(vektor_x, vektor_y)}")
print(f"2. Pengurangan vektor x dan y: {ghaly079.pengurangan_vektor(vektor_x, vektor_y)}")

print(f"\n3. Nilai L^2 Norm dari vektor y: {ghaly079.l2_norm(vektor_y)}")
print(f"4. Nilai L^1 Norm dari vektor y: {ghaly079.l1_norm(vektor_y)}")
print(f"5. Nilai Squared L^2 Norm dari vektor y: {ghaly079.squared_l2_norm(vektor_y)}")
print(f"6. Nilai Max Norm dari vektor y: {ghaly079.max_norm(vektor_y)}")

print(f"\n7. Apakah vektor y merupakan unit vektor: {ghaly079.cek_unit_vektor(vektor_y)}")
print(f"8. Apakah vektor x dan y orthogonal: {ghaly079.cek_orthogonal(vektor_x, vektor_y)}")
print(f"9. Apakah vektor x dan y orthonormal: {ghaly079.cek_orthonormal(vektor_x, vektor_y)}")
print(f"10. Dot product dari vektor x dan y: {ghaly079.dot_product(vektor_x, vektor_y)}")

print(f"\n11. Penjumlahan matriks X dan Y: {ghaly079.penjumlahan_matriks(X, Y)}")
print(f"12. Pengurangan matriks X dan Y: {ghaly079.pengurangan_matriks(X, Y)}")
print(f"13. Perkalian matriks X dan Y: {ghaly079.perkalian_matriks(X, Y)}")
print(f"14. Hadamard product dari matrix X dan Y: {ghaly079.hadamard_product(X, Y)}")

print(f"\n15. Transpose dari matrix Y: {ghaly079.transpose_matriks(Y)}")
print(f"16. Nilai Frobenius Norm dari matriks Y: {ghaly079.frobenius_norm(Y)}")
print(f"17. Invers dari matriks Y: {ghaly079.matriks_inverse(Y)}")