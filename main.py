from os.path import basename

from src.Parser import Parser


def main():
    parser = Parser()
    file_path = input("Insert file path: ")
    file_data = parser.read_input_file(file_path)

    delimiter_symbol = input("Insert delimiter symbol: ")
    delimiter_symbol = parser.delimiter_character(delimiter_symbol)
    directory = input("Type output directory to be outputted: ")
    outputted_file = parser.output_file(directory, basename(file_path))

    output_format = input("Type output file format(linhas[l] | colunas[c]): ")
    output_format = parser.file_format(output_format)

    parsed_data = parser.parse_file_data(file_data)
    parser.write_output_file(
        parsed_data, delimiter_symbol, outputted_file, output_format)


if __name__ == "__main__":
    main()
