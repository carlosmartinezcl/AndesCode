"""
Configuración centralizada de la aplicación.
Todos los parámetros de conexión se modifican aquí para evitar valores
hardcodeados dispersos en el código.
"""


class Config:
    """Parámetros de configuración para el servidor Flask y la conexión con Ollama."""

    # Dirección donde Flask escucha (localhost = solo acceso local)
    SERVER_HOST = 'localhost'

    # Puerto HTTP del servidor web
    SERVER_PORT = 5000

    # Endpoint de la API de chat de Ollama (debe estar corriendo localmente)
    OLLAMA_URL = 'http://localhost:11434/api/chat'

    # Nombre del modelo compilado con `ollama create arquitecto-senior -f ArchitectModel`
    OLLAMA_MODEL = 'arquitecto-senior'
