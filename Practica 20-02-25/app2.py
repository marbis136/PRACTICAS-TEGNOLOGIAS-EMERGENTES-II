#Set-ExecutionPolicy Unrestricted -Scope CurrentUser
import ollama
import subprocess

def consultar_modelo(prompt):
    resultado = subprocess.run(
        ["ollama", "run", "deepseek-r1:1.5b"],
        input=prompt.encode(),
        capture_output=True
    )
    return resultado.stdout.decode()

respuesta = consultar_modelo("Dime cuales son las causas mas frecuentes para la desercion estudiantil en las Universidades de Bolivia")
print(respuesta)