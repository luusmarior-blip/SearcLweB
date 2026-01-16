
# 🔐 SearcLweB 

**SearcLweB** (Security Luis Web) es una herramienta **OSINT** desarrollada en **Python 3** para el reconocimiento web pasivo y legal.

El nombre incorpora la palabra japonesa **恨み (Urami)**, que significa *rencor*, como identidad simbólica del proyecto.

---

## 🚀 Funcionalidades

- 🌐 Obtención de información general del dominio
- 🧠 Detección de tecnologías web (servidor, CMS, backend, frontend)
- 🧩 Búsqueda básica de subdominios comunes
- 🔍 Escaneo básico de puertos abiertos (no intrusivo)
- 📋 Menú interactivo en terminal
- 🎨 Banner ASCII personalizado

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Librería `requests`
- Módulos estándar (`socket`, `os`, `time`)

---

## 📦 Instalación

### 1️⃣ Clonar el repositorio
```bash s
### 🔹 Requisitos previos
- Python **3.8 o superior**
- Conexión a internet
- Git (opcional)

---

### 🔹 Opción 1: Instalación desde GitHub (recomendada)

1️⃣ Clonar el repositorio:
```bash
git clone https://github.com/luusmarior-blip/SearcLweB.git
cd SearcLweB
````

2️⃣ Instalar dependencias:

```bash
pip install -r requirements.txt
```

3️⃣ Ejecutar la herramienta:

```bash
python searclweb.py
```

---

### 🔹 Opción 2: Descarga directa desde GitHub (sin Git)

1️⃣ Entrar a:
[https://github.com/luusmarior-blip/SearcLweB](https://github.com/luusmarior-blip/SearcLweB)

2️⃣ Clic en **Code → Download ZIP**
3️⃣ Extraer el archivo ZIP
4️⃣ Abrir una terminal dentro de la carpeta extraída

5️⃣ Instalar dependencias:

```bash
pip install -r requirements.txt
```

6️⃣ Ejecutar la herramienta:

```bash
python searclweb.py
```

---

### 🔹 Opción 3: Linux / Kali Linux

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
python3 searclweb.py
```

---

## 🛠️ Problemas comunes

### ❌ Error: `No module named requests`

Solución:

```bash
python -m pip install requests
```

---

### ❌ El comando `python` no funciona

Prueba:

```bash
python3 searclweb.py
```

---

## ✅ Verificación de instalación

Si al ejecutar aparece el banner:

```
Security Luis Web | OSINT Tool
恨み (URAMI)
```

👉 La instalación fue **exitosa**.
