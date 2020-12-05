from src.mock.file_data_test import file_data_mock1, file_data_mock2

output_file_mock1 = {
    'parsed_data': file_data_mock1['parsed_data'],
    'delimiter_symbol': ';',
    'output_file': './src/utils/out/outputted_mock1.txt',
    'output_format': 'linhas',
    'expected_file': './src/utils/out/expected_mock1.txt'
}

output_file_mock2 = {
    'parsed_data': file_data_mock2['parsed_data'],
    'delimiter_symbol': ';',
    'output_file': './src/utils/out/outputted_mock2.txt',
    'output_format': 'colunas',
    'expected_file': './src/utils/out/expected_mock2.txt'
}
