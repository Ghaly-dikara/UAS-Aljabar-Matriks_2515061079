def penjumlahan_vektor(a, b):
    return [x + y for x, y in zip(a, b)]

def pengurangan_vektor(a, b):
    return [x - y for x, y in zip(a, b)]

def l2_norm(a):
    return sum(x**2 for x in a) ** 0.5
    '''Menghitung panjang suatu vektor'''

def l1_norm(a):
    return sum(abs(x) for x in a)
    '''jumlah seluruh elemen absolut dari suatu vektor'''

def squared_l2_norm(a):
    return sum(x**2 for x in a)
    '''jumlah seluruh elemen yang dikuardratkan'''

def max_norm(a):
    return max(abs(x) for x in a)
    '''mencari elemen dengan nilai tertinggi dalam suatu vektor'''

def cek_unit_vektor(a):
    panjang = l2_norm(a)
    return abs(panjang - 1.0) <= 1e-9
    '''Mengecek apakah suatu vektor merupakan unit vektor (yaitu vektor yang panjangnya sama dengan satu)'''

def cek_orthogonal(a, b):
    return dot_product(a, b) == 0
    '''
    Mengecek apakah suatu vektor orthogonal atau tidak.
    Syarat vektor orthogonal adalah hasil dot product sama dengan 0
    '''

def cek_orthonormal(a, b):
    return cek_orthogonal(a, b) and cek_unit_vektor(a) and cek_unit_vektor(b)
    '''
    Mengecek apakah suatu vektor orthonormal atau tidak.
    Syarat dari vektor orthonormal:
    1. Orthogonal (Saling tegak lurus), hasil dot product sama dengan 0
    2. Vektor-vektornya merupakan unit vector, panjang nya sama dengan 1
    '''

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))
    '''Jumlah dari hasil perkalian masing masing elemen vektor yang posisinya sama'''

def penjumlahan_matriks(A, B):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def pengurangan_matriks(A, B):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

def hadamard_product(A, B):
    return [[x * y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]
    '''Perkalian matriks menggunakan hadamard product'''

def perkalian_matriks(A, B):
    '''Perkalian titik matriks standar (dot product matriks)'''
    # Syarat: Jumlah kolom matriks A harus sama dengan jumlah baris matriks B
    if len(A[0]) != len(B):
        return "Error, Dimensi matriks tidak sesuai. Kolom A harus sama dengan Baris B."
    
    # Membuat kerangka matriks hasil berisi angka 0 
    # Ukurannya: (jumlah baris A) x (jumlah kolom B)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Melakukan perhitungan perkalian baris kali kolom
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def transpose_matriks(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    '''Mengubah baris matriks menjadi kolom dan kolom matriks menjadi baris'''

def frobenius_norm(A):
    return sum(x**2 for row in A for x in row) ** 0.5
    '''
    Mengukur ukuran matrix jika semua elemen matriks dianggap satu vektor panjang 
    (mengukur seberapa "panjang" vektor tersebut dari titik nol)
    '''

def determinan(A):
    '''Menghitung determinan dengan metode kofaktor rekursif'''
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    det = 0
    for c in range(n):
        sub_matrix = [row[:c] + row[c+1:] for row in A[1:]]
        det += ((-1)**c) * A[0][c] * determinan(sub_matrix)
    return det

def adjoint(A):
    '''Menghitung matriks kofaktor lalu di-transpose'''
    n = len(A)
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            sub_matrix = [row[:c] + row[c+1:] for i, row in enumerate(A) if i != r]
            cofactor_row.append(((-1)**(r+c)) * determinan(sub_matrix))
        cofactors.append(cofactor_row)
    return transpose_matriks(cofactors)

def matriks_inverse(A):
    '''Menghitung invers dari suatu matriks menggunakan rumus (1/determinan matriks) * adjoint matriks'''
    if len(A) != len(A[0]):
        return "Error: Invers tidak bisa dihitung karena matriks bukan matriks persegi."
    
    det = determinan(A)
    if det == 0:
        return "Error: Determinan 0, matriks singular dan tidak memiliki invers."
        
    adj = adjoint(A)
    # Perkalian skalar (1/det) dengan matriks adjoint
    return [[x / det for x in row] for row in adj]