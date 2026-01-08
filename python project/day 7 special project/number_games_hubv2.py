import random

stats = {
    "tebak_main": 0,
    "math_main": 0,
    "high_score": 0,
    "last_score": 0
}

def liat_stats():
    print(f"=== STATISTICS ===")
    print(f"kamu memainkan tebak angka sebanyak {stats['tebak_main']}x")
    print(f"kamu memainkan math challenge sebanyak {stats['math_main']}x")
    print(f"score terakhir mu adalah {stats['last_score']}")
    print(f"score tertinggi mu adalah {stats['high_score']}")
    while True:
        statexit = input("keluar? [Y]").upper()
        if statexit == "Y":
            print("kembali ke menu...")
            break

def tebakangka():
    angkabenar = random.randint(1,100)
    percobaan = 1
    while True:
        try:
            tebakan = int(input(f"""-- Tebak Angka --
percobaan {percobaan}/10
tebak angka 1-100:{angkabenar}"""))
            if percobaan == 10 and tebakan != angkabenar:
                    print(f"u lost, angkanya: {angkabenar}")
                    print("kembali ke menu...")
                    return 0
                
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
                return 1
                
        except ValueError:
            print("tebak angka woy lah")

def math_challenge():
    skor = 0
    soal = 10
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
            try:
                jawaban = int(jawaban)
                break
            except ValueError:
                print("angka doang apalah")


        if jawaban == jawabanbenar:
            skor += 1
            print("benar!")
        else:
            print(f"salah!, jawaban yg bnr:{jawabanbenar}")
    print(f"game selesai, skor: {skor}")
    print("kembali ke menu...")
    return skor
        

while True:

    menu = input(""" === MENU ===
1. Tebak Angka
2. Math Challenge
3. Liat Stats 
4. Keluar
Pilih menu:""")
    if menu == "1":
        stats["tebak_main"] += 1
        hasil = tebakangka()
        stats["last_score"] = hasil
        
    elif menu == "2":
        stats["math_main"] += 1
        score = math_challenge()
        stats["last_score"] = score
        if score > stats["high_score"]:
            stats["high_score"] = score
        
    elif menu == "3":
        liat_stats()
    elif menu == "4":
        print("aight bye")
        break
    else:
        print("pilihan hanya 1-4")


                
                





   