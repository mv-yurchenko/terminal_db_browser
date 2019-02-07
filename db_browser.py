from UI import *
import sys


def main(): 
    # Check for file path
    if len (sys.argv) == 1: 
        err_msg = "NO FILE NAME"
        raise(FileNotFoundError(err_msg))

    file_path = sys.argv[1]

    db_object = SQLite(file_path)
    ui = UI(db_object)
    
    ui.inf_loop_function()

if __name__ == "__main__":
    main()

