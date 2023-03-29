
employee_list = []
item_list = []


def create_employee():
    while True:
        employee_id = input("\nEnter Employee ID: ")
        if not employee_id.isdigit():
            print("Employee ID must be a number.")
            continue
        if [emp for emp in employee_list if emp[0] == int(employee_id)]:
            print("Employee ID must be unique.")
            continue
        employee_name = input("Enter Employee Name: ")
        if not employee_name:
            print("Employee Name cannot be empty.")
            continue
        employee_type = input("Enter Employee Type (hourly or manager): ")
        if employee_type.lower() not in ["hourly", "manager"]:
            print("Employee Type must be 'hourly' or 'manager'.")
            continue
        years_worked = input("Enter Years Worked: ")
        if not years_worked.isdigit():
            print("Years Worked must be a number.")
            continue
        employee_discount = input("Enter Employee Discount Number: ")
        if not employee_discount.isdigit():
            print("Employee Discount Number must be a number.")
            continue
        if [emp for emp in employee_list if emp[6] == int(employee_discount)]:
            print("Employee Discount Number must be unique.")
            continue
        employee = [int(employee_id), employee_name, employee_type, int(years_worked), 0, 0, int(employee_discount)]
        employee_list.append(employee)
        print("Employee added successfully.")
        proceed = input("Do you want to add another employee? (Yes/No)")
        if proceed.lower() != "yes":
            break
    print("Returning to main menu...")

    main()


def create_item():
    while True:
        item_number = input("Enter Item Number: ")
        if not item_number.isdigit():
            print("Item number must be a number.")
            continue

        item_number = int(item_number)
        if any(item_number == item[0] for item in item_list):
            print("Item number already exists.")
            continue

        item_name = input("Enter Item Name: ")
        if not item_name:
            print("Item name cannot be empty.")
            continue

        item_cost = input("Enter Item Cost: ")
        if not item_cost.isdigit():
            print("Item cost must be a number.")
            continue

        item_cost = int(item_cost)
        item_list.append([item_number, item_name, item_cost])

        user_input = input("Do you want to add another item? (YES/NO)").lower()
        if user_input == "no":
            break

    print("Items created:")
    print("Returning to main menu...")
    main()


def make_purchase(item_list, employee_list):
    print("Make a Purchase Page")
    while True:
        print("\nPlease choose one of the following formats to display the Item list:")
        print("\n1. Print with format")
        print("     Item Number        | Item Name       | Item Cost")
        print("     11526              | Nike shoes      | $120.00")
        print("     11849              | Trampoline      | $180.00")
        print("     11966              | Mercury Bicycle | $150.00")
        print("     11334              | Necklace Set    | $80.00")

        print("\n2. Simple print")
        print("Item Number, Item Name, Item Cost")
        print("11526, Nike shoes, $120.00")
        print("11849, Trampoline, $180.00")
        print("11966, Mercury Bicycle, $150.00")
        print("11334, Necklace Set, $80.00")
        display_option = input("\nEnter your choice (1 or 2): ")

        if display_option == "1":
            print("Item Number | Item Name         | Item Cost")
            for item in item_list:
                print("{:<10} | {:<15} | ${:.2f}".format(item[0], item[1], item[2]))
            break
        elif display_option == "2":
            print("Item Number, Item Name, Item Cost")
            for item in item_list:
                print("{}, {}, ${:.2f}".format(item[0], item[1], item[2]))
            break
        else:
            print("Invalid option, please try again.")

    while True:
        employee_id = int(input("Enter employee ID: "))
        for employee in employee_list:
            if employee[0] == employee_id:
                employee_discount_num = employee[6]
                employee_discount = 0
                years_worked = employee[3]
                if years_worked >= 10:
                    employee_discount = 10
                else:
                    employee_discount = 2 * years_worked
                if employee[2] == "manager":
                    employee_discount += 10
                elif employee[2] == "hourly":
                    employee_discount += 2
                if employee_discount >= 10:
                    employee_discount = 10
                employee_discount = employee_discount / 100

                item_number = int(input("Enter item number: "))
                for item in item_list:
                    if item[0] == item_number:
                        total_discount = item[2] * employee_discount
                        total_purchase = item[2] - total_discount
                        employee[5] += total_purchase
                        employee[4] += total_discount
                        print("Employee ID: {}".format(employee[0]))
                        print("Employee Name: {}".format(employee[1]))
                        print("Employee Type: {}".format(employee[2]))
                        print("Years Worked: {}".format(employee[3]))
                        print("Total Purchased: ${:.2f}".format(employee[5]))
                        print("Total Discounts: ${:.2f}".format(employee[4]))
                        print("Employee Discount Number: {}".format(employee[6]))

        another_purchase = input("Another purchase? (YES/NO): ").lower()
        if another_purchase != "no":
            pass
        else:
            main()


def print_employee_summary(employee_list):
    print("\nOption 1: Print with format")
    print(
        "Employee ID | Employee Name | Employee Type | Years Worked | Total Purchased | Total Discount | Employee "
        "Discount Number")
    print("1001        | John Alber    | hourly        | 8            |$ 90.00          | $10            | 22737")
    print("1002        | Sarah Rose    | manager       | 12           |$ 40.00          | $10            | 22344")

    print("\nOption 2: Simple print")
    print(
        "Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, Employee Discount "
        "Number")
    print("1001, John Alber, hourly, 8, 90, 10, 22737")
    print("1002, Sarah Rose, manager, 12,40, 10, 22344")
    display_option = int(input("\nEnter 1 for option 1 or 2 for option 2: "))
    if display_option == 1:
        print(
            "Employee ID | Employee Name | Employee Type | Years Worked | Total Purchased | Total Discount | "
            "Employee Discount Number")
        for employee in employee_list:
            print(employee[0], " " * (12 - len(str(employee[0]))), "|",
                  employee[1], " " * (15 - len(employee[1])),      "|",
                  employee[2], " " * (15 - len(employee[2])),      "|",
                  employee[3], " " * (15 - len(str(employee[3]))), "|",
                  "${:.2f}".format(employee[4]), " " * (15 - len("{:.2f}".format(employee[4]))), "|",
                  "${:.2f}".format(employee[5]), " " * (15 - len("{:.2f}".format(employee[5]))), "|",
                  employee[6])
    elif display_option == 2:
        print(
            "Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, "
            "Employee Discount Number")
        for employee in employee_list:
            print(employee[0], ", ", employee[1], ", ", employee[2], ", ",
                  employee[3], ", ", "${:.2f}".format(employee[4]), ", ",
                  "${:.2f}".format(employee[5]), ", ", employee[6])

    another_employee_summary = input("Another summary? (yes/no)").lower()
    if another_employee_summary != "no":
        print_employee_summary(employee_list)
    else:
        print("Returning to main menu...")
        main()


employee_list = []


def display_menu():
    print("—————————————————————————————————————————")
    print("|   1- Create Employee                  |")
    print("|   2- Create Item                      |")
    print("|   3- Make Purchase                    |")
    print("|   4-All Employee Summary              |")
    print("|   5-Exit                              |")
    print("—————————————————————————————————————————")

    pass


def main():
    display_menu()

    user_input = input("Enter an option from the menu: ")
    if user_input == "1":
        create_employee()
    elif user_input == "2":
        create_item()
    elif user_input == "3":
        make_purchase(item_list, employee_list)
    elif user_input == "4":
        print_employee_summary(employee_list)
    elif user_input == "5":
        exit()
    else:
        print("Invalid option, please try again.")
        main()


main()