from SQLite import SQLite
from time import gmtime, strftime
from sys import platform
import os
from terminaltables import AsciiTable


class UI:

    numerated_tabels = dict()

    def __init__(self, db_object: SQLite):
        self.db_object = db_object
        self.tables = self.db_object.db_data.keys()
        self.numerate_tabels()

    def print_header(self):
        self.clear_screen()
        print("Current time: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print("Database Path: " + self.db_object.path)

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

        current_table = self.numerated_tabels[table_number]

        while True:

            self.print_table(current_table)
            input()

    def numerate_tabels(self): 
        for num, table in enumerate(self.tables): 
            self.numerated_tabels[num] = table

    def print_table(self, table_name: str):
        self.print_header()

        # List for table output
        table_data = list()

        print("Table name: " + table_name)
        columns = self.db_object.db_data[table_name].columns

        for row_data in self.db_object.db_data[table_name].rows_data:

            table_data.append(row_data)
        table = AsciiTable(table_data)

        print(table.table)

if __name__ == "__main__":
    path = "sqlite_example.db"
    a = SQLite(path)
    ui = UI(a)
    ui.inf_loop_function()
