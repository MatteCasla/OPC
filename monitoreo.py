import psutil

class Monitoreo:
    @staticmethod
    def obtener_cpu():
        return psutil.cpu_percent(interval=0.5)
    
    def cpu_cores():
        return psutil.cpu_count()

    @staticmethod
    def obtener_ram():
        return psutil.virtual_memory().percent

    @staticmethod
    def obtener_disc():
        return psutil.disk_usage('c://').percent