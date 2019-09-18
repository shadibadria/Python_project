from TextCheck import TextValidator
from sys import exit
import re
import os
"""
a class to preform actions on the text in the lists
"""
class ActionHandler:
    def __init__(self):
        self.validate = TextValidator()

    def ShowDateAndAction(self, log_list):
        """
        a function to show the user all the time date and hour and commands in the list
        (Option 1)
        :param log_list:
        :return:
        """
        for log in log_list:
            month_val, day_val, time_val, command_in = log.split(" ", 3)
            if self.validate.validateMonth(month_val):
                if self.validate.validateDay(day_val):
                    if self.validate.validateTime(time_val):
                        command_out = command_in.split(":", 1)
                        print(month_val + " " + day_val + " " + time_val + ":" + command_out[1])
        return

    def ShowAmountRep(self, log_list):
        """
        a function to count the amount of log in every date (option 2)
        :param log_list: the listd of all the logs in the file
        :return:
        """
        date_log_list = []
        outPutlist = []
        for log in log_list:
            count = 0
            month_val, day_val, command_text = log.split(" ", 2)
            if self.validate.validateMonth(month_val) and self.validate.validateDay(day_val):
                check_data = month_val + " " + day_val
                if self.validate.IsInList(check_data, date_log_list):
                    date_log_list.append(check_data)
                    for info in log_list:
                        if month_val in info and day_val in info:
                            count = count + 1
                    outPutlist.append(check_data + " " + str(count))
        print("Found " + str(outPutlist.__len__()) + " different dates")
        print("____________")
        for i in outPutlist:
            print(i)
        return

    def ShowLogAmount(self, log_list, path_file):
        """
        a function to count all the log lines in the file(option 4)
        :param log_list: the list of all the logs in the file
        :param path_file: the path of the file enterd by the user
        :return:
        """
        str1 = ""
        str1 = str1 + str(log_list.__len__()) + " Records found in "
        str1 = str1 + os.path.splitext(path_file)[0] + os.path.splitext(path_file)[1]
        print(str1)


    def ShowMemInLines(self,log_list):
        for mem in log_list:
            txt= re.findall("0x",mem)
            if not txt:
                print("j")
            else:
                print(txt)





    def exit_prog(self):
        """
        function to exit the program
        :return:
        """
        print("Thank you for using our program. Exiting...")
        exit(True)

