# import csv
# import wave
# import struct

# # 假设CSV文件名为audio_data.csv
csv_file = 'D:/vscode/code/item_vscode/SensorSteamService/DataBase/Man_Low_Lobs_ZERO_1_Null/AUDIO/Man_Low_Lobs_ZERO_1_Null_AUDIO.csv'

# # 假设采样率为44100Hz，这是常见的CD质量采样率
# sampling_rate = 16000


# audio_data = []
# # 打开CSV文件并读取数据
# with open(csv_file, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row[0] == 'AUDIO':
#             unix_timestamp = int(row[1])
#             audio_data += [int(x.replace("[", "").replace("]", "")) for x in row[2].split(',')]  # 将字符串转换为整数列表

# # 将音频数据转换为字节数据
# # 由于是16位PCM，每个样本需要2个字节
# audio_bytes = b''
# for sample in audio_data:
#     audio_bytes += struct.pack('<h', sample)  # '<h'表示小端格式的短整型

# # 保存为WAV文件
# wav_file = 'output.wav'
# with wave.open(wav_file, 'wb') as wav:
#     wav.setnchannels(1)  # 单声道
#     wav.setsampwidth(2)  # 每个样本2字节
#     wav.setframerate(sampling_rate)  # 设置采样率
#     wav.writeframes(audio_bytes)  # 写入音频数据

import csv
import numpy as np
import wave

def csv_to_pcm(csv_file, output_wav_file, sampling_rate=16000, num_channels=1):
    # 读取 CSV 文件中的数据
    pcm_data = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row[0] == "AUDIO":
                continue
            # 假设每行是一个 PCM 样本
            pcm_data.extend([int(value.replace("[", "").replace("]", "")) for value in row[2].split(",")])

    # 将 PCM 数据转为 numpy 数组
    pcm_data = np.array(pcm_data, dtype=np.int16)

    # 创建 WAV 文件并写入 PCM 数据
    with wave.open(output_wav_file, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)  # 单声道
        wav_file.setsampwidth(2)  # 16-bit 数据，每个样本占 2 字节
        wav_file.setframerate(sampling_rate)  # 设置采样率

        # 将 PCM 数据写入 WAV 文件
        wav_file.writeframes(pcm_data.tobytes())

    print(f"音频已保存为: {output_wav_file}")

# 示例调用
csv_to_pcm(csv_file, 'output_audio.wav')
