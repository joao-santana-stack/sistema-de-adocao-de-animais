# sistema-de-adocao-de-animais
um sistema de linha de comando para gerenciar: cadastro de animais, triagem de adotantes, reservas, adoções, devoluções, quarentena e relatórios. Com políticas configuráveis (ex.: idade mínima do adotante, tipo de moradia vs. porte do animal), lista de espera com prioridade, cálculo de taxa por estratégia (idade/porte/saúde) e persistência com repositórios.

# UML textual
Classe Animal (VacinavelMixin, AdestravelMixin):
  Atributos Principais:
    id: str
    nome: str
    especie: str
    raca: str
    sexo: str
    idade_meses: int
    porte: str (P, M, G)
    temperamento: List[str]
    status: StatusAnimal
    historico_eventos: List[str]
    data_entrada: datetime
  Métodos Principais:
    alterar_status(novo_status: StatusAnimal) -> None
    adicionar_evento(descricao: str) -> None
    __str__() -> str
    __repr__() -> str
    __eq__(other) -> bool
    __hash__() -> int
    __lt__(other) -> bool  (ordenação por data de entrada)
    __iter__() -> Iterator (iteração pelo histórico)
    
Enum StatusAnimal:
  Status:
    DISPONIVEL
    RESERVADO
    ADOTADO
    DEVOLVIDO
    QUARENTENA
    INADOTAVEL
  
Classe Cachorro (Herda de Animal):
  Atributos Específicos:
    necessidade_passeio: str (baixa, media, alta)

Classe Gato (Herda de Animal):
  Atributos Específicos:
    nivel_independencia: str (baixo, medio, alto)

Classe Pessoa (Abstrata/Base):
  Atributos:
    id: str
    nome: str
    idade: int

Classe Adotante (Herda de Pessoa):
  Atributos Específicos:
    moradia: str (casa/apto)
    area_util: float
    experiencia_pets: bool
    criancas_em_casa: bool
    outros_animais: bool
  Métodos Principais:
    e_elegivel(politicas: dict) -> bool

Classe Reserva:
  Atributos:
    id: str
    animal_id: str
    adotante_id: str
    data_reserva: datetime
    expirada: bool
  Métodos:
    esta_ativa() -> bool

Classe FilaEspera:
  Atributos:
    animal_id: str
    fila: List[Tuple[Adotante, float, datetime]] (adotante, pontuacao, data)
  Métodos:
    adicionar_adotante(adotante: Adotante, pontuacao: float) -> None
    proximo() -> Adotante
    __len__() -> int

========================Mixins===========================
Mixin VacinavelMixin:
  Atributos:
    historico_vacinas: List[dict]
  Métodos:
    vacinar(nome_vacina: str, data: str) -> None

Mixin AdestravelMixin:
  Atributos:
    nivel_adestramento: int
  Métodos:
    treinar(pontos: int) -> None

