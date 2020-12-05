class Persistencia:
    def __get_output_filename(self, file_name, directory):
        file_list = file_name.split('.')

        name = file_list[0]
        extension = file_list[1]

        if directory[-1] != '/':
            directory += '/'

        return f"{directory}{name}Tab.{extension}"

    def open_file(self, file_name, option, directory=''):
        if option is 'w':
            file_name = self.__get_output_filename(file_name, directory)

        file = open(file_name, option)

        return file

    def write_file(self, file, formatted_data):
        file.write(formatted_data)

        return file.close()