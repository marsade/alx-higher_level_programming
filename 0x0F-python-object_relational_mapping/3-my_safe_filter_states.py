#!/usr/bin/python3
"""states where name matches the argument from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        exit
    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    match = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
