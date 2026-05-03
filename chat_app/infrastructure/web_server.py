"""
Servidor web Flask — capa de Infraestructura HTTP.
Expone la UI en GET / y la API REST en POST /api/send-message.
También realiza la composición manual de dependencias (DI container).
"""

import os
from typing import Any

from flask import Flask, request, jsonify, render_template

from domain.models import ChatMessage
from domain.repositories import IChatRepository
from application.services import ChatService
from application.use_cases import SendMessageUseCase
from infrastructure.http_client import HttpClient
from config import Config

# Flask busca templates/ relativo al archivo donde se instancia la app.
# Como este archivo está en infrastructure/, se calcula el path hacia la raíz del proyecto.
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=os.path.join(_root, 'templates'))


class ChatRepository(IChatRepository):
    """
    Implementación concreta de IChatRepository que usa HttpClient.
    Adapta la interfaz del dominio al cliente HTTP de infraestructura.
    """

    def __init__(self, http_client: HttpClient) -> None:
        """
        Args:
            http_client: Cliente HTTP configurado para comunicarse con Ollama.
        """
        self.http_client = http_client

    def send_message(self, message: ChatMessage) -> Any:
        """
        Delega el envío al HttpClient y retorna la respuesta cruda de Ollama.

        Args:
            message: Entidad ChatMessage con el texto de la consulta.

        Returns:
            Dict JSON con la respuesta completa de Ollama.
        """
        return self.http_client.send_message(message)


# --- Composición de dependencias (DI manual) ---
# Orden de construcción: HttpClient → ChatRepository → ChatService → UseCase
http_client = HttpClient()
chat_repository = ChatRepository(http_client=http_client)
chat_service = ChatService(repository=chat_repository)
send_message_use_case = SendMessageUseCase(chat_service=chat_service)


@app.route('/')
def index():
    """Sirve la interfaz web de chat (templates/index.html)."""
    return render_template('index.html')


@app.route('/api/send-message', methods=['POST'])
def send_message():
    """
    Endpoint REST para enviar un mensaje a Andes Code.

    Body JSON esperado:
        { "message": "tu consulta aquí" }

    Respuesta exitosa (200):
        { "reply": "respuesta del asistente" }

    Respuesta de error (400):
        { "error": "El campo message es requerido" }
    """
    message_content = request.json.get('message', '')
    if not message_content:
        return jsonify({'error': 'El campo "message" es requerido'}), 400

    raw = send_message_use_case.execute(message_content)

    # Extrae solo el texto del asistente del JSON completo de Ollama
    # Estructura esperada: raw['message']['content']
    reply = raw.get('message', {}).get('content', str(raw))
    return jsonify({'reply': reply}), 200
