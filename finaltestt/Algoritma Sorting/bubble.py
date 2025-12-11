def bubble_sort(data):
    """Mengurutkan data menggunakan Bubble Sort."""
    n = len(data)
    for i in range(n - 1):
        # n-i-1 adalah batas karena i elemen terakhir sudah pasti berada di posisi yang benar
        for j in range(0, n - i - 1):
            # Bandingkan elemen yang berdekatan dan tukar jika urutan salah
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j] # Penukaran

# Contoh Penggunaan
list_a = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(list_a)
print(f"\nBubble Sort: {list_a}") # Output: [11, 12, 22, 25, 34, 64, 90]