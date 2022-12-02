#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    state_name = sys.argv[4]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT c.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id WHERE s.name = %s\
                 ORDER BY c.id", (state_name, ))
    rows = cur.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")
