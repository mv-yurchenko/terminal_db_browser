from SQLite import SQLite
from time import gmtime, strftime
from sys import platform
import os
from terminaltables import AsciiTable


class UI:

    def __init__(self, db_object):
        self.db_object = db_object
        self.tables = db_object.

    def print_header(self):
        self.clear_screen()
        print("Current time: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print("Database Path: " + self.db_object.db_data.path_to_db)

    @staticmethod
    def clear_screen():
        if platform == "win32":
            os.system('cls')
        else:
            os.system("clear")

    @staticmethod
    def input_command():
        command = input("INPUT COMMAND: ")
        return command

    def inf_loop_function(self):

        table_number = 0

        current_table = self.db_object.get_table_by_number(table_number)

        while True:

            self.print_table(current_table)

    def print_table(self, table_name: str):
        self.print_header()

        # List for table output
        table_data = list()

        print("Table name: " + table_name)
        columns = self.db_object.db_data[table_name].columns
        table_data.append(columns)

        for row_data in self.db_object.db_data[table_data].rows:
            table_data.append(row_data)
        table = AsciiTable(table_data)
        print(table.table)
