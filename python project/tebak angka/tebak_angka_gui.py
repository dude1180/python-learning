import tkinter as tk
import random

base = tk.Tk()
base.title("Tebak angka!")
base.geometry("300x300")

percobaan = 0
angkabenar = random.randint(1, 100)
kesulitan = "normal"
max_attempt = 10

pertanyaan = tk.Label(base, text=f"tebak angka 1-100!")
pertanyaan.pack(pady=5)

level = tk.Label(base, text=f"difficulty:{kesulitan}")
level.pack(pady=3)

nyawa = tk.Label(base, text=f"percobaan ke {percobaan}/{max_attempt}" )
nyawa.pack(anchor="w", padx=5, pady=3)

entry = tk.Entry(base)
entry.pack(pady=10)

def pilih_difficulty(mode):
    global kesulitan, max_attempt, angkabenar, percobaan
    kesulitan = mode
    if mode == "easy":
        max_attempt = 15
    elif mode == "normal":
        max_attempt = 10
    elif mode == "hard":
        max_attempt = 5
    percobaan = 0
    angkabenar = random.randint(1, 100)
    level.config(text=f"difficulty: {kesulitan}")
    nyawa.config(text=f"percobaan ke {percobaan}/{max_attempt}")
    pertanyaan.config(text=f"tebak angka 1-100!")
    button.config(state="normal")
    entry.delete(0, tk.END)

def cek_angka():
    global percobaan
    try:
        tebakan = int(entry.get())

        if tebakan > 100 or tebakan < 1:
            pertanyaan.config(text="di bilang 1 - 100 apalah")
            entry.delete(0, tk.END)
            return
        percobaan += 1
        if percobaan == 1:
            for btn in difficulty_button:
                btn.config(state="disabled")

        nyawa.config(text=f"percobaan ke {percobaan}/{max_attempt}")

        if percobaan == max_attempt and tebakan != angkabenar:
            pertanyaan.config(text=f"U LOST LOL angkanya adalah {angkabenar}")
            button.config(state="disabled")
            entry.delete(0, tk.END)
            return
        if tebakan > angkabenar:
            pertanyaan.config(text="terlalu besar")
            
            nyawa.config(text=f"percobaan ke {percobaan}/{max_attempt}")
            entry.delete(0, tk.END)
        elif tebakan < angkabenar:
            pertanyaan.config(text="terlalu kecil")
            
            nyawa.config(text=f"percobaan ke {percobaan}/{max_attempt}")
            entry.delete(0, tk.END)
        else:
            
            nyawa.config(text=f"percobaan ke {percobaan}/{max_attempt}")
            pertanyaan.config(text=f"benar! kamu menebak sebanyak {percobaan} kali")
            button.config(state="disabled")
            entry.delete(0, tk.END)
    except ValueError:
        pertanyaan.config(text="dibilang pilih angka apalah")
        entry.delete(0, tk.END)

def try_again():
    pilih_difficulty(kesulitan)
    for btn in difficulty_button:
        btn.config(state="normal")

difficulty_button = []
btn_frame = tk.Frame(base)
btn_frame.pack(pady=4)
for mode in ["easy", "normal", "hard"]:
    btn = tk.Button(btn_frame, text=mode, width=6, command=lambda m=mode: pilih_difficulty(m))
    btn.pack(side="left", padx=2)
    difficulty_button.append(btn)


tryagain = tk.Button(base, text="try again", command=try_again)
tryagain.pack(pady=10)


button = tk.Button(base, text="submit", command=cek_angka)
button.pack(pady=10)

base.mainloop()