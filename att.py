
class AttendanceShortageException(Exception):
    def __init__(self,arg):
        self.msg=arg
class IncomeException(Exception):
    def __init__(self,arg):
        self.msg=arg
class GPAException(Exception):
    def __init__(self,arg):
        self.msg=arg


attendance=int(input("Enter attendance:"))
if attendance < 75:
    raise AttendanceShortageException(" Thrown when student attendance is less than 75")
else:
    print("student attendance%",attendance,"%")
    
PI = int(input("enter parents income:"))
if PI>500000:
    raise InvalidMinimumException(" Thrown when parents income is higher than 500000 ")
else:
    print("parents income:",PI)

CGPA=int(input("enter CGPA:"))
if CGPA<7:
    raise InsufficientFundException("Thrown when student CGPA is less than 7")
else:
    print(" your CGPA",CGPA)
