import tkinter as tk
def SubTotal():
    global subtotal
    cantidad = float(entrada_cantidad.get())
    precio = float(entrada_precio.get())
    subtotal = cantidad*precio
    
    resultado.config(text=f"SubTotal: {subtotal}")
def IVA():
      global iva
      iva = subtotal * 0.16
      resultado.config(text=f"IVA: {iva:.2f}")
def Total():
      total = subtotal + iva
      resultado.config(text=f"Total: {total:.2f}")

ventana = tk.Tk()
ventana.title("Calculo de ventas")
ventana.geometry("350x230")
tk.Label(ventana, text="Cantidad de artículos").pack(pady=5)
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack(pady=5)

# Etiqueta y entrada de precio
tk.Label(ventana, text="Precio por artículo").pack(pady=5)
entrada_precio = tk.Entry(ventana)
entrada_precio.pack(pady=5)
boton_sumar = tk.Button(ventana, text="SubTotal", command=SubTotal)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="IVA", command=IVA)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Total de la compra", command=Total)
boton_sumar.pack(pady=5)
resultado = tk.Label(ventana, text="Total:")
resultado.pack(pady=5)
ventana.mainloop()
