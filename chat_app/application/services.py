"""
Capa de Aplicación — servicios que orquestan la lógica de negocio.
No contienen lógica de acceso a datos; delegan al repositorio inyectado.
"""

from typing import Any

from domain.models import ChatMessage
from domain.repositories import IChatRepository


class ChatService:
    """
    Servicio de chat que actúa como intermediario entre los casos de uso
    y el repositorio concreto.

    Recibe un IChatRepository por inyección de dependencias, lo que permite
    intercambiar la implementación real por un mock en tests sin cambiar este código.
    """

    def __init__(self, repository: IChatRepository) -> None:
        """
        Args:
            repository: Implementación concreta de IChatRepository
                        (ej: ChatRepository que usa HttpClient → Ollama).
        """
        self.repository = repository

    def send_message(self, message: ChatMessage) -> Any:
        """
        Delega el envío del mensaje al repositorio y retorna la respuesta.

        Args:
            message: Entidad ChatMessage con el texto de la consulta.

        Returns:
            Respuesta cruda del proveedor (dict JSON de Ollama).
        """
        return self.repository.send_message(message)
