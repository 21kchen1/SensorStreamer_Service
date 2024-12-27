import csv
import numpy as np
import wave

"""
    测试音频还原
    @version 1.0
    @author chen
"""

# CSV 文件路径
csv_file = 'AUDIO3.csv'
# csv_file = 'G:\\Badminton\\测试数据\\Man_Low_Lobs_ZERO_4_Null_AUDIO.csv'
wav_file = 'output2_audio.wav'

# 设定参数
sampling_rate = 16000  # 采样率
channels = 1  # 单声道
sample_width = 4  # 16-bit 每个样本 4 字节

# 读取 CSV 文件并提取音频数据
audio_samples = []
timestamp = 0
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row[0] == "AUDIO":
            continue
        # 提取音频数据（假设音频数据在 CSV 的第三列）
        audio_data_str = row[3].strip('[]"')  # 去掉字符串的中括号和双引号
        audio_samples.extend(list(map(int, audio_data_str.split(', '))))  # 将字符串转为整数列表
        timestamp = int(row[1])

print(f"dataLen: { len(audio_samples) }, hopeLen: { sampling_rate * timestamp / 1000 }")

# 将音频数据转换为 numpy 数组
audio_data = np.array(audio_samples, dtype=np.int16)
audio_data = np.clip(audio_data * 100, -32768, 32767)

# 将音频数据保存为 WAV 文件
with wave.open(wav_file, 'wb') as wav_file_obj:
    wav_file_obj.setnchannels(channels)  # 设置声道数
    wav_file_obj.setsampwidth(sample_width)  # 设置采样宽度
    wav_file_obj.setframerate(sampling_rate)  # 设置采样率
    wav_file_obj.writeframes(audio_data.tobytes())  # 写入音频数据

print(f"音频文件已保存为 {wav_file}")