from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException

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

def main():
    file_path = input("Insert file path: ")
    file_data = read_input_file(file_path)
    delimiter_symbol = input("Insert delimiter symbol: ")
    delimiter_symbol = delimiter_character(delimiter_symbol)

if __name__ == "__main__":
    main()