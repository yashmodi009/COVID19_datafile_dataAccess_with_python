"""
Created by YASH MODI
CST8333_351
Assignment 4
"""

import Assign4_Controller

choice = ""

# Start the program
Assign4_Controller.start()


# loop for display menu
while choice != "y":
    print("Coded by YASH MODI\n\n")
    print("A.Display data entries\n" +
          "B.Create data entries\n" +
          "C.Edit data entries\n" +
          "D.Delete data entries\n" +
          "X.Exit\n\n")
    value = input("Enter your choice: ")

    # The first option to display
    if value == "A" or value == "a":
        print("A.Display all data entries\n" + "B.Display filtered records\n" + "C.Display some data entries\n")
        option = input("Enter your option: ")
        if option == "A" or option == "a":
            Assign4_Controller.displayAll()

        elif option == "B" or option == "b":
            Assign4_Controller.display_with_filter()
            # Id = input("Please enter an id: ")
            # date = input("Please enter a date: ")
            # cases = input("Please enter number of cases: ")
            # deaths = input("Please enter number of deaths: ")
            # name_fr = input("Enter name of the country in french: ")
            # name_en = input("Enter name of the country in English: ")
            # data = Assign4_Controller.search(Id, date, cases, deaths, name_fr, name_en)
            # print(data)

        elif option == "C" or option == "c":
            number = input("How many entries do you want to display: ")
            Assign4_Controller.display(number)
        else:
            print("Choose from the given option........\n\n")

    # The second option to Create
    elif value == "B" or value == "b":
        Id = input("Please enter an id: ")
        date = input("Please enter a date: ")
        cases = input("Please enter number of cases: ")
        deaths = input("Please enter number of deaths: ")
        name_fr = input("Enter name of the country in french: ")
        name_en = input("Enter name of the country in English: ")
        Assign4_Controller.create(Id, date, cases, deaths, name_fr, name_en)

    # The third option to edit
    elif value == "C" or value == "c":
        Assign4_Controller.edit()

    # The forth option to Delete
    elif value == "D" or value == "d":
        Id = input("Please enter an id: ")
        date = input("Please enter a date: ")
        cases = input("Please enter number of cases: ")
        deaths = input("Please enter number of deaths: ")
        name_fr = input("Enter name of the country in french: ")
        name_en = input("Enter name of the country in English: ")
        Assign4_Controller.delete(Id, date, cases, deaths, name_fr, name_en)

    elif value == "X" or value == "x":
        choice = input("Are you sure you want to quit (y/n): ")
        if choice == 'y':
            Assign4_Controller.close()
    else:
        print("Choose from the given option........\n\n")
