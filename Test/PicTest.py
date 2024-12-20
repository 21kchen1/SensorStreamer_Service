import cv2

"""
    摄像测试
    @author chen
"""

# 打开摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 拍照
ret, frame = cap.read()
if not ret:
    print("无法从摄像头获取图像")
    exit()

# 保存照片
cv2.imwrite('photo.jpg', frame)

# 释放摄像头资源
cap.release()
print("照片已保存")