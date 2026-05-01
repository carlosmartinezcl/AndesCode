# Andes Code

Asistente de arquitectura de software senior que corre localmente en tu máquina, sin enviar código a servidores externos. Basado en `qwen2.5-coder:14b` con personalidad y reglas de arquitectura fijadas mediante un System Prompt.

**Reglas de oro que aplica automáticamente:**
- Patrones de diseño: Repository, Factory, DTOs
- Clean Architecture (Dominio → Aplicación → Infraestructura)
- Python con Type Hints, TypeScript con tipado estricto
- PostgreSQL con índices, constraints y tipos correctos
- Código documentado en español

---

## Requisitos

| Componente | Detalle |
|---|---|
| **GPU** | RTX 4070 (8 GB VRAM) o superior |
| **RAM** | 16 GB mínimo (el modelo carga ~9 GB) |
| **CPU** | i9 o equivalente (para mover pesos RAM → VRAM al inicio) |
| **OS** | Ubuntu 24.04 (o cualquier distro con soporte Ollama) |
| **Ollama** | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **Modelo base** | `ollama pull qwen2.5-coder:14b` |

---

## Instalación

### 1. Descargar el modelo base

```bash
ollama pull qwen2.5-coder:14b
```

### 2. Compilar el modelo personalizado

Desde la carpeta de este proyecto:

```bash
ollama create arquitecto-senior -f ArchitectModel
```

Esto registra el modelo `arquitecto-senior` en Ollama con temperatura baja (`0.2`) y contexto de 32k tokens.

### 3. Verificar que quedó instalado

```bash
ollama list
```

Deberías ver `arquitecto-senior` en la lista.

### 4. Configurar los alias (opcional pero recomendado)

Abre `~/.bashrc` y agrega al final:

```bash
# Andes Code — alias principal
alias andes='ollama run arquitecto-senior'

# Andes Code — pasar un archivo con una instrucción
andes-revisa() {
    cat "$1" | ollama run arquitecto-senior "$2"
}

# Andes Code — generar un archivo nuevo directamente
andes-crea() {
    echo "--- Andes Code está trabajando en $1 ---"
    ollama run arquitecto-senior "Carlos, genera SOLO el contenido del archivo $1 sin charlas previas ni bloques de markdown. Instrucción: $2" > "$1"
}
```

Recarga la configuración:

```bash
source ~/.bashrc
```

---

## Uso

### Modo interactivo (chat directo)

```bash
ollama run arquitecto-senior
# o con el alias:
andes
```

Escribe tus preguntas libremente. Para salir: `Ctrl + D` o `/exit`.

### One-liner (respuesta rápida)

```bash
andes "Andes, diseña un esquema de tablas para un blog en PostgreSQL siguiendo la 3ra forma normal."
```

### Pasar un archivo para revisión

```bash
# Revisar si cumple SOLID
andes-revisa src/models/user.py "Revisa este modelo y dime si cumple con SOLID."

# Revisar queries de base de datos
andes-revisa api.py "Optimiza las queries de Postgres en este archivo."
```

### Refactorizar y guardar el resultado

```bash
# Guardar en un archivo nuevo
cat auth.py | andes "Refactoriza este código usando el patrón Decorator para manejo de logs. Carlos." > auth_refactorizado.py

# Traducir a TypeScript
cat viejo_script.js | andes "Refactoriza este código a TypeScript usando interfaces y documenta en español." > nuevo_script.ts
```

### Crear un archivo desde cero

```bash
andes-crea "domain/models.py" "Crea la entidad Proyecto con Type Hints y patrón Repository."
andes-crea "database.ts" "Crea la conexión a PostgreSQL usando el patrón Singleton."
```

### Agregar contenido a un archivo existente

```bash
andes "Agrega una sección al final del README.md explicando cómo correr los tests con pytest. Carlos." >> README.md
```

---

## Estructura de proyecto recomendada

Cuando le pidas diseñar un backend, Andes Code seguirá esta estructura de **Arquitectura Hexagonal**:

```
src/
├── domain/            # Reglas de negocio puras (Entidades)
├── application/       # Casos de uso (Lógica de la aplicación)
├── infrastructure/    # Implementaciones técnicas
│   ├── persistence/   # Repositorios (SQLAlchemy o Prisma/TypeORM)
│   └── http/          # Controladores (FastAPI o Express/NestJS)
└── main.py            # Punto de entrada y composición (DI Container)
```

---

## Monitoreo de GPU

Mientras Andes Code genera código complejo, abre una terminal dividida y ejecuta:

```bash
watch -n 0.5 nvidia-smi
```

La primera respuesta puede tardar unos segundos mientras el i9 mueve los pesos del modelo de RAM a VRAM. Una vez cargado, la velocidad de escritura (tokens/segundo) será fluida.

---

## Advertencias

1. **Markdown Wrapper:** A veces el modelo envuelve el código en bloques ` ```python ... ``` `. Si usas `>` para guardar directamente, esos caracteres quedarán en el archivo y darán error de sintaxis. La función `andes-crea` ya instruye al modelo para evitarlo.

2. **Límite de contexto:** El modelo tiene 32k tokens de contexto. Evita pasar archivos de más de ~15k líneas para que la respuesta sea ágil.

3. **Git antes de sobrescribir:** Antes de dejar que Andes Code escriba sobre un archivo existente, asegúrate de tener un `git commit` hecho. Si algo sale mal, `git checkout` es tu salvavidas.

---
