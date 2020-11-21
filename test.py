import pytest
from main import read_input_file
from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

@pytest.mark.parametrize("input,expected", [('./utils/read_file_de.out', 'Datei gelesen'), ('./utils/read_file_en.out', 'File readed'), ('./utils/read_file_fr.out', 'Lecteur de fichiers'), ('./utils/read_file_pt.out', 'Arquivo lido')])
def test_read_input_file(input, expected):
    file = read_input_file(input)
    assert file == expected

@pytest.mark.parametrize("input", [('./utils/read_file_es.out'), ('./test_utils/read_file_en.out')])
def test_read_input_file_not_found(input, expected):
    with pytest.raises(ArquivoNaoEncontradoException):
        assert read_input_file(input)