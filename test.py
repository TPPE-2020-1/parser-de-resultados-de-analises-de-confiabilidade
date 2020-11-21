import pytest
from main import (
    read_input_file,
    delimiter_character
)
from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException

#Test Leitura do arquivo de entrada
@pytest.mark.parametrize("input_file,expected", [('./utils/read_file_de.out', 'Datei gelesen'), ('./utils/read_file_en.out', 'File readed'), ('./utils/read_file_fr.out', 'Lecteur de fichiers'), ('./utils/read_file_pt.out', 'Arquivo lido')])
def test_read_input_file(input_file, expected):
    file = read_input_file(input_file)
    assert file == expected

@pytest.mark.parametrize("input_file", [('./utils/read_file_es.out'), ('./test_utils/read_file_en.out')])
def test_read_input_file_not_found(input_file):
    with pytest.raises(ArquivoNaoEncontradoException):
        assert read_input_file(input_file)

#Test Definição do delimitador de campo
@pytest.mark.parametrize("input_file,expected", [ (';', ';'), ('\t', '\t'), ('\n', '\n'), ('\r', '\r')])
def test_delimiter_character(input_file, expected):
    assert delimiter_character(input_file) == expected
    
@pytest.mark.parametrize("input_file", [('Trennzeichen Beispiel'), ('Exemple de délimiteur'), ('Delimiter Example'), ('Exemplo de delimitador')])
def test_invalid_delimiter_character(input_file):
    with pytest.raises(DelimitadorInvalidoException):
        assert delimiter_character(input_file)