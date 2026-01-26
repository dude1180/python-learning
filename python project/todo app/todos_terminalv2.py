import json
from datetime import datetime
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

def sorting_tanggal():
    def ambil_deadline(item):
        deadline = item.get("deadline", "-")
        if deadline == "-":
            return datetime.strptime("31-12-9999", "%d-%m-%Y")
        return datetime.strptime(deadline, "%d-%m-%Y")
    tugas_list.sort(key=ambil_deadline)
    save_data()

def liat_stats():
    totals = len(tugas_list)
    selesai = sum(1 for item in tugas_list if item["done"])
    pending = totals - selesai

    print(f"""====================
STATS
total tugas:{totals}
✔:{selesai}
✖:{pending} 
====================""")
    
def new_id_generator():
    if not tugas_list:
        return 1
    return max(item["id"] for item in tugas_list) + 1

def validasi_tanggal(pesan):
    while True:
        input_tanggal = input(pesan)
        if not input_tanggal or input_tanggal == "-":
            return "-"
        try:
            datetime.strptime(input_tanggal, "%d-%m-%Y")
            return input_tanggal
        except ValueError:
            print("tanggal tidak valid, pake format dd-mm-yyyy atau kosongkan!")
 

def cari_tugas():
    if not tugas_list:
        print("blm ada tugas, gada yg bisa di cari")
        return
    key_word = input("cari tugas apa?").lower()
    print(f"hasil pencarian untuk '{key_word}':")
    hasil_pencarian = 0
    for item in tugas_list:
        if key_word in item["task"].lower():
            status = "[✔]" if item["done"] else "[✖]"
            print(f"{item['id']}. {status} {item['task']} | deadline: {item.get('deadline', '-')}")
            hasil_pencarian += 1
    print(f"menemukan:{hasil_pencarian} hasil yang cocok")
    if hasil_pencarian == 0:
        print("tugas tidak ada")

def liat_list():
    sorting_tanggal()
    liat_stats()
    print("DAFTAR TUGAS:")
    if not tugas_list:
        print("belum ada tugas")
    else:
        for item in tugas_list:
            status = "[✔]" if item["done"] else "[✖]"
            print(f"{item['id']}. {status} {item['task']} | deadline: {item.get('deadline', '-')}")

def tambah_tugas():
    task = input("ketik tugasnya:")
    deadline = validasi_tanggal("masukan deadline (dd-mm-yyyy) atau kosongkan:")
    new_id = new_id_generator()
    tugas_baru = {
        "id" : new_id,
        "task" : task,
        "done" : False,
        "deadline": deadline
    }
    tugas_list.append(tugas_baru)
    save_data()
    print(f"berhasil di tambahkan dengan id:{new_id}")

def selesaikan_tugas():
    if not tugas_list:
        print("list kosong, gada yg bisa di selesaiin")
        return
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

def hapus_tugas():
    if not tugas_list:
        print("list kosong, gada yg bisa di hapus")
        return
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

def edit_tugas():
    if not tugas_list:
        print("belum ada tugas!")
        return
    try:
        update_num = int(input("masukan id tugas yg mau di edit:"))
        found = False
        for item in tugas_list:
            if item["id"] == update_num:
                print(f"tugas lama:{item['task']}")
                edit_nama_tugas = input("edit tugas ke (kosongkan jika tidak ingin ganti):")
                if edit_nama_tugas:
                    item["task"] = edit_nama_tugas
                print(f"deadline lama:{item.get('deadline', '-')}")
                edit_deadline = validasi_tanggal("edit deadline (dd-mm-yyyy) / kosongkan jika tidak ingin ganti:")
                if edit_deadline != "-":
                    item["deadline"] = edit_deadline
                    
                save_data()
                print("tugas berhasil di edit!")
                found = True
                break
        if not found:
            print("id tidak ada!")
    except ValueError:
        print("masukan id berupa angka!")

load_data()

while True:
    print("""TO-DO LIST
1.liat list
2.tambah tugas
3.selesaikan tugas
4.hapus tugas
5.edit tugas
6.cari tugas
7.keluar""")
    try:
        pilihan = int(input("pilih [1-7?]:"))
        if pilihan == 1:
            liat_list()
        elif pilihan == 2:
            tambah_tugas()
        elif pilihan == 3:
            selesaikan_tugas()
        elif pilihan == 4:
            hapus_tugas()
        elif pilihan == 5:
            edit_tugas()
        elif pilihan == 6:
            cari_tugas()

        elif pilihan == 7:
            print("ok, bye")
            break
        else:
            print("1-7 doang apalah")
    except ValueError:
         print("masukan angka!")

        
                
            
