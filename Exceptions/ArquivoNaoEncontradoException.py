class ArquivoNaoEncontradoException(Exception):

    def __init__(self, file_name):
        self.filename = file_name
        
    def __str__(self):
        return f'Arquivo {self.filename} não encontrado.'