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
import psutil

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

RUTA_BASE = os.path.join(os.path.expanduser("~"), "Desktop", "OPC")
RUTA_LOGS = os.path.join(RUTA_BASE, "LOGS")
RUTA_PROCESOS = os.path.join(RUTA_LOGS, 'LOGS PROCESOS')
RUTA_TEMP = tempfile.gettempdir()

# Historial de actividad.

def loggear_actividad(origen, actividad):
    momento_actividad = []
    hora_log = datetime.now().strftime("%H:%M:%S")
    entrada = f'{hora_log} | ({origen}) -> {actividad}'
    momento_actividad.append(entrada)
    nombre_archivo="historial.log"
    ruta_archivo = os.path.join(RUTA_LOGS, nombre_archivo)
    os.makedirs(RUTA_LOGS, exist_ok=True)
    with open(ruta_archivo, "a") as f:
        for entrada in momento_actividad:
            f.write(entrada + "\n")

# GENERACION DE LOGS Y SU CLASIFICACION.

def logeo_procesos():
    momento = loggear_actividad('Usuario', 'Logeo de procesos')
    procesos = []
    momento = datetime.now()
    timestamp = momento.strftime("%Y-%m-%d_%H-%M-%S")
    log_procesos = f'Procesos_{timestamp}.txt'

    ruta_archivo = os.path.join(RUTA_PROCESOS, log_procesos)
    os.makedirs(RUTA_PROCESOS, exist_ok=True)

    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        for p in psutil.process_iter():
            try:
                p.cpu_percent(interval=None)  
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
            try:
                name = p.info['name']
                if name != "System Idle Process":
                    procesos.append(p.info)
            except Exception as e:
                print('Error', e)

        procesos.sort(key=lambda p: p['cpu_percent'], reverse=True)
        for p in procesos:
            f.write(f"PID: {p['pid']:<8} | Name: {p['name'][:29]:<30} | CPU: {p['cpu_percent'] / psutil.cpu_count():<10.2f}% | RAM: {p['memory_percent']:<10.2f}%\n")
def generar_log_procesos_thread():
    threading.Thread(target=logeo_procesos, daemon=True).start()

ttk.Button(opc.gui.frame_logs, text='Generar log', command=generar_log_procesos_thread, style='OPC.TButton').pack()
opc.run() 