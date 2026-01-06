import random

skor = 0
total_soal = 5

def game_start():
    global skor, total_soal

    for i in range(1, total_soal + 1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
            
        if operator == "+":
            jawaban_benar = a + b
        
        elif operator == "-":
            jawaban_benar = a - b

        else:
            jawaban_benar = a * b

        jawaban = input(f"soal ke {i}: {a} {operator} {b}=")

        try:
            if int(jawaban) == jawaban_benar:
                skor += 1
                print(f"jawaban benar!, skor:{skor}")
            else:
                print(f"jawaban salah! yg bnr {jawaban_benar}, skor:{skor}")
        except ValueError:
            print("hanya angka")

game_start()

