
class FilesHandler:
    def read_file(self, file_path):
        """
        this function is responsible to open the file the user enter, and check for exeptns
        :param file_path: the file location enterd by the user
        :return: a list of all the logs in the log file
        """
        try:
            with open(file_path, 'r') as f:
                return [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            print("File Not Found - could not read file ")
        except FileExistsError:
            print("Could not read file  - the file is missing")
        except PermissionError:
            print('Could Not Read File - Permission is denied')
        return None


