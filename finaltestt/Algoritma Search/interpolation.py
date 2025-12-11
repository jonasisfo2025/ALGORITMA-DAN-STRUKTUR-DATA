def interpolation_search(data, target):
    """Mencari target dalam data yang diurutkan dan terdistribusi seragam."""
    low = 0
    high = len(data) - 1

    while low <= high and target >= data[low] and target <= data[high]:
        # Rumus Interpolasi untuk menentukan posisi
        # Menggunakan estimasi berdasarkan nilai, bukan selalu di tengah
        try:
            pos = low + ((high - low) // (data[high] - data[low])) * (target - data[low])
        except ZeroDivisionError:
            # Menghindari pembagian oleh nol jika high == low dan data[high] == data[low]
            pos = low

        if data[pos] == target:
            return pos
        
        if data[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1

# Contoh Penggunaan (Data terurut dan relatif seragam)
angka_interp = [10, 20, 30, 40, 50, 60, 70, 80]
target_3 = 50

print(f"Interpolation Search 50: Indeks {interpolation_search(angka_interp, target_3)}") # Output: Indeks 4