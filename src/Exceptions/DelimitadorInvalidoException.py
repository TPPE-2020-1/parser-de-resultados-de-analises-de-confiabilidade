class DelimitadorInvalidoException(Exception):
    def __init__(self, delimiter_symbol):
        self.delimiter_symbol = delimiter_symbol

    def __str__(self):
        return f'Delimitador {self.delimiter_symbol} não é válido.'