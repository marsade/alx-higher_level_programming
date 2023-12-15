#!/usr/bin/python3
"""Lists all states where name matches the argument from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit
    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=usr, passwd=password, db=db_name)
    cur = db.cursor()
    exe = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(exe)
    rows = cur.fetchall()
    for row in rows:
        print (row)
    cur.close()
    db.close()
