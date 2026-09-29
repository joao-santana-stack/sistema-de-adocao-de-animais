"""Modelos de domínio do sistema de adoção de animais."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Iterator
from datetime import datetime

from src.mixins import VacinavelMixin, AdestravelMixin


class StatusAnimal(Enum):
    """Enumeração dos status possíveis de um animal no abrigo."""
    DISPONIVEL = "DISPONIVEL"
    RESERVADO = "RESERVADO"
    ADOTADO = "ADOTADO"
    DEVOLVIDO = "DEVOLVIDO"
    QUARENTENA = "QUARENTENA"
    INADOTAVEL = "INADOTAVEL"


class Animal(ABC, VacinavelMixin, AdestravelMixin):
    """Classe abstrata base que representa um animal no sistema."""

    def __init__(
        self,
        animal_id: str,
        nome: str,
        especie: str,
        raca: str,
        sexo: str,
        idade_meses: int,
        porte: str,
        temperamento: List[str],
        status: StatusAnimal = StatusAnimal.DISPONIVEL,
    ) -> None:
        super().__init__()
        self._id = animal_id
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._sexo = sexo
        self._idade_meses = idade_meses
        self._porte = porte
        self._temperamento = temperamento
        self._status = status
        self._historico_eventos: List[str] = []
        self._data_entrada = datetime.now()

    @property
    def idade_meses(self) -> int:
        """Retorna a idade do animal em meses."""
        return self._idade_meses

    @idade_meses.setter
    def idade_meses(self, valor: int) -> None:
        """Define a idade em meses garantindo que seja não-negativa."""
        pass

    @property
    def porte(self) -> str:
        """Retorna o porte do animal (P, M, G)."""
        return self._porte

    @porte.setter
    def porte(self, valor: str) -> None:
        """Define o porte validando os valores permitidos (P, M, G)."""
        pass

    def alterar_status(self, novo_status: StatusAnimal) -> None:
        """Altera o status do animal validando transições permitidas."""
        pass

    def adicionar_evento(self, descricao: str) -> None:
        """Adiciona um registro ao histórico de eventos do animal."""
        pass

    def __str__(self) -> str:
        """Retorna representação textual amigável do animal."""
        return f"{self._nome} ({self._especie}) - Status: {self._status.value}"

    def __repr__(self) -> str:
        """Retorna representação detalhada para depuração."""
        return f"Animal(id={self._id!r}, nome={self._nome!r}, status={self._status.value!r})"

    def __eq__(self, other: object) -> bool:
        """Verifica igualdade baseada no ID único do animal."""
        if not isinstance(other, Animal):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        """Retorna o hash único do objeto baseado no ID."""
        return hash(self._id)

    def __lt__(self, other: "Animal") -> bool:
        """Permite ordenação de animais pela data de entrada."""
        return self._data_entrada < other._data_entrada

    def __iter__(self) -> Iterator[str]:
        """Permite iterar sobre o histórico de eventos do animal."""
        return iter(self._historico_eventos)


class Cachorro(Animal):
    """Classe que representa um cachorro no sistema."""

    def __init__(
        self,
        animal_id: str,
        nome: str,
        raca: str,
        sexo: str,
        idade_meses: int,
        porte: str,
        temperamento: List[str],
        necessidade_passeio: str = "media",
    ) -> None:
        super().__init__(
            animal_id=animal_id,
            nome=nome,
            especie="Cachorro",
            raca=raca,
            sexo=sexo,
            idade_meses=idade_meses,
            porte=porte,
            temperamento=temperamento,
        )
        self.necessidade_passeio = necessidade_passeio


class Gato(Animal):
    """Classe que representa um gato no sistema."""

    def __init__(
        self,
        animal_id: str,
        nome: str,
        raca: str,
        sexo: str,
        idade_meses: int,
        porte: str,
        temperamento: List[str],
        nivel_independencia: str = "medio",
    ) -> None:
        super().__init__(
            animal_id=animal_id,
            nome=nome,
            especie="Gato",
            raca=raca,
            sexo=sexo,
            idade_meses=idade_meses,
            porte=porte,
            temperamento=temperamento,
        )
        self.nivel_independencia = nivel_independencia


class Pessoa(ABC):
    """Classe abstrata base que representa uma pessoa no sistema."""

    def __init__(self, pessoa_id: str, nome: str, idade: int) -> None:
        self._id = pessoa_id
        self._nome = nome
        self._idade = idade


class Adotante(Pessoa):
    """Classe que representa um candidato a adotante."""

    def __init__(
        self,
        pessoa_id: str,
        nome: str,
        idade: int,
        moradia: str,
        area_util: float,
        experiencia_pets: bool,
        criancas_em_casa: bool,
        outros_animais: bool,
    ) -> None:
        super().__init__(pessoa_id, nome, idade)
        self._moradia = moradia
        self._area_util = area_util
        self.experiencia_pets = experiencia_pets
        self.criancas_em_casa = criancas_em_casa
        self.outros_animais = outros_animais


class FilaEspera:
    """Gerencia a fila com prioridade para a adoção de um determinado animal."""

    def __init__(self, animal_id: str) -> None:
        self.animal_id = animal_id
        self._fila: List[tuple] = []

    def adicionar_adotante(self, adotante: Adotante, pontuacao: float) -> None:
        """Adiciona um adotante à fila mantendo a ordenação por pontuação."""
        pass

    def proximo(self) -> Optional[Adotante]:
        """Retorna e remove o próximo adotante com maior prioridade."""
        pass

    def __len__(self) -> int:
        """Retorna o número de adotantes aguardando na fila."""
        return len(self._fila)