class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.count = 0

    def push(self, data):
        if self.is_full():
            print("Stack sudah penuh!")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.top is None:
            print("Stack kosong, tidak bisa menghapus!")
            return
        removed = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Elemen {removed} telah dihapus.")

    def size(self):
        print(f"Ukuran stack saat ini: {self.count}")

    def peek(self):
        if self.top is None:
            print("Stack kosong.")
        else:
            print(f"Puncak stack saat ini: {self.top.data}")

    def is_full(self):
        return self.count == self.capacity

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Stack:", items[::-1])  # Ditampilkan dari bawah ke atas

# ===== PROGRAM UTAMA =====
def main():
    print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
    kapasitas = int(input("Tentukan berapa kapasitas stack : "))
    stack = StackLinkedList(kapasitas)

    while True:
        print("\nPilih menu berikut ini :")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan anda : ")

        if pilihan == '1':
            while not stack.is_full():
                data = input("Masukkan isi stack : ")
                stack.push(data)
                stack.display()
                if stack.is_full():
                    print("Stack sudah penuh.")
                    break
                lanjut = input("Menambah isi Stack Pilih [Ya/Tidak] : ").lower()
                if lanjut != 'ya':
                    break
        elif pilihan == '2':
            stack.pop()
            stack.display()
        elif pilihan == '3':
            stack.size()
        elif pilihan == '4':
            stack.peek()
        elif pilihan == '5':
            if stack.is_full():
                print("Stack dalam kondisi penuh.")
            else:
                print("Stack masih tersedia.")
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
