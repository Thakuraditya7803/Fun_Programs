# 🎥 Video to ASCII Art

A simple Python project that converts a video into **real-time ASCII art** and displays it directly in the Windows terminal.

The project uses **OpenCV (`cv2`)** to read video frames, converts each frame to grayscale, resizes it, and maps pixel brightness to ASCII characters.

---

## ✨ Features

* 🎬 Converts video frames into ASCII art
* 🖥️ Displays the animation directly in the terminal
* ⚡ Plays the ASCII animation in real time
* 🎨 Uses different characters based on pixel brightness
* 📐 Automatically maintains the video's aspect ratio
* 🐍 Built with Python and OpenCV
* 🪟 Designed for Windows Terminal / Command Prompt

---

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV**
* `os`
* `time`

---

## 📁 Project Structure

```text
video-to-ascii/
│
├── ascii_video.py
├── README.md
└── video/
    └── video.mp4
```

---

## 🚀 Installation

### 1. Install Python

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

---

### 2. Install OpenCV

Open your VS Code terminal and run:

```bash
pip install opencv-python
```

---

## ▶️ How to Run

Open the project folder in VS Code.

Then run:

```bash
python ascii_video.py
```

The video will be read frame-by-frame and displayed as ASCII characters in the terminal.

---

## ⚙️ Configuration

You can customize the ASCII output using these variables:

### Video Path

```python
VIDEO_PATH = r"E:\omnicode\asciiv.html"
```

Change this to the location of your video.

For example:

```python
VIDEO_PATH = r"E:\omnicode\video.mp4"
```

> **Note:** The current code expects a video file. An `.html` file will not work as a video source.

---

### ASCII Characters

```python
ASCII = "@#8&o:*. "
```

These characters represent different brightness levels.

Dark pixels use characters near the beginning:

```text
@
#
8
&
o
:
*
.
 
```

Bright pixels use characters near the end.

You can experiment with your own character set:

```python
ASCII = "@%#*+=-:. "
```

or:

```python
ASCII = "█▓▒░ "
```

---

### Width

```python
WIDTH = 120
```

This controls the width of the ASCII video. (isse screen ka size change hoga ismai change krna )

Smaller value:

```python
WIDTH = 80
```

➡️ Faster and easier to read.

Larger value:

```python
WIDTH = 160
```

➡️ More detailed but uses more terminal space.

---

## 🧠 How It Works

The program follows this process:

```text
Video
  ↓
Read Frame
  ↓
Convert to Grayscale
  ↓
Resize Frame
  ↓
Read Pixel Brightness
  ↓
Map Brightness → ASCII Character
  ↓
Print ASCII Frame
  ↓
Repeat
```

---

## 🔍 Code Explanation

### 1. Import Libraries

```python
import cv2
import os
import time
```

* `cv2` → Reads and processes the video
* `os` → Clears the Windows terminal
* `time` → Controls playback speed

---

### 2. Convert Frame to Grayscale

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

A normal video frame contains three color channels:

```text
Blue
Green
Red
```

The code converts it into a single grayscale value.

Each pixel then has a brightness value between:

```text
0 → Black
255 → White
```

---

### 3. Resize the Frame

```python
new_h = int(h / w * WIDTH * 0.45)

gray = cv2.resize(gray, (WIDTH, new_h))
```

The frame is resized so that the ASCII output fits inside the terminal.

The `0.45` factor compensates for the fact that terminal characters are usually taller than they are wide.

---

### 4. Convert Pixels to ASCII

```python
index = int(pixel / 256 * len(ASCII))
```

A pixel's brightness is converted into an index for the ASCII character list.

For example:

```text
Dark pixel     → @
                ↓
               #
               8
               &
               o
               :
               *
               .
Bright pixel   → space
```

---

### 5. Print the Frame

```python
print(ascii_frame)
```

The generated ASCII art is printed to the terminal.

---

### 6. Clear the Previous Frame

```python
os.system("cls")
```

`cls` clears the Windows terminal before displaying the next frame.

This creates the illusion of animation.

---

### 7. Control Playback Speed

```python
fps = video.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 24

delay = 1 / fps
```

The video's FPS is used to calculate how long the program should wait between frames.

For example:

```text
24 FPS

1 / 24
≈ 0.041 seconds
```

So approximately 24 frames are displayed every second.

---

## ⚠️ Troubleshooting

### `video.mp4 not found!`

Check your video path.

Example:

```python
VIDEO_PATH = "File ka path can be in MP4,HTML or Txt"
```

Make sure the file actually exists.

---

### ASCII output is too large

Decrease:

```python
WIDTH = 120
```

to:

```python
WIDTH = 80
```

---

### ASCII output is too small

Increase:

```python
WIDTH = 160
```

---

### Video looks unclear

ASCII art has limited visual resolution.

Try using more ASCII characters:

```python
ASCII = "@%#*+=-:. "
```

You can also increase:

```python
WIDTH = 160
```

---

### Terminal flickers

The current implementation uses:

```python
os.system("cls")
```

on every frame, which can cause flickering.

A more advanced version can use terminal cursor control instead of completely clearing the screen.

---

## 💡 Possible Improvements

Future versions could include:

* 🎨 Colored ASCII output
* 🔊 Audio playback
* ⏩ Adjustable playback speed
* 📏 Automatic terminal-size detection
* 🎞️ Better frame rendering
* 🚫 Reduced terminal flickering
* 🌈 ANSI colors
* 🖼️ Image-to-ASCII conversion
* 🎥 Webcam-to-ASCII conversion
* 💻 Cross-platform support for Windows, Linux and macOS
* ⚡ Faster rendering using buffered output

---

## 📌 Important Note

This project is intended for **terminal-based ASCII animation**.

It does not create a new video file. Instead, it reads the original video and converts each frame into ASCII characters while the program is running.

---

## 📄 License

This project is free to use and modify for learning and personal projects.

---

## ⭐ Project Idea

> **Turn any video into a terminal-style ASCII animation using Python.**

```text
████████████████████████████████
██                            ██
██       ASCII VIDEO          ██
██                            ██
████████████████████████████████
```

Made with 🐍 Python + OpenCV.
