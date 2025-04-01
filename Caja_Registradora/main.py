import tkinter as tk
from tkinter import ttk,messagebox, scrolledtext
from producto import Producto

ventana= tk.Tk()
ventana.geometry('700x500')
ventana.title('Tienda Fruber App')
ventana.iconbitmap('vegetales.ico')
ventana.configure(background='#2e86c1')


# grid
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0,weight=1)

# Crear estilo
style = ttk.Style()
style.configure("Custom.TFrame", background="lightblue")
style.configure("Custom.TLabel", background="lightblue", font=("Arial", 10))
style.configure("Titulo.TLabel", background="lightblue", font=("Arial", 20, "bold"), 
                 anchor="center", justify="center")

def crear_componentes_caja(tabulador):
    etiqueta0=ttk.Label(tabulador,text='🛒 Carrito de compras',style="Titulo.TLabel")
    etiqueta0.grid(padx=30, pady=10,columnspan=4)

    etiqueta1=ttk.Label(tabulador,text='Producto: ',style="Custom.TLabel")
    etiqueta1.grid(row=1, column=0)

    etiqueta2=ttk.Label(tabulador,text='Cantidad: ',style="Custom.TLabel")
    etiqueta2.grid(row=1, column=2)

    producto_obj = Producto()
    listado_productos=producto_obj.consultar_productos()
    productos=ttk.Combobox(tabulador,width=30, values=listado_productos)
    productos.grid(row=1,column=1,padx=5, pady=5)
    entrada2=ttk.Spinbox(tabulador,width=10, from_=1,to=100 , state='readonly')
    entrada2.grid(row=1,column=3,padx=5, pady=5)

    boton1=ttk.Button(tabulador, text='➕ Agregar')
    boton1.grid(row=1,column=4,columnspan=2)

     #tabla de ventas
    columnas=('Codigo','Nombre','Stocks','Costo kilo','Sub total')
    tabla=ttk.Treeview(tabulador,columns=columnas, show='headings')
    tabla.grid(padx=50,pady=40,columnspan=6)

    tabla.heading('Codigo',text='Codigo')
    tabla.heading('Nombre',text='Nombre')
    tabla.heading('Stocks',text='Cantidad')
    tabla.heading('Costo kilo',text='Costo kilo')
    tabla.heading('Sub total',text='Sub total')

    tabla.column('Codigo' , width=80)
    tabla.column('Stocks', width=80)
    tabla.column('Costo kilo', width=80)
    tabla.column('Sub total', width=80)

    # total
    etiqueta0=ttk.Label(tabulador,text='💰Total: ',style="Titulo.TLabel")
    etiqueta0.grid(row=3,column=1)
    Total=ttk.Entry(tabulador,width=30 )
    Total.grid(row=3,column=2)

    boton2=ttk.Button(tabulador, text='🔚 Finalizar')
    boton2.grid(row=3,column=3,columnspan=2)


def crear_componentes_stock(tabulador):
    etiqueta0=ttk.Label(tabulador,text='📋 Inventario',style="Titulo.TLabel")
    etiqueta0.grid(padx=30, pady=10,columnspan=7)

    #tabla
    columnas=('Codigo','Nombre','Stocks','Costo kilo')
    tabla=ttk.Treeview(tabulador,columns=columnas, show='headings')
    tabla.grid(padx=30,row=1 ,column=1)

    tabla.heading('Codigo',text='Codigo')
    tabla.heading('Nombre',text='Nombre')
    tabla.heading('Stocks',text='Cantidad')
    tabla.heading('Costo kilo',text='Valor kilo')

    tabla.column('Codigo' , width=80)
    tabla.column('Stocks', width=80)
    tabla.column('Costo kilo', width=80)

    producto_obj = Producto()
    listado_productos=producto_obj.consultar_inventario()
    for producto in listado_productos:
        tabla.insert(parent='',index=tk.END,values=producto)

    

def crear_componentes_ventas(tabulador):
    etiqueta0=ttk.Label(tabulador,text=' 🗂 Historico de ventas',style="Titulo.TLabel")
    etiqueta0.grid(padx=30, pady=10,columnspan=7)

def crear_tabs():
    #creamos tab control 
    ctrl_tabulador=ttk.Notebook(ventana)
    ctrl_tabulador.pack(padx=10, pady=10, expand=True)

    stock=ttk.Frame(ctrl_tabulador,  style="Custom.TFrame")
    ctrl_tabulador.add(stock, text='Stock')
    crear_componentes_stock(stock) 

    caja=ttk.Frame(ctrl_tabulador, style="Custom.TFrame")
    ctrl_tabulador.add(caja,text='Caja Registradora')
    ctrl_tabulador.pack(fill='both',ipadx=30, ipady=6)
    crear_componentes_caja(caja)

    ventas=ttk.Frame(ctrl_tabulador,  style="Custom.TFrame")
    ctrl_tabulador.add(ventas, text='Historial de ventas')
    crear_componentes_ventas(ventas)


crear_tabs()
ventana.mainloop()