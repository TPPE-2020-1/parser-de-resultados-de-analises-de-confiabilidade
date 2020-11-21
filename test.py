import pytest
from main import (
    read_input_file,
    delimiter_character,
    output_file
)
from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from Exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException

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

#Test Definição do caminho do arquivo de saída.
@pytest.mark.parametrize("directory, file_name, expected", [('utils', 'output_test.out', 'utils/output_test.out'), ('./', 'other_output_test.out', './other_output_test.out')])
def test_output_file(directory, file_name, expected):
    assert output_file(directory, file_name).name == expected

@pytest.mark.parametrize("directory, file_name", [('unexistent_dir/outputs/', 'output_test'), ('../../', 'other_output_test')])
def test_invalid_output_file(directory, file_name):
    with pytest.raises(EscritaNaoPermitidaException):
        assert output_file(directory, file_name)