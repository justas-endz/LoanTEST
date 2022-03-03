from user_input_info import *
import sys

inputFunctions = Loan()

while True:
    print("""
    Press "ENTER" for loan input,
    Type "INFO" for loan information,
    Type "TABLE" for loan table
    Type "ESC" to close
    """)
    user_input = input(">").lower()
    if user_input == "":
        inputFunctions.inputInfo()
    elif user_input == "info":
        inputFunctions.printLoanInfo()
    elif user_input == "table":
        inputFunctions.loanTable()
    elif user_input == "esc":
        sys.exit()
