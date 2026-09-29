"""Exceções customizadas para o sistema de adoção de animais."""

class ReservaInvalidaError(Exception):
    """Lançada quando uma reserva não pode ser processada ou é inválida."""
    pass

class TransicaoDeEstadoInvalidaError(Exception):
    """Lançada ao tentar realizar uma transição de status não permitida no animal."""
    pass

class PoliticaNaoAtendidaError(Exception):
    """Lançada quando um adotante não atende aos requisitos mínimos de elegibilidade."""
    pass

class RepositorioError(Exception):
    """Lançada quando ocorre uma falha nas operações de persistência."""
    pass