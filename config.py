import json


def read_config():
    """"读取配置"""
    with open("config.json") as json_file:
        config = json.load(json_file)
    return config

config = read_config()

prompts_path = config["openai_config"]["prompts_path"]
openai_api_key = config["openai_config"]["openai_api_key"]
openai_api_url = config["openai_config"]["openai_api_url"]
cosplay_role = config["openai_config"]["cosplay_role"]

vits_api_url = config["vits_config"]["vits_api_url"]
vits_wav_path = config["vits_config"]["vits_wav_path"]
vits_id = config["vits_config"]["vits_id"]
vits_lang = config["vits_config"]["vits_lang"]
vits_length = config["vits_config"]["vits_length"]

voice_wav_path = config["voice_wav_path"]
input_mode = config["input_mode"]

