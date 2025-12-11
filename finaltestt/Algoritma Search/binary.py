def binary_search(data, target):
    """Mencari target dalam data yang diurutkan menggunakan Binary Search."""
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if data[mid] == target:
            return mid  # Target ditemukan
        elif data[mid] < target:
            low = mid + 1 # Cari di setengah kanan
        else:
            high = mid - 1 # Cari di setengah kiri
            
    return -1 # Target tidak ditemukan

# Contoh Penggunaan
angka_terurut = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_1 = 23
target_2 = 50

print(f"\nArray Data: {angka_terurut}")
hasil_1 = binary_search(angka_terurut, target_1)
print(f"Binary Search 23: Indeks {hasil_1}") # Output: Indeks 5

hasil_2 = binary_search(angka_terurut, target_2)
print(f"Binary Search 50: Indeks {hasil_2}") # Output: Indeks -1 (Tidak ditemukan)