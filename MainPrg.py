from LogFile import LogFile
from ProgramOption import ProgramOption


def main():
    print("Welcome! A Program By Yair Ziv And Shadi Badaria")
    logData= LogFile(input("Please enter the file path:"))
    if logData.GetLogList():
        while True:
            program=ProgramOption(logData)
            program.print_options()
            program.exe_Function(input(""))
    else:
        print("could not open file! Exiting....")



if __name__ == "__main__":
    main()
