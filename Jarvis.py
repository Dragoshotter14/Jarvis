import openai

# Define a chave de API
openai.api_key = "YOU-API-KEY-HERE"

# Define a pergunta
print("Oi, eu sou o Jarvis!")
while True:
    prompt = input("Digite sua pergunta para o Jarvis (ou digite 'sair' para encerrar): ")
    if prompt.lower() == "sair":
        break

    # Define os parâmetros de chamada da API
    parameters = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 100,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Faz a chamada da API
    response = openai.Completion.create(**parameters)

    # Obtém a resposta
    answer = response.choices[0].text.strip()

    # Imprime a resposta
    print(answer)
