import tkinter as tk
from tkinter import ttk
class OPCGUI:
    def __init__(self, root):
        self.root = root
        self._apply_style()
        self._create_layout()


    # ESTILOS

    def _apply_style(self):
        style = ttk.Style()
        style.theme_use('clam')

        BG = "#1e1e1e"
        FG = "#e6e6e6"

        self.root.configure(bg=BG)

        style.configure(".", background=BG, foreground=FG)
        style.configure("OPC.TLabel", font=('Segoe UI', 10), background=BG, foreground=FG)
        style.configure("OPC.TButton", font=('Segoe UI', 10), background=BG, foreground=FG)
        style.map("OPC.TButton", background=[("active", "#3a3a3a")])

        style.configure("OPC.TCheckbutton", font=('Segoe UI', 10), background=BG, foreground=FG)
        style.map("OPC.TCheckbutton",
                  foreground=[('selected', FG), ('active', FG)],
                  background=[("selected", BG), ("active", BG)])

        style.configure("TNotebook", background=BG, borderwidth=0)
        style.configure("TNotebook.Tab",
                        background="#3a3a3a",
                        foreground="#e6e6e6",
                        padding=[10, 5])
        style.map("TNotebook.Tab",
                  background=[("selected", "#5a5a5a"),
                              ("active", "#4a4a4a")],
                  foreground=[("selected", "#ffffff"),
                              ("active", "#e6e6e6")])


    # LAYOUT

    def _create_layout(self):

        # Notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Frames
        self.frame_monitor = ttk.Frame(self.notebook)
        self.frame_logs = ttk.Frame(self.notebook)
        self.frame_eliminar_basura = ttk.Frame(self.notebook)
        self.frame_automatizacion = ttk.Frame(self.notebook)

        # Agregar pestañas
        self.notebook.add(self.frame_monitor, text='Inicio')
        self.notebook.add(self.frame_logs, text='Logs')
        self.notebook.add(self.frame_eliminar_basura, text='Limpieza')
        self.notebook.add(self.frame_automatizacion, text='Automatización')

        # Labels principales (SIN .pack() encadenado)
        self.label_monitor = ttk.Label(
            self.frame_monitor,
            text='Sector de monitoreo',
            style='OPC.TLabel',
            font=('Segoe UI', 16)
        )
        self.label_monitor.pack(pady=20)

        self.label_logs = ttk.Label(
            self.frame_logs,
            text='Sector de logs',
            style='OPC.TLabel',
            font=('Segoe UI', 16)
        )
        self.label_logs.pack(pady=20)

        self.label_eliminar_basura = ttk.Label(
            self.frame_eliminar_basura,
            text='Sector de eliminación de basura',
            style='OPC.TLabel',
            font=('Segoe UI', 16)
        )
        self.label_eliminar_basura.pack(pady=20)

        self.label_automatizacion = ttk.Label(
            self.frame_automatizacion,
            text='Sector de automatización',
            style='OPC.TLabel',
            font=('Segoe UI', 16)
        )
        self.label_automatizacion.pack(pady=20)


    # MÉTODOS PÚBLICOS

    def update_monitor(self, text):
        self.label_monitor.config(text=text)

    def update_logs(self, text):
        self.label_logs.config(text=text)

    def update_eliminar_basura(self, text):
        self.label_eliminar_basura.config(text=text)

    def update_automatizacion(self, text):
        self.label_automatizacion.config(text=text)

def opc_showinfo(root, BG, titulo, mensaje):
    win = tk.Toplevel(root)
    win.title(titulo)
    win.configure(bg=BG)
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()

    frame = ttk.Frame(win, style="OPC.TFrame", padding=15)
    frame.pack(fill="both", expand=True)

    lbl = ttk.Label(frame, text=mensaje, style="OPC.TLabel", justify="left")
    lbl.pack(pady=(0, 15))

    ttk.Button(frame, text="Aceptar", style="OPC.TButton", command=win.destroy).pack()

    win.wait_window()


def opc_askyesno(root, BG, titulo, mensaje):
    respuesta = {"valor": False}

    win = tk.Toplevel(root)
    win.title(titulo)
    win.configure(bg=BG)
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()

    frame = ttk.Frame(win, style="OPC.TFrame", padding=15)
    frame.pack(fill="both", expand=True)

    lbl = ttk.Label(
        frame, text=mensaje, style="OPC.TLabel",
        wraplength=350, justify="left"
    )
    lbl.pack(pady=(0, 15))

    botones = ttk.Frame(frame, style="OPC.TFrame")
    botones.pack()

    def aceptar():
        respuesta["valor"] = True
        win.destroy()

    def cancelar():
        win.destroy()

    ttk.Button(botones, text="Sí", style="OPC.TButton", command=aceptar).pack(side="left", padx=5)
    ttk.Button(botones, text="No", style="OPC.TButton", command=cancelar).pack(side="left", padx=5)

    win.wait_window()
    return respuesta["valor"]
