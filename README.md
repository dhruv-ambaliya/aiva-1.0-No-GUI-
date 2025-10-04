# AIVA 1.0 (No-GUI Version)

![AIVA Snap](ironsnap2.gif)

AIVA 1.0 is a Python-based personal assistant for Windows designed for desktop automation, task management, email handling, and more—all via voice commands or scripts. This version operates entirely through the command-line and script execution, with no graphical interface.

---

## Features

- **Voice Assistant**: Listens to your commands and executes tasks using speech recognition and synthesis.
- **Task Scheduling**: Manage daily tasks, set alarms, and reminders.
- **Email Automation**: Send and read emails (Gmail integration, attachments supported).
- **Web Automation**: Open/close apps, browse the internet, fetch news, and more.
- **Fun Interactions**: Jokes, games (Rock Paper Scissors), and Wikipedia queries.
- **System Controls**: Volume, media, shutdown/restart/sleep, screenshot, and focus mode (blocks distracting websites).
- **PDF Reading**: Reads out content from PDF books.
- **News & Weather**: Fetches latest news and weather updates.
- **No GUI**: All interactions are via terminal or voice; suitable for automation and scripting.
- **Extensible**: Easily add new features or integrate APIs.

---

## Directory Structure

```
aiva-1.0-No-GUI-/
├── aiva_main.py         # Main assistant script
├── alarm.py             # Alarm and reminders
├── Cal.py               # Calculator functions (WolframAlpha)
├── Calculatenumbers.py  # Calculation utilities
├── Dictapp.py           # App/web shortcuts
├── FocusMode.py         # Focus mode (website blocker)
├── FocusGraph.py        # Visualization for focus sessions
├── GreetMe.py           # Greeting utilities
├── INTRO.py             # Intro animation and audio
├── NewsRead.py          # News reading utility
├── game.py              # Voice-controlled game
├── keyboard.py          # Volume/media controls
├── email_send.py        # Email sending with attachments
├── email_control.py     # Email reading (Gmail API)
├── Whatsapp.py          # WhatsApp automation
├── Translator.py        # Translate and speak phrases
├── SearchNow.py         # Unified search (web, YouTube, Wikipedia)
├── ironsnap2.gif        # Thematic GIF
├── music.mp3            # Audio for alarms/notifications
├── requirements.txt     # Python dependencies
├── credentials.json     # Gmail API credentials (user-provided)
└── README.md            # This file
```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dhruv-ambaliya/aiva-1.0-No-GUI-.git
   cd aiva-1.0-No-GUI-
   ```

2. **Install Dependencies**
   Install Python 3.x and required packages. You can use the provided `requirements.txt` or install manually:
   ```bash
   pip install -r requirements.txt
   ```
   Or, for common packages:
   ```bash
   pip install pyttsx3 SpeechRecognition numpy pyjokes wikipedia pygame plyer speedtest-cli requests beautifulsoup4 termcolor matplotlib pynput Pillow google-api-python-client google-auth-httplib2 google-auth-oauthlib googletrans gtts playsound
   ```
   > **Note:** Some scripts require API keys (WolframAlpha, NewsAPI, Gmail API). Update the scripts with your keys where indicated.

3. **Microphone & Audio Setup**
   - Ensure your microphone and speakers are configured and working for voice input/output.

---

## Usage

- **Run the main assistant (voice-controlled):**
  ```bash
  python aiva_main.py
  ```

- **Standalone Scripts:**  
  Many scripts can also be run directly for their specific features, e.g.:
  ```bash
  python alarm.py
  python FocusMode.py
  python email_send.py
  ```

- **Typical Commands:**
  - "What's the weather in [city]?"
  - "Set an alarm for 7:00 AM"
  - "Play music"
  - "Send an email"
  - "Tell me a joke"
  - "Open [application]"
  - "Shutdown the system"
  - "Translate 'hello' to Spanish"

- **Focus Mode:**  
  Blocks distracting websites until a specified time.

- **Alarm:**  
  Set alarms via voice or text.

- **Game:**  
  Play Rock-Paper-Scissors with your voice.

---

## Customization & Extending

- **Email Setup:**  
  For Gmail, place your `credentials.json` in the root and configure OAuth as per Google’s instructions.
- **Contacts:**  
  Add your contacts to the relevant dictionaries in the email scripts.
- **APIs:**  
  Insert your API keys in the scripts for WolframAlpha, NewsAPI, etc.
- **Add Features:**  
  Extend by adding new Python modules for more skills.

---

## Contributing

Feel free to submit issues or pull requests! Contributions to improve code, documentation, or features are welcome.

---

## License

This project is under the MIT License.

---

> **Note**: This project is for educational and personal use. Please review each script for credentials and sensitive information before use.
