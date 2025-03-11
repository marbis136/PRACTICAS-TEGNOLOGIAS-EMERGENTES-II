from openai import  OpenAI

client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model = "deepseek/deepseek-r1:free", #24.7B tokens
    #model = "deepseek/deepseek-r1-distill-llama-70b:free", #2.84B tokens
    #model = "nvidia/llama-3.1-nemotron-70b-instruct:free", #1.16B tokens
    #model = "google/gemini-2.0-pro-exp-02-05:free", #6.7B tokens
    messages=[
        {
            "role": "user",
            "content": "dime quiene es la mujer mas alta"
        }
    ]
)

# Verifica si la respuesta es válida
if chat and hasattr(chat, 'choices') and len(chat.choices) > 0:
    # Imprime el mensaje de respuesta
    print(chat.choices[0].message.content)
else:
    print("Error: No se recibió una respuesta válida de la API.")
