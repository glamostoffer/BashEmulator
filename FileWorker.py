import zipfile
import os


class FileWorker:
    def __init__(self, file):
        self.__file = zipfile.ZipFile(file, "r")  # открытие архива для чтения
        self.__path = zipfile.Path(self.__file, at="")  # создание объекта для операций с путями

    def __del__(self):  # в деструкторе закрываем архив и удаляем освобождаем поля
        del self.__path
        self.__file.close()
        del self.__file

    def get_path(self):
        return self.__path

    def print_path(self):
        print(str(self.get_path()) + "#", end=' ')

    def ls(self, path_file=" "):
        path = self.get_path()
        if path_file == " ":
            for name in path.iterdir():  # выводим названия всех файлов в директории с помощью цикла
                print(name.name)
        else:
            path = path.joinpath(path_file)
            if path.exists():
                for name in path.iterdir():
                    print(name.name)
            else:
                print("Incorrect path")

    def cd(self, path):
        if path == "../" or path == ".." or path == "//":
            new_path = str(self.__path)  # для подъема в предыдущую директорию удалим из пути имя последней папки
            new_path = new_path[:len(new_path)-1]
            new_path = new_path[new_path.find('/')+1:new_path.rfind('/')]  # и удалим название архива
            self.__path = zipfile.Path(self.__file, at="")
            self.__path = self.__path.joinpath(new_path)  # добавим к начальному пути путь без последней директории
        else:
            self.__path = self.__path.joinpath(path)

    def pwd(self):
        print(str(os.getcwd()) + '\\' + str(self.__path).replace('/', '\\'))

    def cat(self, file_name):
        new_path = self.__path.joinpath(file_name)
        if new_path.is_file() and new_path.exists():
            print(new_path.read_text())
        else:
            print("Incorrect file name")
