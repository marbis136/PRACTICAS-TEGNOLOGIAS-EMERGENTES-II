import tkinter as tk
from tkinter import scrolledtext, messagebox
from openai import OpenAI
import time

def enviar_mensaje(event=None):
    pregunta = entrada_texto.get()
    if not pregunta.strip():
        messagebox.showwarning("Advertencia", "Por favor, ingresa una pregunta.")
        return
    
    modelo_seleccionado = modelo_var.get()
    client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")
    
    tiempo_label.config(text="Procesando...")
    ventana.update_idletasks()
    
    inicio = time.time()
    chat = client.chat.completions.create(
        model=modelo_seleccionado,
        messages=[
            {"role": "user", "content": pregunta}
        ]
    )
    fin = time.time()
    
    if chat and hasattr(chat, 'choices') and len(chat.choices) > 0:
        respuesta = chat.choices[0].message.content
    else:
        respuesta = "Error: No se recibió una respuesta válida de la API."
    
    tiempo_total = fin - inicio
    tiempo_label.config(text=f"Tiempo: {tiempo_total:.2f} seg")
    area_texto.insert(tk.END, f"Tú: {pregunta}\nBot: {respuesta} (Tiempo Respuesta Tardada: {tiempo_total:.2f} seg)\n\n")
    entrada_texto.delete(0, tk.END)

def ajustar_responsive(event):
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    area_texto.config(width=int(width / 10), height=int(height / 30))
    entrada_texto.config(width=int(width / 12))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Chat con OpenAI")
ventana.geometry("600x500")
ventana.configure(bg="#282c34")
ventana.bind("<Configure>", ajustar_responsive)

# Área de texto desplazable
area_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, bg="#1e1e1e", fg="#ffffff")
area_texto.pack(pady=10, fill=tk.BOTH, expand=True)

# Entrada de texto
entrada_texto = tk.Entry(ventana, bg="#333842", fg="#ffffff")
entrada_texto.pack(pady=5, fill=tk.X, padx=10)
entrada_texto.bind("<Return>", enviar_mensaje)

# Selección de modelo
modelos = [
    "deepseek/deepseek-r1:free",
    "deepseek/deepseek-r1-distill-llama-70b:free",
    "nvidia/llama-3.1-nemotron-70b-instruct:free",
    "google/gemini-2.0-pro-exp-02-05:free"
]
modelo_var = tk.StringVar(value=modelos[0])
modelo_menu = tk.OptionMenu(ventana, modelo_var, *modelos)
modelo_menu.config(bg="#3a3f4b", fg="#ffffff")
modelo_menu.pack(pady=5, fill=tk.X, padx=10)

# Botón para enviar mensaje y etiqueta de tiempo
frame_envio = tk.Frame(ventana, bg="#282c34")
frame_envio.pack(pady=5, fill=tk.X, padx=10)

boton_enviar = tk.Button(frame_envio, text="Enviar", command=enviar_mensaje, bg="#007acc", fg="#ffffff", padx=10, pady=5)
boton_enviar.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Etiqueta para mostrar el tiempo de respuesta
tiempo_label = tk.Label(frame_envio, text="Tiempo: 0.00 seg", bg="#282c34", fg="#ffffff")
tiempo_label.pack(side=tk.RIGHT)

# Ejecutar la aplicación
ventana.mainloop()
