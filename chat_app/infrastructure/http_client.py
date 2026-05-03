"""
Cliente HTTP para comunicarse con la API de Ollama.
Pertenece a la capa de Infraestructura: es el único lugar del proyecto
que conoce el formato exacto de la API de Ollama.
"""

from typing import Any

import requests

from domain.models import ChatMessage
from config import Config


class HttpClient:
    """
    Implementa la comunicación HTTP con el endpoint /api/chat de Ollama.

    Ollama espera un payload con esta estructura:
        {
            "model": "arquitecto-senior",
            "messages": [{"role": "user", "content": "..."}],
            "stream": false
        }

    Y responde con:
        {
            "model": "...",
            "message": {"role": "assistant", "content": "..."},
            ...
        }
    """

    def __init__(self, base_url: str = Config.OLLAMA_URL) -> None:
        """
        Args:
            base_url: URL del endpoint de Ollama. Por defecto usa Config.OLLAMA_URL.
                      Se puede sobreescribir en tests para apuntar a un mock.
        """
        self.base_url = base_url

    def send_message(self, message: ChatMessage) -> Any:
        """
        Envía el mensaje a Ollama y retorna el JSON de respuesta completo.

        Args:
            message: Entidad ChatMessage con el texto de la consulta.

        Returns:
            Dict con la respuesta de Ollama. El texto del asistente
            se encuentra en response['message']['content'].

        Raises:
            requests.HTTPError: Si Ollama responde con un código de error HTTP.
            requests.ConnectionError: Si Ollama no está corriendo.
        """
        payload = {
            'model': Config.OLLAMA_MODEL,
            # Ollama espera una lista de mensajes con rol y contenido
            'messages': [{'role': 'user', 'content': message.content}],
            # stream=False para recibir toda la respuesta de una vez (no token a token)
            'stream': False,
        }
        response = requests.post(
            self.base_url,
            json=payload,
            headers={'Content-Type': 'application/json; charset=utf-8'},
        )
        # Lanza excepción si el status HTTP es 4xx o 5xx
        response.raise_for_status()
        return response.json()
