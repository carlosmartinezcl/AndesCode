"""
Modelos del dominio — representan entidades puras de negocio sin
dependencias de frameworks ni infraestructura.
"""

from dataclasses import dataclass


@dataclass
class ChatMessage:
    """
    Representa un mensaje enviado por el usuario al asistente.

    Attributes:
        content: Texto de la consulta o instrucción para Andes Code.
    """
    content: str
