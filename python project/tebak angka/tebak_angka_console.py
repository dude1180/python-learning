import random
    
def maingame(max_attempt):
    angkabenar = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input(f"tebak angka 1-100:"))

            if tebakan < 1 or tebakan > 100:
                print(f"di bilang 1-100 apalah. percobaan ke {percobaan}/{max_attempt}")
                continue
            percobaan += 1

            if percobaan == max_attempt and tebakan != angkabenar:
                print(F"U LOST THE NUMBER IS {angkabenar}")
                break
            if tebakan < angkabenar:
                print(f"terlalu kecil. percobaan ke {percobaan}/{max_attempt}")
            elif tebakan > angkabenar:
                print(f"terlalu besar. percobaan ke {percobaan}/{max_attempt}")
            else:
                print(f"wow benar, kamu menebak sebanyak {percobaan}x")
                break
                
        except ValueError:
            print(f"di bilang tebak angka apalah, percobaan ke {percobaan}/{max_attempt}")

def select_gamemode():
    while True:
            gamemode = input("pilih gamemode: easy/normal/hard?").lower()
            if gamemode == "easy":
                maingame(15)
                break
            elif gamemode == "normal":
                maingame(10)
                break
            elif gamemode == "hard":
                maingame(5)
                break
            else:
                print("di bilang easy/normal/hard doang apalah")

while True:
    select_gamemode()
    while True:

        jawaban = input("try again? [y/n]").lower()

        if jawaban == "y":
            break
        elif jawaban == "n":
            print("aight, bye")
            exit()
        else:
            print("y/n doang apalah")
    
            
            










