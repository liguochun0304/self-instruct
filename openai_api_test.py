import os
import openai

# 读取环境变量 "OPENAI_API_KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")

# # 创建一个 GPT-3 请求
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="你好，我的房子是住宅性质，租给了别人，承租人办了家政服务餐饮的营业执照，对我会有什么不利的影响吗，比如会不会涉及到缴税的问题。",
    temperature=0.7,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 输出 GPT-3 的回答
# print(response.choices[0].text.strip())

print(response)
