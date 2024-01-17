# 导入requests库
import requests
# 导入pyaudio库
import pyaudio
# 导入wave库
import wave
from config import vits_api_url, vits_wav_path

def vits_textToVodie(text, id = "225", lang = "zh", length = "1.4"):
    # 定义请求的URL和参数
    url = vits_api_url
    params = {
        "text": text,
        "id": id,
        "lang": lang,
        "length": length,

        # "text": "你好，这是一个测试",
        # "id": "225",
        # "lang": "zh"
    }

    # 发送GET请求，并获取响应对象
    response = requests.get(url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 从响应对象中获取音频数据
        audio_data = response.content
        # 保存音频数据到本地文件
        with open(vits_wav_path, "wb") as f:
            f.write(audio_data)
        # 打印成功信息
        print("音频文件已保存")
    else:
        # 打印错误信息
        print("请求失败，状态码为", response.status_code)





    # 打开一个WAV文件
    with wave.open(vits_wav_path, 'rb') as f:
        # 获取文件的参数
        nchannels, sampwidth, framerate, nframes, comptype, compname = f.getparams()
        # 读取文件的数据
        data = f.readframes(nframes)

    # 创建一个PyAudio对象
    p = pyaudio.PyAudio()
    # 打开一个流
    stream = p.open(format=p.get_format_from_width(sampwidth),
                    channels=nchannels,
                    rate=framerate,
                    output=True)
    # 播放音频数据
    stream.write(data)
    # 关闭流
    stream.stop_stream()
    stream.close()
    # 终止PyAudio对象
    p.terminate()
