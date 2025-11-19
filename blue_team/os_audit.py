#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime

OUTPUT_FILE = "log_events.txt"

def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError:
        return "Error ejecutando comando: " + cmd

def main():
    with open(OUTPUT_FILE, "w") as f:
        f.write(" Revisión del sistema\n")
        f.write(f"Fecha: {datetime.now()}\n\n")

        f.write("Usuarios: \n")
        users = run_cmd("cat /etc/passwd")
        f.write(users + "\n\n")

        f.write("Puertos abiertos: \n")
        ports = run_cmd("ss -tulnp")
        f.write(ports + "\n\n")

        f.write("Servicios activos:\n")
        services = run_cmd("systemctl --type=service --state=running")
        f.write(services + "\n\n")

    print(f"Completado. Archivo guardado en {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
