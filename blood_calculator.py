print("This is the database module and python calls it {}".format(__name__))

def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9-Quit")
        print("1-HDL test")
        print("2-LDL test")
        print("3-Total Cholesterol test")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Total_Cholesterol_driver()

    return

def accept_input(test_name):
    entry = input("Enter the {} test result:".format(test_name))
    return int(entry)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Bloodline Low"
    else:
        answer = "Low"
    return answer

def check_LDL(LDL_value):
    if LDL_value >= 190:
        answer = "Very High"
    elif 189 >= LDL_value >= 160:
        answer = "High"
    elif 159 >= LDL_value >= 130:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer

def check_Total_Cholesterol(Total_Cholesterol_value):
    if Total_Cholesterol_value >= 240:
        answer = "High"
    elif 239 >=  Total_Cholesterol_value >= 200:
        answer = "Bloodline High"
    else:
        answer = "Normal"
    return answer


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}.".format(test_value, test_name, test_class)
    print(out_string)
    return

def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)

def LDL_driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)

def Total_Cholesterol_driver():
    Total_Cholesterol_value = accept_input("Total Cholesterol")
    classification = check_Total_Cholesterol(Total_Cholesterol_value)
    print_result("Total Cholesterol", Total_Cholesterol_value, classification)

if __name__ == "__main__":
    interface()

