"""
a class to check the data in the log lines
"""
class TextValidator:
    def validateMonth(self, month_na):
        """
        function to check if the month name in the log line is correct
        :param month_na: the month appreing in the log line
        :return: return true if the month name is correct and return false if not
        """
        try:
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            if month_na in months:
                return True
        except ValueError:
            return False
        return False

    def validateDay(self, day_val):
        """
        check if the date value is correct in the log lines
        :param day_val: the date number of the month
        :return: return true if the dates  is correct and return false if not
        """
        try:
            if int(day_val) < 1 or int(day_val) > 31:
                return False
        except ValueError:
            return False
        return True

    def validateTime(self, time_val):
        """
        a function to check if the hours are correct in the log lines
        :param time_val: the houer that appers in the log line in the text file
        :return: return true if the dateis correct and return false if not
        """
        try:
            hour_val, min_val, sec_val = time_val.split(":")
            if int(hour_val) > 23 or int(hour_val) < 0:
                return False
            if int(min_val) > 59 or int(min_val) < 0:
                return False
            if int(sec_val) > 59 or int(sec_val) < 0:
                return False
        except ValueError:
            return False
        return True

    def IsInList(self, to_check, in_list):
        """
        a function to check if an item appers in a list
        :param to_check: the item to check if he in the list
        :param in_list: the list to check in
        :return: a return true if the object is in the list and flase if not
        """
        for log in in_list:
            if to_check in log:
                return False
        return True








