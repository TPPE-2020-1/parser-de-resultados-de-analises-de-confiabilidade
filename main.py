from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException
from Exceptions.DelimitadorInvalidoException import DelimitadorInvalidoException
from Exceptions.EscritaNaoPermitidaException import EscritaNaoPermitidaException

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
        if directory[-1] != '/':
            directory += '/'
        output_file_name = f"{directory}{name}.out"
        output_file = open(output_file_name, "w")
        return output_file
    except:
        raise EscritaNaoPermitidaException(directory, file_name)

def main():
    file_path = input("Insert file path: ")
    file_data = read_input_file(file_path)
    delimiter_symbol = input("Insert delimiter symbol: ")
    delimiter_symbol = delimiter_character(delimiter_symbol)
    directory = input("Type output directory to be outputted: ")
    file = input("Type output file name: ")
    outputted_file = output_file(directory, file)
if __name__ == "__main__":
    main()