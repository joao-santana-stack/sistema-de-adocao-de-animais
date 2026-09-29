"""Mixins para herança múltipla e composição de comportamentos específicos."""

from typing import List, Dict

class VacinavelMixin:
    """Mixin que adiciona capacidades de vacinação e histórico de vacinas."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.historico_vacinas: List[Dict[str, str]] = []

    def vacinar(self, nome_vacina: str, data: str) -> None:
        """Registra a aplicação de uma vacina no histórico."""
        pass


class AdestravelMixin:
    """Mixin que adiciona capacidades de treino e nível de adestramento."""
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.nivel_adestramento: int = 0

    def treinar(self, pontos: int) -> None:
        """Aumenta o nível de adestramento com base nos pontos fornecidos."""
        pass