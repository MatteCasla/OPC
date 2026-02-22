import psutil
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