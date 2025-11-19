import tkinter as tk

ventana = tk.Tk()
ventana.title("Nombre y apellido")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe tu nombre y apellido:", font=("Arial", 12))
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

entrada2 = tk.Entry(ventana, font=("Arial", 12))
entrada2.pack(pady=5)

def mostrar_texto():
    texto = entrada.get()
    texto2 = entrada2.get()
    etiqueta_resultado.config(text=f"{texto}, {texto2}")

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)


ventana.mainloop()