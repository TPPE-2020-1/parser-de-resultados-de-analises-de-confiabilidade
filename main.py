
from Exceptions.ArquivoNaoEncontradoException import ArquivoNaoEncontradoException

def read_input_file(input_file_name):
    try:
        input_file = open(input_file_name)
    except:
        raise ArquivoNaoEncontradoException(input_file_name)
    return input_file.read()

def main():
    file_path = input("Insert file path: ") 
    file_data = read_input_file(file_path)

if __name__ == "__main__":
    main()