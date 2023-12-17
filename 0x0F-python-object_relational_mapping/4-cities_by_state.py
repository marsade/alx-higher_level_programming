#!/usr/bin/python3
"""lists all states from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit
    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                LEFT JOIN states \
                ON states.id = cities.state_id \
                ORDER BY cities.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
