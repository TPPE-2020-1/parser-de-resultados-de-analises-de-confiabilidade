class ParseData:
    def format_output_in_lines(self, parsed_data: dict, delimiter_symbol: str, output_format: str) -> str:
        output_str = ''

        for evolution, times in parsed_data.items():
            partial = f"{delimiter_symbol}".join(times)
            line = f"{evolution}{delimiter_symbol}{partial}"
            output_str += line + '\n'

        return output_str

    def format_output_in_columns(self, parsed_data: dict, delimiter_symbol: str, output_format: str) -> str:
        max_times_size = 0
        output_str = ''
        count = 0

        for i, evolution in enumerate(parsed_data.keys()):
            output_str += str(evolution) + (delimiter_symbol if i <
                                            len(parsed_data.keys()) - 1 else '\n')

            current_times_size = len(parsed_data[evolution])
            if current_times_size > max_times_size:
                max_times_size = current_times_size

        for idx in range(0, max_times_size):
            for evolution in parsed_data.keys():
                try:
                    output_str += (delimiter_symbol if count !=
                                   0 else '') + str(parsed_data[evolution][idx])
                except:
                    output_str += (f"{delimiter_symbol}NaN" if count !=
                                   0 and count + 1 != len(parsed_data.keys()) else '')

                count += 1

            output_str += '\n'

            count = 0

        return output_str
