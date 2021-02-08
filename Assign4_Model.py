"""
Created by YASH MODI
CST8333_351
Assignment 4
"""

import csv
import sqlite3

obj_list = []

connection = sqlite3.connect('covid19cases.db')
c = connection.cursor()

"""This method is used to create table in database"""


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS covid19(identity TEXT, date TEXT, cases TEXT, deaths TEXT, name_fr TEXT, '
              'name_en TEXT)')


"""This method is used to fill table in database"""


def data_entry(identity, date, cases, deaths, name_fr, name_en):
    c.execute("INSERT INTO covid19(identity, date, cases, deaths, name_fr, name_en) VALUES(?, ?, ?, ?, ?, ?)",
              (identity, date, cases, deaths, name_fr, name_en))


"""This method is used to fetch table data from database"""


def fetch(final_str):
    c.execute(final_str)
    record_objects = c.fetchall()
    return record_objects


"""This method is used to search table data from database"""


def Searched_data(identity, date, cases, deaths, name_fr, name_en):
    c.execute("SELECT * FROM covid19 WHERE identity == " + "'" + identity + "'"
              + " AND date == " + "'" + date + "'"
              + " AND cases == " + "'" + cases + "'"
              + " AND deaths == " + "'" + deaths + "'"
              + " AND name_fr == " + "'" + name_fr + "'"
              + " AND name_en == " + "'" + name_en + "'")
    record_object = c.fetchall()
    return record_object


"""This method is used to save data in database"""


def change_save():
    connection.commit()


"""This method is used to delete table data from database"""


def data_deletion(identity, date, cases, deaths, name_fr, name_en):
    c.execute("DELETE FROM covid19 WHERE identity == " + "'" + identity + "'"
              + " AND date == " + "'" + date + "'"
              + " AND cases == " + "'" + cases + "'"
              + " AND deaths == " + "'" + deaths + "'"
              + " AND name_fr == " + "'" + name_fr + "'"
              + " AND name_en == " + "'" + name_en + "'")


"""This method is used get data from csv for database"""


def fileIO():
    try:
        with open('InternationalCovid19Cases.csv') as iniFile:
            scanner = csv.reader(iniFile)
            counter = 0
            for row in scanner:

                if counter == 0:
                    counter += 1
                    continue
                else:

                    counter += 1
                    obj_list.append(row)

        iniFile.close()
    # Checking if mentioned file exist or not
    except IOError:
        print('File not Found')
        print('Please make sure file is in the location')
        exit()


"""This method is used to check data from database"""


def data_check_fill():
    c.execute("SELECT * FROM covid19")
    record_objects = c.fetchall()
    if len(record_objects) == 0:
        print("Please wait, grab a coffee because it might take up to 6min.......thank you for waiting")
        fileIO()
        for row in obj_list:
            data_entry(row[0], row[1], row[2], row[3], row[4], row[5])
        change_save()
    else:
        print("All ready to go")


"""This method is used to disconnect from database"""


def disconnect():
    c.close()
    connection.close()


# fileIO()
# c.execute('CREATE TABLE IF NOT EXISTS covid19(identity TEXT, date TEXT, cases TEXT, deaths TEXT, name_fr TEXT, '
#           'name_en TEXT)')
#
# for row in obj_list:
#     data_entry(row[0], row[1], row[2], row[3], row[4], row[5])
# change_save()
