import cv2
import os
import time

VIDEO_PATH = "\asciiv.html"

ASCII = "@#8&o:*. "

WIDTH = 120


def convert_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    new_h = int(h / w * WIDTH * 0.45)

    gray = cv2.resize(gray, (WIDTH, new_h))

    result = ""

    for row in gray:
        for pixel in row:
            index = int(pixel / 256 * len(ASCII))

            if index >= len(ASCII):
                index = len(ASCII) - 1

            result += ASCII[index]

        result += "\n"

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

    # Windows terminal clear
    os.system("cls")

    print(ascii_frame)

    time.sleep(delay)


video.release()