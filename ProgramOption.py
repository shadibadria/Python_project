from LogFile import LogFile
from ActionsOnText import ActionHandler
from sys import exit
"""
a class to show and sends the user options in the program
"""

class ProgramOption:
    def __init__(self, log_file):
        self.log_file = log_file
        self.program_action = ActionHandler()

    def print_options(self):
        """
        function to print the action the program preformes
        :return: none
        """
        print("""
        1- Print Time and commands
        2- Print all dates in the list(no repeats)
        3- Print all memory address(no repeats)
        4- print the amount of lines in the log file
        5- exit program
        """)

    def exe_Function(self, option):
        """
        the function gets the optin the user picked and call that function
        :param option:  the option number the user entered
        :return: none
        """
        if option == "1":
            self.program_action.ShowDateAndAction(self.log_file.logList)
        elif option == "2":
            self.program_action.ShowAmountRep(self.log_file.logList)
        elif option == "3":
            self.program_action.ShowMemInLines(self.log_file.logList)
        elif option == "4":
            self.program_action.ShowLogAmount(self.log_file.logList, self.log_file.file_path)
        elif option == "5":
            self.program_action.exit_prog()
        else:
            print("Incorrect option must type a number between 1 to 5")







