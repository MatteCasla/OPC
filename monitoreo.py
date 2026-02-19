import psutil

class Monitoreo:
    @staticmethod
    def obtener_cpu():
        return psutil.cpu_percent(interval=None)
    
    @staticmethod
    def obtener_ram():
        return psutil.virtual_memory().percent

    @staticmethod
    def obtener_disc():
        return psutil.disk_usage('c://').percent

class Procesos:
    @staticmethod
    def obtener_procesos(attrs=None):
        if attrs is None:
            attrs = ['pid', 'name', 'memory_percent', 'cpu_percent']

        procesos = []
        for p in psutil.process_iter(attrs):
            try:
                procesos.append(p.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return procesos