import csv
import cv2
import numpy as np
import io

"""
    测试视频还原
    @version 1.0
    @author chen
"""

# csv_file = "VIDEO.csv"
csv_file = 'G:\\Badminton\\测试数据\\TEST\\Man_Low_BackhandTransition_LeiYang_1_1_VIDEO2.csv'
valueLocal = 4
avi_file = "output2.avi"

frames = []  # 这里应该是你的图像帧列表，每个元素都是一个numpy.ndarray

with open(csv_file, newline= "", encoding= "utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row[0] == "VIDEO":
            continue
        values = row[valueLocal].strip('[]"')
        values = list(map(int, values.split(", ")))
        # 将字节列表转换为字节数据
        dataBytes = np.array(values, dtype=np.uint8).tobytes()
        # 使用 io.BytesIO 将字节数据转换为文件类对象
        imageData = io.BytesIO(dataBytes).getvalue()
        # 使用 cv2 读取图像数据
        image = cv2.imdecode(np.frombuffer(imageData, np.uint8), cv2.IMREAD_UNCHANGED)
        frames.append(image)

# 定义视频编码器和创建VideoWriter对象
# 例如，使用XVID编码器，输出视频的分辨率为(640, 480)，帧率为20fps
out = cv2.VideoWriter(avi_file, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

# 将每一帧图像写入视频
for frame in frames:
    # 确保frame是numpy.ndarray类型
    out.write(frame)

# 释放VideoWriter对象
out.release()

print(f"生成 { avi_file }.")