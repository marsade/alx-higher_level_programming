#!/usr/bin/python3
"""lists all cities from a state in hbtn_0e_4_usa"""
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
    cur.execute("SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON states.id = cities.state_id \
                WHERE states.name = %s ", (match, ))
    rows = cur.fetchall()
    tmp = set(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
