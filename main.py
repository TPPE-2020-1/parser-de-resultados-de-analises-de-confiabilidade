from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from Exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from Exceptions.FormatoSaidaArquivoInvalidoException import FormatoSaidaArquivoInvalidoException
from Exceptions.FormatoArquivoInvalidoException import FormatoArquivoInvalidoException


def read_input_file(input_file_name):
    try:
        input_file = open(input_file_name)
    except:
        raise ArquivoNaoEncontradoException(input_file_name)
    return input_file.read()


def delimiter_character(delimiter_symbol):
    if len(delimiter_symbol) == 1:
        return delimiter_symbol
    else:
        raise DelimitadorInvalidoException(delimiter_symbol)


def output_file(directory, file_name):
    try:
        file_list = file_name.split('.')
        name = file_list[0]
        extension = file_list[1]
        if name[-3:] != 'Tab':
            name += 'Tab'
        if directory[-1] != '/':
            directory += '/'
        output_file_name = f"{directory}{name}.out"
        output_file = open(output_file_name, "w")
        return output_file
    except:
        raise EscritaNaoPermitidaException(directory, file_name)


def file_format(file_format_option):
    expected_options = ['colunas', 'linhas', 'l', 'c']

    if file_format_option.lower() in expected_options:
        return file_format_option
    else:
        raise FormatoSaidaArquivoInvalidoException(file_format_option)


def parse_file_data(file_data: str) -> dict:
    import re

    parsed_data = {}

    regex = r'\-+\s.+\s\d+\s\-+\D(^\d+\D)+'

    if not re.search(regex, file_data, re.MULTILINE):
        raise FormatoArquivoInvalidoException()

    matches = re.finditer(regex, file_data, re.MULTILINE)

    for match in matches:
        pattern = r'-+\s.+\s(\d+)\s\-+'
        evolution = int(
            re.search(pattern, match.group(), re.MULTILINE).group(1))

        values = re.finditer(r'(^\d+)', match.group(), re.MULTILINE)

        parsed_data[evolution] = []

        for value in values:
            try:
                parsed_data[evolution].append(int(value.group()))
            except:
                raise FormatoArquivoInvalidoException()

        if not parsed_data[evolution]:
            raise FormatoArquivoInvalidoException()

    if not parsed_data:
        raise FormatoArquivoInvalidoException()

    return parsed_data


def main():
    file_path = input("Insert file path: ")
    file_data = read_input_file(file_path)

    delimiter_symbol = input("Insert delimiter symbol: ")
    delimiter_symbol = delimiter_character(delimiter_symbol)

    directory = input("Type output directory to be outputted: ")
    file = input("Type output file name: ")
    outputted_file = output_file(directory, file)

    output_format = input("Type output file format(linhas[l] | colunas[c]): ")
    output_format = file_format(output_format)

    parsed_data = parse_file_data(file_data)


if __name__ == "__main__":
    main()
