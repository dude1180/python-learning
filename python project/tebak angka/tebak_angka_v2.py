import random

def game_start():
    percobaan = 0
    angka_benar = random.randint(1, 50)
    while True:
        try:
            tebakan = input("tebak angka 1-50:")
            tebakan = int(tebakan)

            if tebakan < 1 or tebakan > 50:
                print("pilih angka 1-50!!")
                continue

            percobaan += 1
            if tebakan < angka_benar:
                print("angka terlalu kecil")
            elif tebakan > angka_benar:
                print("angka terlalu besar")
            else:
                print(f"angka benar!, anda mencoba {percobaan}x")
                break
        except ValueError:
            print("masukan angka!!")

while True:
    game_start()
    while True:
        ulang = input("main lagi? [Y/N]").upper()
        if ulang == "Y":
            break
        elif ulang == "N":
            print("aight, bye")
            break
        else:
            print("Y/N doang apalah")
    if ulang == "N":
        break