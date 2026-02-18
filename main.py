import tkinter as tk
from tkinter import ttk
from grafico import OPCGUI, opc_askyesno, opc_showinfo
from monitoreo import Monitoreo
import os
import tempfile
from datetime import datetime
import time
import threading
import shutil
import subprocess


class OPCAplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('OPC - Monitoreo de sistema')
        self.root.geometry('400x300')

        self.gui = OPCGUI(self.root)    
    def run(self):
        self.root.mainloop()
opc = OPCAplicacion()
BG = "#1e1e1e"
FG = "#e6e6e6"

# MONITOREO (LABELS Y ACTUALIZACIONES DE DATOS)

label_cpu_percent = ttk.Label(opc.gui.frame_monitor, text='CPU: --%' ,style='OPC.TLabel')
label_cpu_percent.pack()
label_ram_percent = ttk.Label(opc.gui.frame_monitor, text='RAM: --%', style='OPC.TLabel')
label_ram_percent.pack()
label_disc_percent = ttk.Label(opc.gui.frame_monitor, text='DISC: --%', style='OPC.TLabel')
label_disc_percent.pack()

        # ACTUALIZA DATOS

def actualizar_labels_recursos():
    label_cpu_percent.config(text=f'CPU: {Monitoreo.obtener_cpu()}%', foreground='#ffa500' if Monitoreo.obtener_cpu()>65 else FG)
    label_ram_percent.config(text=f'RAM: {Monitoreo.obtener_ram()}%', foreground='#ffa500' if Monitoreo.obtener_ram()>65 else FG)
    label_disc_percent.config(text=f'DISC: {Monitoreo.obtener_disc()}%', foreground='#ffa500' if Monitoreo.obtener_disc()>65 else FG)
    opc.root.after(1000, actualizar_labels_recursos)
actualizar_labels_recursos()

opc.run() 