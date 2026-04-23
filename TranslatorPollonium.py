import keyboard
import pyperclip
import time
import random
import tkinter as tk
import re
from threading import Thread
from googletrans import Translator

# BY @Pollonium2112 & @Los4angeles_
# OPTIMIZED GRAMMAR & FULL HISPANIC SLANG

translator = Translator()
active = True

vocabulary = {
    # PEOPLE
    "brother": "carnal", "friend": "homie", "buddy": "ese", "man": "vato",
    "police": "la jura", "cop": "chota", "snitch": "rata", "girl": "chica",
    "woman": "ruca", "parents": "jefes", "boss": "jefe", "gangster": "cholo",
    
    # THINGS & PLACES
    "home": "canton", "house": "crib", "prison": "la pinta", "money": "feria",
    "gun": "cuete", "pistol": "cohete", "car": "ranfla", "neighborhood": "barrio",
    "street": "calle", "work": "chamba", "food": "comida", "beer": "chela",
    
    # ACTIONS & STATUS
    "understand": "comprende", "yes": "simon", "no": "nel", "crazy": "loco",
    "stupid": "pendejo", "cool": "chingon", "true": "no cap", "dangerous": "pesado",
    "weed": "mota", "go": "vamonos", "look": "mira", "stop": "parale"
}

def smart_grammar_fix(text):
    # Perbaikan otomatis untuk susunan kalimat yang sering ngaco
    text = text.lower()
    
    # Fix Nama & Kata Ganti
    text = re.sub(r'\bmy name cave\b', 'my name is', text)
    text = re.sub(r'\bname cave\b', 'name is', text)
    text = re.sub(r'\bi is\b', 'I am', text)
    text = re.sub(r'\bme want\b', 'I want', text)
    text = re.sub(r'\bme no\b', 'I dont', text)
    text = re.sub(r'\byou is\b', 'you are', text)
    text = re.sub(r'\bthey is\b', 'they are', text)
    text = re.sub(r'\bwe is\b', 'we are', text)
    
    # Fix Hilangkan kata 'is/am/are' yang double
    text = re.sub(r'\bam is\b', 'am', text)
    
    # Fix Spasi Tanda Baca
    text = re.sub(r'\s+([?.!,])', r'\1', text) # hapus spasi sebelum tanda baca
    text = re.sub(r'([?.!,])(?=[^\s])', r'\1 ', text) # tambah spasi setelah tanda baca
    
    return text.strip()

def translate_logic():
    global active
    if not active: return
        
    time.sleep(0.15)
    keyboard.press_and_release('ctrl+a')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+x')
    time.sleep(0.1)
    
    raw_input = pyperclip.paste()
    if not raw_input or len(raw_input.strip()) <= 1: return

    try:
        # Step 1: Translate
        res = translator.translate(raw_input, src='id', dest='en').text
        
        # Step 2: Fix Grammar Dasar
        res = smart_grammar_fix(res)
        
        # Step 3: Inject Slang
        words = res.split()
        processed = []
        for w in words:
            clean_w = w.strip(".,!?")
            if clean_w in vocabulary:
                slang = vocabulary[clean_w]
                processed.append(w.replace(clean_w, slang))
            else:
                processed.append(w)

        final = " ".join(processed)
        
        # Step 4: Add Chicano Signature
        endings = [", loco!", ", homes.", ", carnal.", ", ese.", ", comprende?", ", simon."]
        final += random.choice(endings)

        # Final Touch
        pyperclip.copy(final.capitalize())
        time.sleep(0.12)
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.1)
        keyboard.press_and_release('enter')
    except:
        pyperclip.copy(raw_input)
        keyboard.press_and_release('ctrl+v')

def toggle_status():
    global active
    active = not active
    if active:
        btn_toggle.config(text="OFF", bg="#8B0000")
        status_label.config(text="STATUS: ACTIVE", fg="#00ff41")
    else:
        btn_toggle.config(text="ON", bg="#006400")
        status_label.config(text="STATUS: PAUSED", fg="#ffcc00")

def hotkey_thread():
    keyboard.add_hotkey('ctrl+r', translate_logic)
    keyboard.wait()

def start_ui():
    global status_label, btn_toggle
    app = tk.Tk()
    app.title("SAMP Smart Translator")
    app.geometry("350x240")
    app.attributes("-topmost", True)
    app.configure(bg='#121212')

    tk.Label(app, text="AUTO TRANSLATOR", fg="#e0e0e0", bg="#121212", font=("Impact", 20)).pack(pady=10)
    status_label = tk.Label(app, text="STATUS: ACTIVE", fg="#00ff41", bg="#121212", font=("Consolas", 10, "bold"))
    status_label.pack()

    btn_toggle = tk.Button(app, text="OFF", command=toggle_status, bg="#8B0000", fg="white", font=("Arial", 9, "bold"), width=12)
    btn_toggle.pack(pady=15)
    
    tk.Label(app, text="Hotkey: CTRL + R", fg="#888888", bg="#121212", font=("Arial", 8)).pack()
    tk.Label(app, text="Made by @Pollonium2112 & @Los4angeles_ [Discord]", fg="#00ff41", bg="#121212", font=("Arial", 8, "bold")).pack(side="bottom", pady=15)

    Thread(target=hotkey_thread, daemon=True).start()
    app.mainloop()

if __name__ == "__main__":
    start_ui()