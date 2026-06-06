# Simple Python Alarm Clock ⏰

A lightweight, terminal-based alarm clock built with Python and Pygame that plays your favorite soundtrack when the designated time is reached.

---

## 🚀 Features

* **Real-time Tracking:** Displays a second-by-second countdown/current time update in the terminal.
* **Custom Audio Playback:** Uses `pygame.mixer` for high-quality audio streaming.
* **Simple Interface:** Quick and easy time configuration directly via the command line.
* **Automatic Shutoff:** Smart loop tracking ensures the script cleanly exits once the audio finishes playing.

---

## 🛠️ Prerequisites & Requirements

Before running the project, ensure you meet the following requirements:

* **Python Version:** Python `3.12.x` is highly recommended.
* **External Libraries:** You will need the `pygame` library installed.

### Installation

1. Clone this repository or copy the script to your local machine.
2. Install the required dependency using pip:

## ⚙️ Configuration (Important!)
Before running the alarm, you must configure your own audio file path.
Open the script and locate the soundtrack variable inside the `set_alarm` function. Update it with the path to your specific `.mp3` or `.wav` file: