from txt_reader import TxtReader
from txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        """
        A method to read a file content
        """
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_value):
        """
        A method that  writes a new string to a file.
        Allows to write an empty string in order to erase the file content.

        """
        self.__result = self.__txt_writer.write(new_value)
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')
    print(proxy_reader.read_file())
    proxy_reader.write_file('Happy Birthday!')
    print(proxy_reader.read_file())
    proxy_reader.write_file('')
    print(proxy_reader.read_file())
    proxy_reader.write_file('Hello!')
    print(proxy_reader.read_file())
