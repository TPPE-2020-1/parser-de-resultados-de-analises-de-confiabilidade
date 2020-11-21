class EscritaNaoPermitidaException(Exception):
    def __init__(self, directory, file_name):
        self.directory = directory
        self.file_name = file_name
        
    def __str__(self):
        return f'O arquivo {self.file_name} não pode ser criado no diretório {self.directory}.'