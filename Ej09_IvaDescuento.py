#CBTIS 89
#3°B PROGRAMACION MATUTINO
#Programa que muestra una ventana en la cual esta una caja de texto
#y tres botones para realizar diversos calculos

#Importamos la biblioteca tkinter que permite crear interfaces graficas en python
import tkinter as tk
from tkinter import messagebox #Messagebox sirve para mostrar cuadros de dialogo (Alertas, errores)

#Funciones principales

# funcion para calcular el IVA (impuesto al valor agregado 16%)
def calcular_iva():
    try:
        #obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get()) #Convertimos el texto a numero decimal
        # calculamos el 16% de IVA
        iva = cantidad * 0.16
        #Mostramos el resultado en la etiqueta de resultados 
        #etiqueta_resultado.config(text=f"Iva (16%): ${iva:.2f}")
    #Si el usuario no ingresa un numero, mostramos un mensaje de error
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad válida.")
        
#Funcion para calcular el 10% de decuento 
def calcular_descuento():
     try:
        #obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get()) #Convertimos el texto a numero decimal
        
        # calculamos el descuento 10%
        descuento = cantidad * 0.10
        
        #Mostramos el resultado en la etiqueta de resultados 
        #etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")
        
    #Si el usuario no ingresa un numero, mostramos un mensaje de error
     except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad válida.")

#Funcion para calcular el total a pagar(Considerando IVA y descuento)
def calcular_total():
    try:
        cantidad = float(entrada_cantidad.get())
        
        #Calculamos IVa y descuento 
        iva= cantidad * 0.16
        descuento = cantidad *0.10
        
        #Total =cantidad original + iva - descuento
        total = cantidad + iva - descuento
        
        #Mostramos el total en la pantalla
        #etiqueta_resultado.config(text=f"Total ah pagar: ${total:.2f}")
        
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese una cantidad valida.")




#INTERFAZ GRAFICA DE LA VENTANA PRNCIPAL

#Creamos la ventana principal
ventana = tk.Tk()#Inicia la aplicacion grafica 
ventana.title("Calcular IVA y Descuento")#Titulo de la ventana
ventana.geometry("300x250")#Tamaño (Ancho x Alto)
ventana.resizable(False, False)# Evitar que el usuario cambie el tamaño de la ventana

#ETIQUETA Y CAJA DE TEXTO

#Creamos una etiqueta que indica que debe escribir el usuario 
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad: ")
etiqueta_cantidad.pack(pady=10) #.pack() coloca el elemento y pady da un margen vertical

#Caja de texto donde se escribira la cantidad
entrada_cantidad = tk.Entry(ventana,  justify="center")# justify centra el texto
entrada_cantidad.pack()# Se agrega a la ventana

# BOTONES DE ACCIÓN

#Pagina para colores https://python-charts.com/es/colores/

#Boton que calcula el IVA
btn_iva=tk.Button