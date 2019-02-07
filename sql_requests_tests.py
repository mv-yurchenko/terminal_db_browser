import unittest
from SQLite import SQLite


class testSQL(unittest.TestCase):

    sql_obj = SQLite("test.db")

    def test_select_request(self): 
        
        # Test "SELECT ALL"
        test_request_1 = "SELECT * FROM test_table"
        expected_answ_1 = "[(123, '23'), (123, '123'), (1323, '123'), (1323, '123'), (1323, '123'), (1323, '123'), (1323, '123'), ('dffgdfg', 'sdgfdfg')]"
        self.assertEqual(str(self.sql_obj.execute_request(test_request_1)), expected_answ_1)

        # Test "SELECT from" by columns
        test_request_2 = "SELECT test_int_field FROM test_table"
        expected_answ_2 = "[(123,), (123,), (1323,), (1323,), (1323,), (1323,), (1323,), ('dffgdfg',)]"
        self.assertEqual(str(self.sql_obj.execute_request(test_request_2)), expected_answ_2)

        test_request_3 = test_request_2.replace("test_int_field", "test_text_field")
        expected_answ_3 = "[('23',), ('123',), ('123',), ('123',), ('123',), ('123',), ('123',), ('sdgfdfg',)]"
        self.assertEqual(str(self.sql_obj.execute_request(test_request_3)), expected_answ_3)

        # Test column that doesn't exist
        test_request_4 = test_request_2.replace("test_int_field", "column_random")
        self.assertEqual(self.sql_obj.execute_request(test_request_4) , RuntimeError)

    
if __name__ == "__main__":
    unittest.main()