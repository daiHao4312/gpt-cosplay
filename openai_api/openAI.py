import openai
from config import prompts_path, openai_api_key, openai_api_url, cosplay_role

openai.api_key = openai_api_key
openai.api_base = openai_api_url

# 初始对话

messages = []

# 从文本文件中读取提示词
with open(prompts_path, "r", encoding="utf-8") as file:
    prompts = file.read().splitlines()

# 添加提示词部分
for prompt in prompts:
    # print(prompt)
    messages.append({"role": "user", "content": prompt})

messages += [
    {"role": "assistant", "content": "好的！让我们开始{}扮演吧！请问有什么问题或者需要我帮助的吗？".format(cosplay_role)}
]

def chat(user_input):

    # 添加用户输入到对话中
    messages.append({"role": "user", "content": user_input})

    # 调用OpenAI聊天模型
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # 获取模型的回复消息
    model_reply = completion.choices[0].message

    # 添加模型回复到对话中
    messages.append(model_reply)

    # 输出模型回复
    print("Assistant:", model_reply["content"])
    return model_reply["content"]

