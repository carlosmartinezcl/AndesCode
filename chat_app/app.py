"""
Punto de entrada principal de la aplicación chat_app.

Importa la instancia Flask creada en infrastructure/web_server.py
y arranca el servidor en el host y puerto definidos en Config.

Uso:
    python app.py
"""

from infrastructure.web_server import app
from config import Config

if __name__ == '__main__':
    app.run(host=Config.SERVER_HOST, port=Config.SERVER_PORT, debug=True)
