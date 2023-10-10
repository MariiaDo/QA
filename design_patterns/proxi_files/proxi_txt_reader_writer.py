from iread import Read
from iwrite import Write
from txt_reader import TxtReader
from txt_writer import TxtWriter


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self._is_actual_read = None
        self._is_actual_write = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self._is_actual_read:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self._is_actual_read = True
            return self.__result

    def write(self, text: str):
        if self._is_actual_write:
            return self.__result
        else:
            self.__result = self.__real_writer.write(text)
            self._is_actual_write = True
            return self.__result


if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer_writer = TxtWriter('new_file.txt')
    proxy = ProxyTxtRW(reader_reader, writer_writer)
    print(proxy.read())  # тут прочитали файл
    print(proxy.read())  # тут вже не читаємо, а забираємо текст файлу
    proxy.write("write first time")
    proxy.write("try write again")
