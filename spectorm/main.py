import json
import os


class ApplicationContext:
    """The central user and configuration interface. Parses the user input, sets default values and so on"""
    def __init__(self):
        # basic path for plots
        self.plot_path = None

        # target database
        self.database_type = "sqlite"

        # delete imported raw files
        self.delete_imported = False

        # generated and default orm classes, useful for queries
        self.orm_classes = {}

        # database interaction class (ImportWizard or WorkWizard)
        self.database_actor = None

    def parse_config_files(self):
        """Read in the users configuration data"""
        pass

    def invoke_import(self):
        """Start the import procedure"""
        pass

    @staticmethod
    def read_spec_config(file):
        with open(file) as infile:
            temp = infile.read()
            spec_list = json.loads(temp)

            return spec_list


# todo: make exception module, customize exceptions
# todo: add knowledge about metaclass, docstrings and custom exception to markdown notes
# todo: implement a filter-based method of MetaSpectrum to check all attributes necessary for spectrum creation
# todo: ensure that an initial table spec_types is generated
# todo: handling of unit and name of x/y separately
# todo: create a function for backup of the database