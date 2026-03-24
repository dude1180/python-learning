import random
pilihan = ["batu", "gunting", "kertas"]
logic = {
    "batu": "gunting",
    "gunting": "kertas",
    "kertas": "batu"
}
skor_player = 0
skor_bot = 0
while skor_player < 5 and skor_bot < 5:
    player = input("pilih batu, gunting, atau kertas: ").lower()
    if player not in pilihan:
        print("pilihan tidak valid, coba lagi.")
        continue
    bot = random.choice(pilihan)
    print(f"bot memilih: {bot}")

    if player == bot:
        print("seri!")
    elif logic[player] == bot:
        print("kamu menang!")
        skor_player += 1
    else:
        print("bot menang!")
        skor_bot += 1
    print(f"skor kamu: {skor_player}, skor bot: {skor_bot}")

if skor_player == 5:
    print("selamat, kamu menang!")
else:
    print("kamu kalah!")
