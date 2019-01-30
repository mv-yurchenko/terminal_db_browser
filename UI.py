from SQLite import SQLite
from time import gmtime, strftime
from sys import platform
import os
from terminaltables import AsciiTable
from itertools import cycle
import readline


class UI:

    numerated_tabels = dict()
    commands_and_names = list()

    def __init__(self, db_object: SQLite):
        self.db_object = db_object
        self.tables = list(self.db_object.db_data.keys())
        self.numerate_tabels()
        self.ui_commands = {
            "NEXT" : self.next_table_command, 
            "PREV" : self.prev_table_command
        }
        self.generate_list_for_autocomplete()

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

    
    def input_command(self):
        # Bind TAB for autocomplete
        readline.parse_and_bind("tab: complete")

        # Define compiter function 
        def completer(text, cmd_index):
            possible_commands = [cmd for cmd in self.commands_and_names if cmd.startswith(text)]
            if cmd_index < len(possible_commands):
                return possible_commands[cmd_index]
            else:
                return None

        readline.set_completer(completer)

        command = input("INPUT COMMAND: ")
        return command

    def inf_loop_function(self):

        self.current_table = self.tables[0]

        while True:

            self.print_table(self.current_table)
            
            command = self.input_command()

            command_type, command = self.get_command_type_and_command_text(command)

            if command_type == "UI_COMMAND" and command in self.ui_commands.keys(): 
                self.execute_ui_command(command.upper())

            elif command_type == "SQL_COMMAND": 
                self.execute_sql_command(command)
                

    def numerate_tabels(self): 
        for num, table in enumerate(self.tables): 
            self.numerated_tabels[num] = table

    @staticmethod
    def color_str_to_red(string: str) -> str: 
        R__BEG = '\033[91m'
        R_END = '\033[0m'
        return R__BEG + string + R_END 

    def print_table(self, table_name: str):
        self.print_header()

        # List for table output
        table_data = list()

        print("Table name: " + table_name)

        # Columns is the header of the table
        table_data.append(self.db_object.db_data[table_name].columns)

        # Add every row in the table
        table_data +=  self.db_object.db_data[table_name].rows_data

        table = AsciiTable(table_data)

        print(table.table)

    def get_command_type_and_command_text(self, command: str) -> str: 
        # Check for first symbol (UI commands starts with /)

        # If command is empty returns ValueError
        if not command: 
            return ValueError

        if command[0] == "/": 
            return "UI_COMMAND", command[1:].upper()

        else: return "SQL_COMMAND", command

    def generate_list_for_autocomplete(self): 
        # Add table names 
        self.commands_and_names.append(self.tables)

        # Add columns names
        for table in self.db_object.db_data.values():
            self.commands_and_names.append(table.columns)
        
        # Items from sublists to main list
        self.commands_and_names = [item for sublist in self.commands_and_names for item in sublist]

        # Add SQL Commands to autocomplete list
        sql_commands = ["SELECT", "INSERT", "from"]
        
        self.commands_and_names += sql_commands

    # SQL COMMANDS
    def execute_sql_command(self, command):
        # 1) Process command
        # 2) send command to sql as string
        columns_names = self.process_sql_command_and_get_columns_names(command)
        
        answer = self.db_object.execute_request(command)

        self.output_select_answer(columns_names, answer)
        print("\n answer from SQL: ")
        print(answer)
        input()

    @staticmethod
    def output_select_answer(columns_names, rows_data): 
        print("\nResult: \n")
        table_data = [ ]
        # Columns is the header of the table
        table_data.append(columns_names)

        # Add every row in the table
        table_data += rows_data

        table = AsciiTable(table_data)

        print(table.table)

    def process_sql_command_and_get_columns_names(self, command: str):
        # replace all ',' with ' '
        command = command.replace(',', ' ')
        # Remove ;
        if command[-1] == ";": 
            command = command[:-1]
        
        command = command.split()


        from_index = 2
        
        for word in command: 
            if word == "from" or word == "FROM": 
                from_index = command.index(word)

        # table name aftwer from 
        table_name = command[from_index + 1]

        if command[1] == "*": 
            columns_names = self.db_object.db_data[table_name].columns
        else:   
            columns_names = command[1: from_index]
        return columns_names

    # UI COMMANDS 
    def execute_ui_command(self, command): 
        self.ui_commands[command]()
    
    def next_table_command(self): 
        current_index = self.tables.index(self.current_table)

        if current_index == len(self.tables) - 1: 
            self.current_table = self.tables[0]
        else: 
            self.current_table = self.tables[current_index + 1]
    
    def prev_table_command(self): 
        current_index = self.tables.index(self.current_table)

        if current_index == 0: 
            self.current_table = self.tables[len(self.tables) - 1]
        else: 
            self.current_table = self.tables[current_index - 1]
    
if __name__ == "__main__":
    path = "sqlite_example.db"
    a = SQLite(path)
    ui = UI(a)
    ui.inf_loop_function()
