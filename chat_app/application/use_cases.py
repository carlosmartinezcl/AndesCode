"""
Casos de uso — representan acciones concretas del usuario sobre el sistema.
Cada caso de uso coordina entidades del dominio y servicios de aplicación.
"""

from typing import Any

from domain.models import ChatMessage
from application.services import ChatService


class SendMessageUseCase:
    """
    Caso de uso: el usuario envía un texto y recibe la respuesta de Andes Code.

    Es el punto de entrada para la lógica de negocio; no sabe nada de HTTP
    ni de Ollama, solo trabaja con entidades del dominio.
    """

    def __init__(self, chat_service: ChatService) -> None:
        """
        Args:
            chat_service: Servicio que gestiona el envío al proveedor de chat.
        """
        self.chat_service = chat_service

    def execute(self, message_content: str) -> Any:
        """
        Construye la entidad de dominio y la envía al servicio.

        Args:
            message_content: Texto plano ingresado por el usuario.

        Returns:
            Respuesta cruda del proveedor (dict JSON de Ollama).
        """
        # Convierte el string del usuario en una entidad del dominio
        message = ChatMessage(content=message_content)
        return self.chat_service.send_message(message)
