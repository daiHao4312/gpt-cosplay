# gpt-cosplay

## Description
可以实现语音与特定人物的对话，目前支持的人物有很多，默认是爱莉希雅。这个项目只是一个demo，所以没有做UI，优化会比较差。

本人不是专业的开发者，所以代码写的比较烂，如果有什么问题可以提issue，我会尽量解决。

因为语音识别是用的谷歌的，所以需要翻墙，如果你不想翻墙，可以自己换成sphinx。在voice_to_text.py中修改即可。
```
transcribed_text = r.recognize_sphinx(audio, language="zh_CN")
```
也可以使用国内的语音识别，这个就需要自己去找了。

关于vits的api，可以参考这个项目：https://github.com/Artrajz/vits-simple-api
这个需要自己搭建。


## Usage
主要是修改config.json中的配置，然后运行main.py即可
```
{
  "openai_config": {
    "prompts_path": "./openai_api/prompts.txt",
    "openai_api_key": "sk-***",
    "openai_api_url": "https://***",
    "cosplay_role": "爱莉希雅"
  },
    "vits_config": {
      "vits_api_url": "http://127.0.0.1:23456/voice/vits",
      "vits_wav_path": "./vits_api/WAV/test.wav",
      "vits_id": "255",
      "vits_lang": "zh",
      "vits_length": "1.4"
    },

  "voice_wav_path": "./voice_recognition/WAV_VOICE/voice.wav",
  "input_mode": "text"
}
```
主要的配置项有：
- openai_config
  - prompts_path: openai的prompt文件路径
  - openai_api_key: （必须）openai的api key
  - openai_api_url: （必须）openai的api url
  - cosplay_role: 人物名称
- vits_config
  - vits_api_url: （必须）vits的api url
  - vits_wav_path: vits的wav文件路径
  - vits_id: （必须）vits的id
  - vits_lang: （必须）vits的语言
  - vits_length: （必须）vits的语速

- voice_wav_path: 语音识别的wav文件路径
- input_mode: （必须）输入模式，目前支持text和voice两种

## 如果你想换人物
1. 可以修改openai_api/prompts.txt文件，里面默认的是爱莉希雅，想要别的角色可以自己修改。
2. 修改config.json中的cosplay_role字段，改成你想要的角色名称即可。
3. 修改vits_id，找到对应的角色id。（本项目的角色id是对应的我搭建的vits的）

## 如果你想换语音识别
1. 修改config.json中的input_mode字段，改成voice即可。默认是text，即文本输入。
voice模式下，需要按1是开始录音，按2是结束录音。

## 配置环境
1. 安装python3.7以上版本
2. 安装依赖包，可以使用pip install -r requirements.txt安装
```
openai==0.28.0
requests==2.31.0
PyAudio
SpeechRecognition==3.9.0
keyboard==0.13.5
```
3. 如果还差什么包，自己去pip安装即可
4. 项目本身包含虚拟环境，可以直接使用

## 启动项目
直接运行main.py即可

# gpt-cosplay
# gpt-cosplay
