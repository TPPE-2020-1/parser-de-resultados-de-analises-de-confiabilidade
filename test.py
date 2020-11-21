@pytest.mark.parametrize("input,expected", [('./utils/read_file_de.out', 'Datei gelesen'), ('./utils/read_file_en.out', 'File readed'), ('./utils/read_file_fr.out', 'Lecteur de fichiers'), ('./utils/read_file_pt.out', 'Arquivo lido')])
def test_read_input_file(input, expected):
    file = read_file(input)
    assert file == expected