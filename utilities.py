# -*- coding: utf-8 -*- 
# __author__: Adarsh Kalikadien #
import sqlite3
import pandas as pd


def convert_csv_to_sqlite_db(csv_filename):
    '''Convert CSV files to SQLITE3 database, the script assumes that the CSV file and database are
    in the same folder as the script

    :param csv_filename:
    :return: SQLITE3 database with contents from CSV file
    '''
    db_filename = csv_filename.split('.')[0]
    conn = sqlite3.connect(db_filename + '.db')
    location_csv = pd.read_csv(csv_filename)  # load in dataframe
    # create table study_locations in test.db
    location_csv.to_sql('study_locations', conn, if_exists='replace', index=False)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


if __name__ == "__main__":
    convert_csv_to_sqlite_db('test.csv')
    # con = sqlite3.connect("test.db")
    # con.row_factory = dict_factory
    # cur = con.cursor()
    # cur.execute("select * from study_locations")
    # print(cur.fetchall()[0]["study_location"])
