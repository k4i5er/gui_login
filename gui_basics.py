# Importamos todos los elementos de la librería tkinter
from tkinter import *
# Importamos todos los elementos de la sublibrería ttk
from tkinter.ttk import *

validUser = 'yo'
validPasswd = 'mero'


def loginCheck():
    if entry_username.get() == validUser and entry_passwd.get() == validPasswd:
        # print(f'¡Bienvenido {entry_username.get()}!')
        lbl_message.configure(
            text=f'¡Bienvenido {entry_username.get()}!', foreground='#3BFF00')
    elif entry_username.get() == validUser and entry_passwd.get() != validPasswd:
        lbl_message.configure(
            text=f'Tu contraseña es: {validPasswd}!', foreground='#3BFF00')
    else:
        lbl_message.configure(foreground='#F88683',
                              text='Usuario/contraseña no válidos, ¿olvidaste tu contraseña?\nRecupérala con el botón "Recuperar contraseña"')


# Contenedor principal
root = Tk()  # Crear una instancia de Tk llamada 'root'

# Cambiamos las dimensiones de la ventana
root.geometry('400x200')
# Cambiamos el título de la ventana
root.title('Mi primera ventana en Python')
# Cambiamos el color del viewport
root.configure(bg='#335FA3')

# Estilos para los Widgets
styles = Style()
styles.configure('TFrame', background='#335FA3')
styles.configure('TLabel', width=10, background='#335FA3')
styles.configure('lbl1.TLabel',
                 foreground='#00FF00', font=('Calibri', 18, 'normal'))

styles.configure('lbl2.TLabel',
                 foreground='#FFFF00', font=('Calibri', 18, 'normal'))

styles.configure('message.TLabel', width=50,
                 foreground='#3BFF00', font=('Calibri', 12, 'normal'))

# Contenedor secundario (Frame)
frm_username = Frame(root)
frm_username.pack(fill=X)

# Agregamos Widgets al Frame:
# Etiquetas
Label(frm_username, text='Usuario', style='lbl1.TLabel').pack(
    padx=10, pady=10, side=LEFT, anchor=NW)

# Cajas de texto
userName = StringVar()  # userName = ''
entry_username = Entry(frm_username, textvariable=userName, width=20, font=(
    'Calibri', 18, 'normal'))
entry_username.pack(padx=10, pady=10, side=LEFT, anchor=NW, expand=1, fill=X)

# Contenedor secundario (Frame)
frm_passwd = Frame(root)
frm_passwd.pack(fill=X)

Label(frm_passwd, text='Contraseña', style='lbl2.TLabel').pack(
    padx=10, pady=10, side=LEFT, anchor=SW)

userPasswd = StringVar()
entry_passwd = Entry(frm_passwd, textvariable=userPasswd, width=20, font=(
    'Calibri', 18, 'normal'))
entry_passwd.pack(padx=10, pady=10, side=LEFT, anchor=NW, expand=1, fill=X)

# Frame para botones
frm_buttons = Frame(root)
frm_buttons.pack(fill=X)

Button(frm_buttons, text='Acceder', command=loginCheck).pack(side=LEFT, expand=1)
Button(frm_buttons, text='Recuperar contraseña',
       command=loginCheck).pack(side=LEFT, expand=1)

lbl_message = Label(root, style='message.TLabel')
lbl_message.pack()

root.mainloop()
