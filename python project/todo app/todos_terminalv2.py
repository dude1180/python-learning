import json
file_data = "todos_datas.json"
tugas_list = []
def save_data():
    with open(file_data, "w") as f:
        json.dump(tugas_list, f, indent=4)
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
3.selesaikan tugas
4.hapus tugas
5.edit tugas
6.keluar""")
    try:
        pilihan = int(input("pilih [1-6?]:"))
        if pilihan == 1:
            print("DAFTAR TUGAS:")
            if not tugas_list:
                print("belum ada tugas")
            else:
                for item in tugas_list:
                    status = "[✓]" if item["done"] else "[]"
                    print(f"{item['id']}. {status} {item['task']}")
        elif pilihan == 2:
            task = input("ketik tugasnya:")
            new_id = tugas_list[-1]["id"] + 1 if tugas_list else 1
            tugas_baru = {
                "id": new_id,
                "task": task,
                "done": False
            }
            tugas_list.append(tugas_baru)
            save_data()
            print(f"berhasil di tambahkan dengan id:{new_id}")
        elif pilihan == 3:
            if not tugas_list:
                print("list kosong, gada yg bisa di selesaiin")
                continue
            try:
                target = int(input("masukan id tugas yg udh selesai:"))
                found = False
                for item in tugas_list:
                    if item["id"] == target:
                        item["done"] = True
                        found = True
                        save_data()
                        print(f"tugas {target} sudah selesai!")
                        break
                if not found:
                    print("id tidak ada.")
            except ValueError:
                print("id berupa angka!!")

        elif pilihan == 4:
            if not tugas_list:
                print("list kosong, gada yg bisa di hapus")
                continue
            try:
                nomor = int(input("nomor brp yg mau di hapus?:"))
                found = False
                for item in tugas_list:
                    if item["id"] == nomor:
                        tugas_list.remove(item)
                        found = True
                        save_data()
                        print(f"tugas {nomor} di hapus")
                        break
                if not found:
                    print("tugas tidak ada di list!")
            except ValueError:
                print("masukan angka doang apalah!")
        elif pilihan == 5:
            if not tugas_list:
                print("belum ada tugas!")
                continue
            try:
                update_num = int(input("masukan id tugas yg mau di edit:"))
                found = False
                for item in tugas_list:
                    if item["id"] == update_num:
                        print(f"tugas lama:{item['task']}")
                        edit_tugas = input("edit ke (kosongkan jika batal):")
                        if edit_tugas:
                            item["task"] = edit_tugas
                            save_data()
                            print("tugas berhasil di edit!")
                        found = True
                if not found:
                    print("id tidak ada!")
            except ValueError:
                print("masukan id berupa angka!")

        elif pilihan == 6:
            print("ok, bye")
            break
        else:
            print("1-6 doang apalah")
    except ValueError:
         print("masukan angka!")

        
                
            
