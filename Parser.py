from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from Exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException
from Exceptions.FormatoSaidaArquivoInvalidoException import FormatoSaidaArquivoInvalidoException
from Exceptions.FormatoArquivoInvalidoException import FormatoArquivoInvalidoException


class Parser:
    def read_input_file(self, input_file_name):
        try:
            input_file = open(input_file_name)
        except:
            raise ArquivoNaoEncontradoException(input_file_name)
        return input_file.read()

    def delimiter_character(self, delimiter_symbol):
        if len(delimiter_symbol) == 1:
            return delimiter_symbol
        else:
            raise DelimitadorInvalidoException(delimiter_symbol)

    def output_file(self, directory, file_name):
        try:
            file_list = file_name.split('.')

            name = file_list[0]
            extension = file_list[1]

            if directory[-1] != '/':
                directory += '/'

            output_file_name = f"{directory}{name}Tab.{extension}"

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
        if output_format in ['linhas', 'l']:
            for evolution, times in parsed_data.items():
                partial = f"{delimiter_symbol}".join(times)
                line = f"{evolution}{delimiter_symbol}{partial}"
                outputted_file.write(line + '\n')

            outputted_file.close()
            return

        max_times_size = 0
        for i, evolution in enumerate(parsed_data.keys()):
            outputted_file.write(
                str(evolution) + (delimiter_symbol if i < len(parsed_data.keys()) - 1 else '\n'))

            current_times_size = len(parsed_data[evolution])
            if current_times_size > max_times_size:
                max_times_size = current_times_size

        i = 0
        for idx in range(0, max_times_size):
            for evolution in parsed_data.keys():
                try:
                    outputted_file.write(
                        (delimiter_symbol if i != 0 else '') + str(parsed_data[evolution][idx]))
                except:
                    outputted_file.write(
                        (f"{delimiter_symbol}NaN" if i != 0 and i + 1 != len(parsed_data.keys()) else ''))

                i += 1

            outputted_file.write('\n')

            i = 0

        outputted_file.close()
        return
