import openai
from get_env import print_env

env = print_env(['app_key'])

openai.api_key = env['app_key']
while True:
    def generate_text(prompt):
        completions = openai.Completion.create(
            engine= "text-davinci-003",
            prompt=prompt,
            max_tokens = 700,
            n=1,
            stop = None,
            temperature = 0.5,
        )
        message = completions.choices[0].text
        return message.strip()

    prompt = input("Faça um pergunta para o ChatGPT: \n")
    print(generate_text(prompt))

    saida = input("você deseja sair do CHAT GPT ?")
    if saida == 'sim':
        break