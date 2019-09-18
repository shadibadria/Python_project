from FileHandler import FilesHandler

"""
a class to work with the log files
"""


class LogFile:

    def __init__(self, file_Path):
        self.file_path = file_Path
        self.logList = []

    def GetLogList(self):
        """
        a function to try and open the file the user gives if not the exit the program
        :return: a boolean value if the file was correctly open
        """
        self.logList = FilesHandler().read_file(self.file_path)
        if not self.logList:
            return False
        return True
