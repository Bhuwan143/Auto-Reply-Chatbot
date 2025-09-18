from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="xxxxxx",
)

command = "Hello, how are you?"
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named bhuwan who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like bhuwan."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)