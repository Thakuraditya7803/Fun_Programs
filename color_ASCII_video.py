import cv2
import os
import time

VIDEO_PATH = r"E:\omnicode\video.mp4"

ASCII = "@#8&o:*. "

WIDTH = 120


def convert_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    new_h = int(h / w * WIDTH * 0.45)

    # Resize grayscale image
    gray = cv2.resize(gray, (WIDTH, new_h))

    # Resize original frame for colors
    color_frame = cv2.resize(frame, (WIDTH, new_h))

    result = ""

    for y in range(new_h):
        for x in range(WIDTH):

            pixel = gray[y, x]

            # ASCII character
            index = int(pixel / 256 * len(ASCII))

            if index >= len(ASCII):
                index = len(ASCII) - 1

            char = ASCII[index]

            # OpenCV uses BGR
            b, g, r = color_frame[y, x]

            # ANSI RGB color
            result += f"\033[38;2;{r};{g};{b}m{char}"

        result += "\033[0m\n"

    return result


video = cv2.VideoCapture(VIDEO_PATH)

if not video.isOpened():
    print("ERROR: video.mp4 not found!")
    input("Press Enter to exit...")
    exit()


fps = video.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 24

delay = 1 / fps


while True:

    success, frame = video.read()

    if not success:
        break

    ascii_frame = convert_frame(frame)

    # Clear Windows terminal
    os.system("cls")

    print(ascii_frame, end="")

    time.sleep(delay)


video.release()