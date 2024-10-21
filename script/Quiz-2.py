#Matías Barrantes Rojas
import tkinter as tk
from tkinter import messagebox

TASA_CONVERSION = 514.47

def realizar_conversion():
    try:
        valor_dolares = float(entrada_dolares.get())
        valor_colones = valor_dolares * TASA_CONVERSION
        resultado_conversion.config(text=f"{valor_dolares} USD = {valor_colones:.2f} CRC")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

def limpiar_campos():
    entrada_dolares.delete(0, tk.END)
    resultado_conversion.config(text="")

def confirmar_salida():
    if messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?"):
        ventana.destroy()

ventana = tk.Tk()
ventana.title("Conversor de USD a CRC")
ventana.geometry("400x200")

etiqueta_dolares = tk.Label(ventana, text="Monto en USD:")
etiqueta_dolares.grid(row=0, column=0, padx=10, pady=10)

entrada_dolares = tk.Entry(ventana)
entrada_dolares.grid(row=0, column=1, padx=10, pady=10)

boton_convertir = tk.Button(ventana, text="Convertir", command=realizar_conversion)
boton_convertir.grid(row=1, column=0, padx=10, pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.grid(row=1, column=1, padx=10, pady=10)

resultado_conversion = tk.Label(ventana, text="")
resultado_conversion.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)

ventana.mainloop()