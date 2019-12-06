import datetime
import os

class DefaultImporter:

    """ This class and its derived classes are responsible for the actual raw data import procedure"""
    @staticmethod
    def get_creation_time(file_path):
        temp = os.path.getmtime(file_path)
        return datetime.datetime.fromtimestamp(temp)
