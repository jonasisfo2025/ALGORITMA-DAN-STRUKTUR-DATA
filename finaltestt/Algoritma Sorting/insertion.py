def insertion_sort(data):
    """Mengurutkan data menggunakan Insertion Sort."""
    # Mulai dari elemen kedua (indeks 1)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # Pindahkan elemen data[0..i-1] yang lebih besar dari key
        # ke satu posisi di depan posisi saat ini
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = key

# Contoh Penggunaan
list_c = [12, 11, 13, 5, 6]
insertion_sort(list_c)
print(f"Insertion Sort: {list_c}") # Output: [5, 6, 11, 12, 13]