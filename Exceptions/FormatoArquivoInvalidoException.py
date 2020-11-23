class FormatoArquivoInvalidoException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'O formato do arquivo não está padronizado com os exemplos de entrada.'
