class DoubleStack:
    """
    Mengimplementasikan dua Stack (Stack 1 dan Stack 2) 
    menggunakan satu array tunggal (list) di Python.
    """
    def __init__(self, capacity):
        # Inisialisasi array dengan kapasitas yang ditentukan
        self.capacity = capacity
        self.arr = [None] * capacity
        
        # TOP1 dimulai dari -1 (ujung kiri)
        self.top1 = -1
        
        # TOP2 dimulai dari capacity (ujung kanan)
        self.top2 = capacity

    # --- Operasi Stack 1 ---

    def push1(self, item):
        """Menambahkan item ke Stack 1 (tumbuh ke kanan)."""
        # Periksa kondisi Stack Penuh
        # Stack Penuh jika top1 bertemu top2
        if self.top1 + 1 == self.top2:
            print("❌ Stack 1 Overflow (Stack Penuh)")
            return
        
        self.top1 += 1
        self.arr[self.top1] = item
        print(f"✅ Pushed {item} ke Stack 1")

    def pop1(self):
        """Menghapus dan mengembalikan item dari Stack 1."""
        # Periksa kondisi Stack Kosong
        if self.top1 == -1:
            print("❌ Stack 1 Underflow (Stack Kosong)")
            return None
        
        item = self.arr[self.top1]
        self.arr[self.top1] = None # Opsional: Membersihkan slot
        self.top1 -= 1
        return item
    
    # --- Operasi Stack 2 ---

    def push2(self, item):
        """Menambahkan item ke Stack 2 (tumbuh ke kiri)."""
        # Periksa kondisi Stack Penuh
        if self.top1 + 1 == self.top2:
            print("❌ Stack 2 Overflow (Stack Penuh)")
            return
        
        self.top2 -= 1
        self.arr[self.top2] = item
        print(f"✅ Pushed {item} ke Stack 2")

    def pop2(self):
        """Menghapus dan mengembalikan item dari Stack 2."""
        # Periksa kondisi Stack Kosong
        if self.top2 == self.capacity:
            print("❌ Stack 2 Underflow (Stack Kosong)")
            return None
        
        item = self.arr[self.top2]
        self.arr[self.top2] = None # Opsional: Membersihkan slot
        self.top2 += 1
        return item

    # --- Status ---
    def display_array(self):
        print(f"\n--- Status Array Bersama (Kapasitas {self.capacity}) ---")
        print(f"Array: {self.arr}")
        print(f"TOP 1 Index: {self.top1} | TOP 2 Index: {self.top2}")
        print("-----------------------------------------------------")


# --- Contoh Penggunaan ---

# Inisialisasi Double Stack dengan kapasitas 10
ds = DoubleStack(10)

ds.display_array()

# Operasi pada Stack 1
print("\n[Operasi Stack 1]")
ds.push1(10)
ds.push1(20)
ds.push1(30)
ds.display_array()

# Operasi pada Stack 2
print("\n[Operasi Stack 2]")
ds.push2('A')
ds.push2('B')
ds.push2('C')
ds.display_array()

# Pengujian Full/Overflow (Memaksimalkan kapasitas)
ds.push1(40)
ds.push1(50)
ds.push2('D')
ds.push2('E') # Array Penuh
ds.push2('F') # Akan gagal (Overflow)

ds.display_array()

# Operasi POP
print("\n[Operasi POP]")
print(f"Pop Stack 1: {ds.pop1()}") # Output: E
print(f"Pop Stack 2: {ds.pop2()}") # Output: F

ds.display_array()