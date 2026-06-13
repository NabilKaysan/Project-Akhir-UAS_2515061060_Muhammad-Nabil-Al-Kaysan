import Nabil060 as n

A = [[1, 2, 4],
     [3, 4, 5],
     [6, 7, 8]]
B = [[2,5, 1],
     [5,0, 6],
     [1, 0, 6]]

print("Penjumlahan:")
print(n.tambah_matriks(A, B))

print("Pengurangan:")
print(n.kurang_matriks(A, B))

print("Perkalian:")
print(n.kali_matriks(A, B))

print("Transpose A:")
print(n.transpose_matriks(A))