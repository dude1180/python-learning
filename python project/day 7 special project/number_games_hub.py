import random

def tebakangka():
    angkabenar = random.randint(1,100)
    percobaan = 1
    while True:
        try:
            tebakan = int(input(f"""-- Tebak Angka --
percobaan {percobaan}/10
tebak angka 1-100:"""))
            if percobaan == 10 and tebakan != angkabenar:
                    print(f"u lost, angkanya: {angkabenar}")
                    print("kembali ke menu...")
                    break
            if tebakan < 1 or tebakan > 100:
                    print(f"1-100 doang apalah")
                    continue
            
            percobaan += 1
            if tebakan < angkabenar:
                print(f"kurang besar")
            elif tebakan > angkabenar:
                print(f"terlalu besar")
            else:
                print(f"benar!, anda menebak sebanyak {percobaan}x")
                print("kembali ke menu...")
                break
        except ValueError:
            print("tebak angka woy lah")

def math_challenge():
    skor = 0
    soal = 5
    for i in range(1, soal + 1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        if operator == "+":
            jawabanbenar = a + b
        elif operator == "-":
            jawabanbenar = a - b
        else:
            jawabanbenar = a * b
        while True:
            jawaban = input(f"""soal ke {i}
skor:{skor}
{a} {operator} {b} =""")
            if not jawaban.isdigit():
                print("angka doang apalah")
                continue
            else:
                jawaban = int(jawaban)
                break

        if jawaban == jawabanbenar:
            skor += 1
            print("benar!")
        else:
            print(f"salah!, jawaban yg bnr:{jawabanbenar}")
    print(f"game selesai, skor: {skor}")
    print("kembali ke menu...")
        

while True:

    menu = input(""" === MENU ===
1. Tebak Angka
2. Math Challenge
3. Keluar 
Pilih menu:""")
    if menu == "1":
        tebakangka()
    elif menu == "2":
        math_challenge()
    elif menu == "3":
        print("aight, bye")
        break
    else:
        print("pilihan hanya 1-3")


                
                





   