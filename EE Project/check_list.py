def check_phno(ph_no):
    if len(ph_no)==10:
        pass
    else:
        print("Error...!!")
        print("Invalid Phone Number...!")
        ph_no=input("Re-Enter the Phone Number : ")
        check_phno(ph_no)
def check_gender(gender):
    if gender=='male' or gender=='female' or gender=='transgender':
        pass
    else:
        print("Gender Un-Identified...!!!")
        gender=input("Please Re-Enter your Gender : ")
        check_gender(gender)
