# Implementasi Single Stack
stack = []

# Operasi PUSH (Menambahkan elemen)
stack.append("Data A")
stack.append("Data B")
stack.append("Data C")
print(f"\nStack setelah PUSH: {stack}") # Output: ['Data A', 'Data B', 'Data C']

# Operasi POP (Menghapus dan mengembalikan elemen teratas)
elemen_pop = stack.pop()
print(f"Elemen POP: {elemen_pop}") # Output: Data C
print(f"Stack setelah POP: {stack}") # Output: ['Data A', 'Data B']

# Melihat elemen teratas (PEEK)
if stack:
    print(f"Elemen PEEK (teratas): {stack[-1]}") # Output: Data B