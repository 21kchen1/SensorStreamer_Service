import cv2
import logging

WIN_NAME = "1"
CAP_WIDTH = 2560
CAP_HEIGHT = 1440
CAP_NUM = 10


cap = None
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT)
if not cap.isOpened():
    print("error")
    exit(0)

print(f"_getPicture: CAP_PROP_FRAME = { cap.get(cv2.CAP_PROP_FRAME_WIDTH) } : { cap.get(cv2.CAP_PROP_FRAME_HEIGHT) }")
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FPS, 30)
while True:
    continue
#     # 读取每一帧
#     ret, frame = cap.read()
#     if not ret:
#         logging.warning("_getPicture: Unable to read frames")
#         continue
#     cv2.imshow(WIN_NAME, frame)
#     # 等待按键 s
#     theKey = cv2.waitKey(1)