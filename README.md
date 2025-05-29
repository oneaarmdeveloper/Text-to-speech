# German Text-to-Speech (gTTS & Edge TTS)

This project contains two simple Python scripts that convert German text to spoken German in MP3 format.

You can choose between:
*   A command-line app using Google's gTTS (`gtts_simple.py`)
*   A desktop GUI app using Microsoft Edge's high-quality neural voices via `edge-tts` (`edge_tts_gui.py`)

## Project Contents

*   **`gtts_simple.py`**: Command-line version using Google TTS.
*   **`edge_tts_gui.py`**: GUI app using Edge neural voices (Katja).
*   **`requirements.txt`**: Python dependencies (you might need to create this based on the individual requirements).
*   **`README.md`**: This file.
*   **`test.py`**: (Assumed content) Script for testing if `edge-tts` works correctly.

---

## ▶ Option 1: `gtts_simple.py`

A minimal command-line script that takes German text input and creates an MP3 file using Google's gTTS.

### Features
*   Input via terminal
*   Converts instantly to MP3
*   Lightweight and easy to use

### How It Works
1.  Reads text from `input()`.
2.  Calls `gTTS(text, lang="de")`.
3.  Saves the audio as `ausgabe.mp3`.

### ⚙ Requirements
*   Python 3.8+
*   `gTTS`

### Setup & Run
1.  Install dependencies:
    ```bash
    pip install gtts
    ```
2.  Run the script:
    ```bash
    python gtts_simple.py
    ```

---

## ▶ Option 2: `edge_tts_gui.py`

A desktop GUI app that lets you paste German text and create natural-sounding speech using Edge Neural Voices.

### Features
*   Clean and simple GUI (via `tkinter`)
*   Converts text to speech using `edge-tts`
*   Saves audio as `ausgabe.mp3`
*   Uses `de-DE-KatjaNeural` (a high-quality German voice) by default

### How It Works
1.  Opens a GUI window with a text box and a button.
2.  On button click, it runs `edge-tts` using `asyncio`.
3.  Saves the generated speech in the same folder as `ausgabe.mp3`.

### Requirements
*   Python 3.8+
*   `edge-tts`
*   `tkinter` (usually pre-installed with Python)

### Setup & Run
1.  Install dependencies:
    ```bash
    pip install edge-tts
    ```
2.  Run the script:
    ```bash
    python edge_tts_gui.py
    ```

---

## Build Executable (GUI App - `edge_tts_gui.py`)

To bundle the GUI version (`edge_tts_gui.py`) into a standalone Windows `.exe` file:

### 🛠️ Build Instructions
1.  Install PyInstaller (if you haven't already) along with `edge-tts`:
    ```bash
    pip install edge-tts pyinstaller
    ```
2.  Navigate to your project directory in the terminal and run:
    ```bash
    pyinstaller --onefile --noconsole edge_tts_gui.py
    ```
    *   `--onefile`: Bundles everything into a single executable.
    *   `--noconsole`: Prevents the command-line console from appearing when the GUI app runs.

3.  The `.exe` file will be located in the `dist/` folder created in your project directory.
4.  You can double-click this `.exe` file to open the app without needing Python installed on the target machine.

---

## Algorithms & Pseudocode

### `gtts_simple.py`
Start
↓
Ask for user input (German text)
↓
Create TTS object with gTTS(text, lang="de")
↓
Save as "ausgabe.mp3"
↓
Print success message
↓
End


### `edge_tts_gui.py`
Start GUI window
↓
User enters text and clicks button
↓
Async function sends text to edge-tts (with specified voice, e.g., de-DE-KatjaNeural)
↓
Edge neural voice creates audio stream
↓
Save audio stream as "ausgabe.mp3"
↓
Show confirmation dialog (e.g., "File saved!")
↓
End / Wait for new input



---

## Voice Used in `edge-tts_gui.py`

By default, the voice used is:
**`de-DE-KatjaNeural`**

You can change this directly in the `edge_tts_gui.py` script. Look for a line similar to:
```python
VOICE = "de-DE-KatjaNeural"
# or
communicate = edge_tts.Communicate(text, "de-DE-KatjaNeural")

And modify the voice identifier string.
To find more available voices for Microsoft Edge TTS, refer to the official documentation:
Microsoft Cognitive Services - Speech Service: Language and voice support
Credits
gTTS: Google Text-to-Speech library
edge-tts: Python interface for Microsoft Edge's online text-to-speech service
Built with Python.

**How to use this:**
1.  Create a new file named `README.md` in the root directory of your GitHub project.
2.  Copy and paste the entire content above into that file.
3.  Commit and push to GitHub.

This will then render nicely on your GitHub project page.
You might also want to create a `requirements.txt` file that lists all dependencies for easier setup for users:

Users could then install all with `pip install -r requirements.txt`.

