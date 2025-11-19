import subprocess
import datetime
import os

def run_scan():
    print("=== Scanner Red Team ===")

    targets_input = input("Ingresa las IPs que deseas escanear (separadas por comas): ").strip()

    targets = [t.strip() for t in targets_input.split(",") if t.strip()]

    if not targets:
        print("No ingresaste ninguna IP. Terminando programa.")
        return

    output_dir = "red_team/results"
    os.makedirs(output_dir, exist_ok=True)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"scan_results_{date_str}.txt")

    print(f"\nGuardando resultados en: {output_file}\n")
    print("Iniciando escaneo...\n")

    with open(output_file, "w") as f:
        f.write("===== RESULTADOS DEL ESCANEO (RED TEAM) =====\n")
        f.write(f"Fecha: {date_str}\n")
        f.write("Flags usados: -sS -sV -Pn\n\n")

        for target in targets:
            f.write(f"\n--- Escaneando {target} ---\n")

            command = ["nmap", "-sS", "-sV", "-Pn", target]

            try:
                result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
                f.write(result)
            except subprocess.CalledProcessError as e:
                f.write(f"Error al escanear {target}:\n{e.output}\n")

    print("Escaneo completado. Archivo guardado correctamente.")
    print(f"\n✔ Escaneo terminado. Revisa: {output_file}\n")


if __name__ == "__main__":
    run_scan()
