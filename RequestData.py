class RequestData:
    
    def __init__(self, request_type: str, columns: list, table_name, *conditions):
        self.request_data = request_type
        self.columns = columns
        self.table_name = table_name
        self.conditions = conditions