import openai_api.openAI as op
import vits_api.vits as vt
from voice_recognition.voice_to_text import AudioRecorder
from config import voice_wav_path, input_mode, vits_id, vits_lang, vits_length


def input_text():
    user_input = input("User: ")
    return user_input


def receive_variable(voice_wav):
    recorder = AudioRecorder(voice_wav)
    recorder.record_audio()
    recorder.transcribe_audio()
    transcribed_text = recorder.get_transcribed_text()
    print("转换后的文本：", transcribed_text)
    return transcribed_text


User_input = ""

while True:
    if input_mode == "text":
        User_input = input_text()
    elif input_mode == "voice":
        User_input = receive_variable(voice_wav_path)
    Assistant_content = op.chat(User_input)
    vt.vits_textToVodie(Assistant_content, vits_id, vits_lang, vits_length)
