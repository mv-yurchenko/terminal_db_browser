from UI import UI
import unittest
from SQLite import SQLite

class TestUI(unittest.TestCase): 

    path = "sqlite_example.db"
    db = SQLite(path)
    ui = UI(db)
    sql_commad_example_1 = "SELECT * FROM test_table"
    sql_commad_example_2  = "SELECT test_text_field, test_int_field FROM test_table"
    sql_commad_example_3  = "SELECT test_int_field FROM test_table"
    def test_get_command_type_and_command_text(self):
        ui_command_example = "/UI_COMMAND_EXAMPLE"


        self.assertEqual(("SQL_COMMAND", self.sql_commad_example_1), self.ui.get_command_type_and_command_text(self.sql_commad_example_1))
        self.assertEqual(("UI_COMMAND", "UI_COMMAND_EXAMPLE"), self.ui.get_command_type_and_command_text(ui_command_example))
        self.assertEqual(ValueError, self.ui.get_command_type_and_command_text(""))
    
    def test_process_sql_command(self): 
        self.assertEqual([ "test_int_field", "test_text_field"], self.ui.process_sql_command_and_get_columns_names(self.sql_commad_example_1))
        self.assertEqual([ "test_text_field" ,"test_int_field" ], self.ui.process_sql_command_and_get_columns_names(self.sql_commad_example_2))
        self.assertEqual([ "test_int_field"], self.ui.process_sql_command_and_get_columns_names(self.sql_commad_example_3))

if __name__ == "__main__":
    unittest.main()