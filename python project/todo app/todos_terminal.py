import json
file_data = "todos_data.json"
tugas_list = []
def save_data():
    with open(file_data, "w") as f:
        json.dump(tugas_list, f)
def load_data():
    global tugas_list
    try:
        with open(file_data, "r") as f:
            tugas_list = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        tugas_list = []

load_data()

while True:
    print("""TO-DO LIST
1.liat list
2.tambah tugas
3.hapus tugas
4.keluar""")
    try:
        pilihan = int(input("pilih [1/2/3/4?]:"))
        if pilihan == 1:
            print("DAFTAR TUGAS:")
            if len(tugas_list) == 0:
                print("belum ada tugas")
            else:
                for i, task in enumerate(tugas_list, 1):
                    print(f"{i}.{task}")
        elif pilihan == 2:
            task = input("ketik tugas:")
            tugas_list.append(task)
            save_data()
            print("berhasil di tambahkan")
        elif pilihan == 3:
            if len(tugas_list) == 0:
                print("list kosong, gada yg bisa di hapus")
            else:
                try:
                    nomor = int(input("nomor brp yg udah selesai/mau di hapus?:"))
                    if 1 <= nomor <= len(tugas_list):
                        tugas_list.pop(nomor - 1)
                        save_data()
                        print("tugas di hapus")
                    else:
                        print("tugas tidak ada di list!")
                except ValueError:
                    print("masukan angka doang apalah!")
        elif pilihan == 4:
            print("ok, bye")
            break
        else:
            print("1-4 doang apalah")
    except ValueError:
         print("masukan angka!")

        
                
            
