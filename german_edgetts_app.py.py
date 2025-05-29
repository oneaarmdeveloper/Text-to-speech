import asyncio
import edge_tts
import tkinter as tk
from tkinter import messagebox

# Async function to generate and save TTS output
async def generate_speech(text, filename="ausgabe.mp3", voice="de-DE-KatjaNeural"):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(filename)
        messagebox.showinfo("Fertig!", f"Gespeichert als: {filename}")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

# Tkinter GUI setup
def start_app():
    def on_generate():
        user_text = input_box.get("1.0", tk.END).strip()
        if user_text:
            asyncio.run(generate_speech(user_text))
        else:
            messagebox.showwarning("Fehler", "Bitte gib einen Text ein.")

    root = tk.Tk()
    root.title("German TTS App")
    root.geometry("400x250")
    root.resizable(False, False)

    tk.Label(root, text="Gib deutschen Text ein:").pack(pady=5)
    input_box = tk.Text(root, height=6, width=45)
    input_box.pack()

    tk.Button(root, text="MP3 erstellen", command=on_generate).pack(pady=10)
    root.mainloop()

# Run the app
start_app()
