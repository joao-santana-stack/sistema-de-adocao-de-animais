"""Estratégias de cálculo de taxa de adoção (Padrão Strategy)."""

from abc import ABC, abstractmethod
from src.models import Animal


class BaseFeeStrategy(ABC):
    """Estratégia base para cálculo da taxa de adoção."""

    @abstractmethod
    def calcular_taxa(self, animal: Animal) -> float:
        """Calcula o valor final da taxa de adoção."""
        pass


class SeniorFeeStrategy(BaseFeeStrategy):
    """Aplica desconto para animais idosos."""

    def calcular_taxa(self, animal: Animal) -> float:
        """Retorna a taxa com desconto sênior."""
        pass


class PuppyFeeStrategy(BaseFeeStrategy):
    """Aplica taxa diferenciada para cobrir custos de vacinas de filhotes."""

    def calcular_taxa(self, animal: Animal) -> float:
        """Retorna a taxa estipulada para filhotes."""
        pass


class SpecialCareFeeStrategy(BaseFeeStrategy):
    """Aplica taxa cobrindo custos para animais com necessidades especiais."""

    def calcular_taxa(self, animal: Animal) -> float:
        """Retorna a taxa para tratamentos especiais."""
        pass