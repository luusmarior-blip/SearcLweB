import socket
import requests
import os
import time

# ---------------- UTILIDADES ----------------
def limpiar():
    os.system("clear")

def banner():
    print(r"""
   ███████╗███████╗ █████╗ ██████╗  ██████╗██╗     ██╗    ██╗███████╗██████╗
   ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║     ██║    ██║██╔════╝██╔══██╗
   ███████╗█████╗  ███████║██████╔╝██║     ██║     ██║ █╗ ██║█████╗  ██████╔╝
   ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██║     ██║███╗██║██╔══╝  ██╔══██╗
   ███████║███████╗██║  ██║██║  ██║╚██████╗███████╗╚███╔███╔╝███████╗██████╔╝
   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═════╝
                Security lu!s Web | OSINT Tool
                         仇 (noname)
    """)

def obtener_ip(dominio):
    try:
        return socket.gethostbyname(dominio)
    except:
        return "No disponible"

# ---------------- TECNOLOGÍAS ----------------
def detectar_tecnologias(dominio):
    tecnologias = []

    try:
        r = requests.get("http://" + dominio, timeout=5)
        headers = r.headers
        html = r.text.lower()

        if "server" in headers:
            tecnologias.append(f"Servidor: {headers['server']}")

        if "x-powered-by" in headers:
            tecnologias.append(f"Backend: {headers['x-powered-by']}")

        if "wp-content" in html:
            tecnologias.append("CMS: WordPress")
        if "joomla" in html:
            tecnologias.append("CMS: Joomla")
        if "drupal" in html:
            tecnologias.append("CMS: Drupal")

        if "cloudflare" in headers.get("server", "").lower():
            tecnologias.append("Protección: Cloudflare")

        if "bootstrap" in html:
            tecnologias.append("Frontend: Bootstrap")
        if "jquery" in html:
            tecnologias.append("Frontend: jQuery")

    except:
        tecnologias.append("No se pudo detectar tecnologías")

    return tecnologias

# ---------------- SUBDOMINIOS ----------------
def buscar_subdominios(dominio):
    subdominios_comunes = [
        "www", "mail", "ftp", "test", "dev",
        "api", "blog", "admin", "portal", "cpanel"
    ]

    encontrados = []

    for sub in subdominios_comunes:
        subdominio = f"{sub}.{dominio}"
        try:
            socket.gethostbyname(subdominio)
            encontrados.append(subdominio)
        except:
            pass

    return encontrados

# ---------------- PUERTOS ----------------
def escanear_puertos(dominio):
    puertos_comunes = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-ALT"
    }

    abiertos = []

    ip = obtener_ip(dominio)
    if ip == "No disponible":
        return abiertos

    for puerto, servicio in puertos_comunes.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            resultado = s.connect_ex((ip, puerto))
            if resultado == 0:
                abiertos.append(f"{puerto} ({servicio})")
            s.close()
        except:
            pass

    return abiertos

# ---------------- INFO COMPLETA ----------------
def analisis_completo(dominio):
    print("\n[+] Información general")
    print("Dominio:", dominio)
    print("IP:", obtener_ip(dominio))

    try:
        r = requests.get("http://" + dominio, timeout=5)
        print("Status Code:", r.status_code)
        print("HTTPS:", "Sí" if r.url.startswith("https") else "No")
    except:
        print("No se pudo conectar al sitio")

    print("\n[+] Tecnologías detectadas")
    for t in detectar_tecnologias(dominio):
        print("-", t)

    print("\n[+] Subdominios encontrados")
    subs = buscar_subdominios(dominio)
    if subs:
        for s in subs:
            print("-", s)
    else:
        print("No se encontraron")

    print("\n[+] Puertos abiertos (básico)")
    puertos = escanear_puertos(dominio)
    if puertos:
        for p in puertos:
            print("-", p)
    else:
        print("No se detectaron puertos abiertos comunes")

# ---------------- MENÚ ----------------
def menu():
    while True:
        print("""
========= MENÚ 恨み =========
[1] Análisis completo del dominio
[2] Detectar tecnologías
[3] Buscar subdominios
[4] Escanear puertos abiertos
[0] Salir
============================
        """)
        opcion = input("SearcLweB > ")

        if opcion == "1":
            d = input("Dominio (ej: example.com): ")
            analisis_completo(d)
        elif opcion == "2":
            d = input("Dominio: ")
            for t in detectar_tecnologias(d):
                print("-", t)
        elif opcion == "3":
            d = input("Dominio: ")
            subs = buscar_subdominios(d)
            for s in subs if subs else ["No encontrados"]:
                print("-", s)
        elif opcion == "4":
            d = input("Dominio: ")
            puertos = escanear_puertos(d)
            for p in puertos if puertos else ["Ninguno detectado"]:
                print("-", p)
        elif opcion == "0":
            print("\nSaliendo de SearcLweB | 恨み")
            break
        else:
            print("Opción inválida")

        input("\nENTER para continuar...")
        limpiar()
        banner()

# ---------------- MAIN ----------------
def main():
    limpiar()
    banner()
    menu()
    print("\nHecho por Lumarape")

if __name__ == "__main__":
    main()
