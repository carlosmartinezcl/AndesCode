"""
Interfaces del dominio — contratos abstractos que definen qué operaciones
existen sin acoplarse a ninguna implementación concreta (Ollama, mock, etc.).
Siguiendo el principio de Inversión de Dependencias (SOLID - D).
"""

from abc import ABC, abstractmethod
from typing import Any

from .models import ChatMessage


class IChatRepository(ABC):
    """
    Contrato abstracto para enviar mensajes a un proveedor de chat.
    Cualquier implementación (Ollama, OpenAI, mock para tests) debe heredar de esta clase.
    """

    @abstractmethod
    def send_message(self, message: ChatMessage) -> Any:
        """
        Envía un mensaje y retorna la respuesta del proveedor.

        Args:
            message: Entidad ChatMessage con el texto de la consulta.

        Returns:
            Respuesta cruda del proveedor (dict JSON).
        """
        pass
