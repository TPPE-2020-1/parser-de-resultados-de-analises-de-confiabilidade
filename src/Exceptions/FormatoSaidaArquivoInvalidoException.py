class FormatoSaidaArquivoInvalidoException(Exception):
    def __init__(self, file_format_option):
        self.file_format_option = file_format_option

    def __str__(self):
        return f'Opção {self.file_format_option} não é válida.'
