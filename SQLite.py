import sqlite3
from os.path import isfile
from TableData import TableData


class SQLite: 

    def __init__(self, path):
        self.path = path

        # Open DB and Initialize connection and cursor 
        self.update_db_connection_and_data()

    def open_db(self):
        
        # If file not exists
        if not isfile(self.path): 
            raise(FileNotFoundError)

        connection = sqlite3.connect(self.path)
        return connection, connection.cursor()

    def get_tables_list(self): 
        request = "select name FROM  sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
        self.cursor.execute(request)
        tables_list = []
        for table in (list(self.cursor.fetchall())):
            tables_list.append(table[0])
        return tables_list

    def get_data_from_table(self, table_name: str):
        # Compile request
        request = "SELECT * FROM '" + table_name + "'"
        
        self.cursor.execute(request)

        return self.cursor.fetchall()

    def get_column_names(self, table_name: str):
        request = "PRAGMA table_info('" + table_name + "');"
        answer = self.cursor.execute(request).fetchall()

        columns_names = list()
        for column_data in answer:
            columns_names.append(column_data[1])
        return columns_names
     
    @staticmethod
    def process_request(request: str):
        request = request.replace(',', ' ')
        return request

    def parse_select_request(self, request):
        splitted_request = request.split()
        print(splitted_request)
        from_index = int()
        # Search for 'from' word
        for index, word in enumerate(splitted_request):
            if word == 'from' or word == 'FROM':
                from_index = index
                table_name_index = from_index + 1

        table_name = splitted_request[table_name_index]

        # if column names specified
        if splitted_request[1] != '*':
            columns_names = splitted_request[1:from_index]

        else:
            columns_names = self.db_data[table_name].columns
        return columns_names, table_name

    def update_db_connection_and_data(self): 

        self.connection, self.cursor = self.open_db()

        self.tables_list = self.get_tables_list()

        self.db_data = dict()   # dict : {'table_name' : table_data_object}

        for table in self.tables_list:
            data = self.get_data_from_table(table)
            columns = self.get_column_names(table)
            
            table_data = TableData(columns, data)

            self.db_data[table] = table_data
        

if __name__ == "__main__":
    path = "sqlite_example.db"
    a = SQLite(path)
