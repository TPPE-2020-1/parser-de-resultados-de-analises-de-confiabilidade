from src.Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from src.Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from src.Exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from src.Exceptions.FormatoSaidaArquivoInvalidoException import FormatoSaidaArquivoInvalidoException
from src.Exceptions.FormatoArquivoInvalidoException import FormatoArquivoInvalidoException

from src.ParseData import ParseData


class Parser:
    def read_input_file(self, input_file_name):
        try:
            input_file = open(input_file_name)

            return input_file.read()
        except:
            raise ArquivoNaoEncontradoException(input_file_name)

    def delimiter_character(self, delimiter_symbol):
        if len(delimiter_symbol) == 1:
            return delimiter_symbol
        else:
            raise DelimitadorInvalidoException(delimiter_symbol)

    def __get_output_filename(self, file_name, directory):
        file_list = file_name.split('.')

        name = file_list[0]
        extension = file_list[1]

        if directory[-1] != '/':
            directory += '/'

        return f"{directory}{name}Tab.{extension}"

    def output_file(self, directory, file_name):
        try:
            output_file_name = self.__get_output_filename(file_name, directory)

            output_file = open(output_file_name, "w")
            return output_file
        except:
            raise EscritaNaoPermitidaException(directory, file_name)

    def file_format(self, file_format_option):
        expected_options = ['colunas', 'linhas', 'l', 'c']

        if file_format_option.lower() in expected_options:
            return file_format_option
        else:
            raise FormatoSaidaArquivoInvalidoException(file_format_option)

    def parse_file_data(self, file_data: str) -> dict:
        import re

        parsed_data = {}

        regex = r'\-+\s.+\s\d+\s\-+\D(^\d+\D?)+'

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
                    parsed_data[evolution].append(str(value.group()))
                except:
                    raise FormatoArquivoInvalidoException()

            if not parsed_data[evolution]:
                raise FormatoArquivoInvalidoException()

        if not parsed_data:
            raise FormatoArquivoInvalidoException()

        return parsed_data

    def write_output_file(self, parsed_data, delimiter_symbol, outputted_file, output_format):
        parse_data = ParseData()

        options = {
            'linhas': parse_data.format_output_in_lines,
            'l': parse_data.format_output_in_lines,
            'colunas': parse_data.format_output_in_columns,
            'c': parse_data.format_output_in_columns
        }

        formatted_str = options[output_format](
            parsed_data, delimiter_symbol, output_format)

        outputted_file.write(formatted_str)

        return outputted_file.close()
