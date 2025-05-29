## Text-to-speech
This project contains two simple python scripts that convert a German text to spoken German in mp3 format

You can choose between:
- A **command-line app** using Google's `gTTS`
- A **desktop GUI app** using Microsoft Edge's high-quality neural voices via `edge-tts`

---

##  Project Contents

| File                | Description                                 |
|---------------------|---------------------------------------------|
| `gtts_simple.py`    | Command-line version using Google TTS       |
| `edge_tts_gui.py`   | GUI app using Edge neural voices (Katja)    |
| `requirements.txt`  | Python dependencies                         |
| `README.md`     
| 'test.py '          |   Testing if edge-tts works correctly       |

---

## ▶ Option 1: `gtts_simple.py`

A minimal command-line script that takes German text input and creates an MP3 file using Google's `gTTS`.

###  Features

- Input via terminal
- Converts instantly to MP3
- Lightweight and easy to use

###  How It Works

1. Reads text from `input()`
2. Calls `gTTS(text, lang="de")`
3. Saves the audio as `ausgabe.mp3`

### ⚙ Requirements

- Python 3.8+
- `gTTS`

###  Setup & Run

```bash
pip install gtts
python gtts_simple.py

Option 2: edge_tts_gui.py
A desktop GUI app that lets you paste German text and create natural-sounding speech using Edge Neural Voices.

## Features
Clean and simple GUI (via tkinter)

Converts text to speech using edge-tts

Saves audio as ausgabe.mp3

Uses KatjaNeural (a high-quality German voice)

## How It Works
Opens a GUI window with a text box and a button

On click, it runs edge-tts using asyncio

Saves the generated speech in the same folder

### Requirements
Python 3.8+

edge-tts

tkinter (usually pre-installed)

## Setup & Run
bash
Copy
Edit
pip install edge-tts
python edge_tts_gui.py

 Build Executable (GUI App)
To bundle the GUI version into a Windows .exe file:

🛠️ Build Instructions
bash
Copy
Edit
pip install edge-tts pyinstaller
pyinstaller --onefile --noconsole edge_tts_gui.py
The .exe file will be in the dist/ folder

Double-click it to open the app without needing Python

 ## Algorithms & Pseudocode
#  gtts_simple.py

Start
↓
Ask for user input (German text)
↓
Create TTS object with gTTS(lang="de")
↓
Save as "ausgabe.mp3"
↓
Print success message
↓
End

## edge_tts_gui.py

Start GUI window
↓
User enters text and clicks button
↓
Async function sends text to edge-tts
↓
Edge neural voice creates audio
↓
Save as "ausgabe.mp3"
↓
Show confirmation dialog
↓
End / Wait for new input



## Voice Used in Edge-TTS
By default, the voice used is:

de-DE-KatjaNeural
You can change it in the script:
by  adding in the python
voice="de-DE-KatjaNeural"

To find mre available links 
https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support

Credits
gTTS – Google Text-to-Speech API
edge-tts – Microsoft Edge TTS interface
Built with  using Python

