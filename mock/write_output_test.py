from file_data_test import file_data_mock1

output_file_mock1 = {
    'parsed_data': file_data_mock1['parsed_data'],
    'delimiter_symbol': ';',
    'outputted_file': '../utils/out/outputted_mock1.txt',
    'output_format': 'linhas',
    'expected_file': '../utils/out/expected_mock1.txt'
}

output_file_mock2 = {
    'parsed_data': file_data_mock1['parsed_data'],
    'delimiter_symbol': ';',
    'outputted_file': '../utils/out/outputted_mock2.txt',
    'output_format': 'colunas',
    'expected_file': '../utils/out/expected_mock2.txt'
}
