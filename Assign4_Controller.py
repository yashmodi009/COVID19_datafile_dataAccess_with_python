"""
Created by YASH MODI
CST8333_351
Assignment 4
"""

import Assign4_Model

"""This method is used to check if the database data and fill it if necessary"""


def start():
    Assign4_Model.data_check_fill()


"""This method is used to close the database"""


def close():
    Assign4_Model.disconnect()


"""This method is used to Display from the database with filter"""


def display_with_filter():
    req = input("Enter column/columns you wanna filter (identity, date, cases, deaths, name_fr, name_en): ").split(' ')
    ini_string = "SELECT * FROM covid19 WHERE "

    for x in req:
        if x == "date":
            inp = input("Enter value for " + x + " (YYYY-MM-DD): ")
            choice = input("Choose (greater(1)/smaller(2)/equal(3)/greater equal(4)/smaller equal(5)): ")
            if choice == "1":
                str_formation = x + " > " + "'" + inp + "'" + " AND "
                ini_string = ini_string + str_formation
            elif choice == "2":
                str_formation = x + " < " + "'" + inp + "'" + " AND "
                ini_string = ini_string + str_formation
            elif choice == "3":
                str_formation = x + " == " + "'" + inp + "'" + " AND "
                ini_string = ini_string + str_formation
            elif choice == "4":
                str_formation = x + " >= " + "'" + inp + "'" + " AND "
                ini_string = ini_string + str_formation
            elif choice == "5":
                str_formation = x + " <= " + "'" + inp + "'" + " AND "
                ini_string = ini_string + str_formation
            else:
                print("Please choose from the option given......")
        else:
            inp = input("Enter value for " + x + " : ")
            str_formation = x + " == " + "'" + inp + "'" + " AND "
            ini_string = ini_string + str_formation
    final_str = ini_string[:len(ini_string) - 5]
    record_objects = Assign4_Model.fetch(final_str)
    if len(record_objects) == 0:
        print("No record with such value exists")
    else:
        for row in record_objects:
            print(row)


"""This method is used to create an object and store it"""


def create(identity, date, cases, deaths, name_fr, name_en):
    record = search(identity, date, cases, deaths, name_fr, name_en)
    if len(record) == 0:
        Assign4_Model.data_entry(identity, date, cases, deaths, name_fr, name_en)
        Assign4_Model.change_save()
        print("New record created and save")
    else:
        print("Already existing data")


"""This method is used to edit an object and store it and also delete the old recorded object"""


def edit():
    print("Enter information of the entity you need to update")
    ide = input("Please enter an id: ")
    date = input("Please enter a date: ")
    cases = input("Please enter number of cases: ")
    deaths = input("Please enter number of deaths: ")
    name_fr = input("Enter name of the country in french: ")
    name_en = input("Enter name of the country in English: ")

    # Finding if the object record exist
    record = search(ide, date, cases, deaths, name_fr, name_en)
    if len(record) == 0:
        print("No such entity exist")
    else:
        Assign4_Model.data_deletion(ide, date, cases, deaths, name_fr, name_en)
        Assign4_Model.change_save()
        id_updated = input("Please enter the updated id: ")
        date_updated = input("Please enter the updated date: ")
        cases_updated = input("Please enter updated number of cases: ")
        deaths_updated = input("Please enter updated number of deaths: ")
        name_fr_updated = input("Enter updated name of the country in french: ")
        name_en_updated = input("Enter updated name of the country in English: ")
        Assign4_Model.data_entry(id_updated, date_updated, cases_updated, deaths_updated, name_fr_updated,
                                 name_en_updated)
        Assign4_Model.change_save()
        print("Entity updated")


"""This method is used to delete an object"""


def delete(identity, date, cases, deaths, name_fr, name_en):
    record = search(identity, date, cases, deaths, name_fr, name_en)
    if len(record) == 0:
        print("The record you mentioned does not exist")
    else:
        Assign4_Model.data_deletion(identity, date, cases, deaths, name_fr, name_en)
        Assign4_Model.change_save()
        print("Deleted Record permanently")


"""This method is used to display all objects"""


def displayAll():
    process_str = "SELECT * FROM covid19"
    record_objects = Assign4_Model.fetch(process_str)
    for row in record_objects:
        print(row)


"""This method is used to display objects from the recorded list"""


def display(count):
    process_str = "SELECT * FROM covid19 LIMIT " + count
    record_objects = Assign4_Model.fetch(process_str)
    for row in record_objects:
        print(row)


"""This method is used to search for particular object record"""


def search(identity, date, cases, deaths, name_fr, name_en):
    data = Assign4_Model.Searched_data(identity, date, cases, deaths, name_fr, name_en)
    return data
