# Protocolo para Andes Code

Andes Code es tu asistente de arquitectura de software senior. Puedes inter[5D[K
interactuar con él de varias formas:

1. **Modo Interactivo (Chat directo)**
   - Bash: `ollama run arquitecto-senior`
   - Una vez dentro, puedes escribir tus dudas.
   - Para salir, usa Ctrl + D o escribe `/exit`.

2. **Modo de Comando Único (One-liner)**
   - Ideal si solo quieres una respuesta rápida sin entrar al prompt intera[6D[K
interactivo:
     - Bash: `ollama run arquitecto-senior "Carlos, diseña un esquema de ta[2D[K
tablas para un blog en PostgreSQL siguiendo la 3ra forma normal."`

3. **Inyección de Contexto (Piping)**
   - Como estás trabajando en VS Code, puedes usar la terminal integrada pa[2D[K
para pasarle archivos de código a Andes Code.
   - Analizar un archivo de Python:
     - Bash: `cat src/models/user.py | ollama run arquitecto-senior "Andes [K
Code, revisa este modelo y dime si cumple con SOLID."`
   - Refactorizar un script completo:
     - Bash: `cat viejo_script.js | ollama run arquitecto-senior "Refactori[10D[K
"Refactoriza este código a TypeScript usando interfaces y documenta en espa[4D[K
español." > nuevo_script.ts`

4. **Automatización: El Alias de Arquitecto**
   - Para que no tengas que escribir comandos largos, vamos a crear un alia[4D[K
alias en tu `.bashrc`.
     - Abre tu configuración de Bash: `nano ~/.bashrc`
     - Ve al final del archivo y pega esto:
       ```bash
       # Alias para Andes Code (Arquitecto Senior)
       alias andes='ollama run arquitecto-senior'

       # Función para que Andes Code lea un archivo y una instrucción
       andes-revisa() {
           cat "$1" | ollama run arquitecto-senior "$2"
       }
       ```
     - Recarga la configuración: `source ~/.bashrc`
   - Ahora puedes usarlo así:
     - `andes "Hola, soy Carlos, necesito un DTO en Java Script"`
     - `andes-revisa api.py "Optimiza las queries de Postgres en este archi[5D[K
archivo"`

5. **Monitoreo de Rendimiento (Senior Tip)**
   - Mientras Andes Code genera código complejo (como el de 14B), abre una [K
terminal dividida en VS Code y lanza esto:
     - Bash: `watch -n 0.5 nvidia-smi`
   - Verás cómo los 8GB de tu RTX 4070 entran en acción. Si notas que la re[2D[K
respuesta tarda un poco al inicio, es normal: el i9 está moviendo los pesos[5D[K
pesos del modelo de la RAM a la VRAM. Una vez cargado, la velocidad de escr[4D[K
escritura (tokens por segundo) será excelente.

**Regla de Oro para Carlos:**
- Cuando le pases código por terminal mediante `cat`, asegúrate de que el a[1D[K
archivo no sea excesivamente gigante (más de 15k líneas), aunque configuram[10D[K
configuramos 32k de contexto, para que la respuesta sea ágil y no desborde [K
tu memoria.

### Crear archivos nuevos desde cero
- Si necesitas que Andes Code cree un archivo de instrucciones o un nuevo m[1D[K
módulo, usa el operador `>` (sobrescribir/crear).
  - Ejemplo: Crear un archivo de instrucciones Markdown
    - Bash: `andes "Andes Code, crea un archivo de instrucciones técnico en[2D[K
en Markdown para configurar el esquema de PostgreSQL de nuestro proyecto. C[1D[K
Carlos." > INSTRUCCIONES_DB.md`
  - Ejemplo: Crear un archivo de Python con arquitectura limpia
    - Bash: `andes "Crea el archivo domain/models.py con la entidad Proyect[7D[K
Proyecto usando Type Hints. Carlos." > domain/models.py`

### Editar o añadir contenido (Append)
- Si quieres agregar algo al final de un archivo existente sin borrar lo an[2D[K
anterior, usa `>>`.
  - Bash: `andes "Agrega una sección al final del README.md explicando cómo[4D[K
cómo correr los tests con pytest. Carlos." >> README.md`

### La técnica del "Arquitecto Revisor" (Lectura + Escritura)
- Esta es la más potente. Le pasas un archivo, le pides que lo mejore y gua[3D[K
guardas el resultado en un archivo nuevo (o el mismo).
  - Refactorizar y guardar:
    - Bash: `cat auth.py | andes "Andes Code, refactoriza este código usand[5D[K
usando el patrón Decorator para el manejo de logs. Carlos." > auth_refactor[13D[K
auth_refactorizado.py`

### Herramienta Senior: El script andes-save
- Para que no tengas que escribir redirecciones largas, vamos a mejorar tus[3D[K
tus alias en el `.bashrc`. Vamos a crear una función que limpie la salida ([1D[K
(por si el modelo añade texto extra) y guarde el código.
  - Añade esto a tu `~/.bashrc`:
    ```bash
    # Función para que Andes Code cree archivos directamente
    andes-crea() {
        # $1 es el nombre del archivo, $2 es la instrucción
        echo "--- Andes Code está trabajando en $1 ---"
        ollama run arquitecto-senior "Carlos, aquí tienes el código para $1[2D[K
$1. Genera SOLO el contenido del archivo sin charlas previas ni bloques de [K
markdown (sin http://googleusercontent.com/immersive_entry_chip/0)"
    }
    ```
  - Luego ejecuta `source ~/.bashrc`.
  
**Uso:**
- `andes-crea "database.ts" "Crea la conexión a PostgreSQL usando el patrón[6D[K
patrón Singleton"`

### Advertencias de Arquitecto (Best Practices)
1. **Cuidado con el "Markdown Wrapper":** A veces los modelos encierran el [K
código en bloques ```python ... ```. Si usas el redireccionamiento directo [K
(`>`), esos caracteres se guardarán en el archivo y darán error de sintaxis[8D[K
sintaxis. Por eso en la función de arriba le pedimos que genere **solo** el[2D[K
el contenido.
2. **Backups con Git:** Carlos, regla de oro: antes de dejar que una IA esc[3D[K
escriba sobre tus archivos, asegúrate de tener un `git commit` hecho. Si el[2D[K
el modelo se equivoca y sobrescribe algo importante, `git checkout` será tu[2D[K
tu salvavidas.
3. **Archivos `.md` de instrucciones:** Para esto Andes Code es brillante. [K
Puede generarte guías de despliegue, documentación de API o manuales de usu[3D[K
usuario en segundos.
