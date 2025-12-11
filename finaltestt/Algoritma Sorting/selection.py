def selection_sort(data):
    """Mengurutkan data menggunakan Selection Sort."""
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        # Cari elemen minimum di sisa list (dari i+1 sampai akhir)
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
                
        # Tukar elemen minimum yang ditemukan dengan elemen pada posisi i
        data[i], data[min_idx] = data[min_idx], data[i]

# Contoh Penggunaan
list_b = [64, 25, 12, 22, 11]
selection_sort(list_b)
print(f"Selection Sort: {list_b}") # Output: [11, 12, 22, 25, 64]