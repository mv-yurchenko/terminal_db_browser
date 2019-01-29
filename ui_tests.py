from UI import UI
import unittest
from SQLite import SQLite

class TestUI(unittest.TestCase): 

    path = "sqlite_example.db"
    db = SQLite(path)
    ui = UI(db)

    def test_get_command_type_and_command_text(self):
        ui_command_example = "/UI_COMMAND_EXAMPLE"
        sql_commad_example = "SELECT * FROM TABLE"

        self.assertEqual(("SQL_COMMAND", sql_commad_example), self.ui.get_command_type_and_command_text(sql_commad_example))
        self.assertEqual(("UI_COMMAND", "UI_COMMAND_EXAMPLE"), self.ui.get_command_type_and_command_text(ui_command_example))
        self.assertEqual(ValueError, self.ui.get_command_type_and_command_text(""))
    
    def test_process_sql_command(self): 
        pass
if __name__ == "__main__":
    unittest.main()