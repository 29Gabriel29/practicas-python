import shutil
import os
import sys

def obtener_metricas_disco(ruta):
    """Calcula las métricas de disco y devuelve un diccionario."""
    try:
        total, usado, libre = shutil.disk_usage(ruta)
        porcentaje = (usado / total) * 100
        gb = 1024 ** 3
        
        return {
            "total": total / gb,
            "usado": usado / gb,
            "libre": libre / gb,
            "porcentaje": porcentaje
        }
    except FileNotFoundError:
        return None

def monitor_disco(ruta="C:/", umbral_alerta=80):
    """Muestra el estado del disco y lanza una alerta si supera el umbral."""
    metricas = obtener_metricas_disco(ruta)
    
    if not metricas:
        print(f"Error: La ruta '{ruta}' no es válida o no se puede acceder.")
        return

    print("-" * 30)
    print(f"SISTEMA DE MONITOREO: {ruta}")
    print("-" * 30)
    print(f"Total:      {metricas['total']:>8.2f} GB")
    print(f"Usado:      {metricas['usado']:>8.2f} GB")
    print(f"Libre:      {metricas['libre']:>8.2f} GB")
    print(f"Capacidad:  [{metricas['porcentaje']:.2f}%]")
    
    # Lógica de Alerta
    if metricas['porcentaje'] >= umbral_alerta:
        print("\n[!] ALERTA: El uso de disco ha superado el límite de seguridad (capacidad => 80).")
    else:
        print("\n[OK] El estado del disco es saludable.")
    print("-" * 30)

if __name__ == "__main__":
    # Detectamos el sistema operativo para asignar una ruta por defecto inteligente
    ruta_defecto = "C:/" if sys.platform == "win32" else "/"
    monitor_disco(ruta_defecto, umbral_alerta=90)