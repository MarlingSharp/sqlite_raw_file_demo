import sqlite3
from sqlite3 import Error

DB_FILENAME = 'mydb.db'
SQL_FILENAME = 'commands.sql'
SQL_COMMAND_TERMINATOR = ';'

def select_data(sql, criteria=()):
  conn = None
  try:
      conn = sqlite3.connect(DB_FILENAME)
      cur = conn.cursor()
      cur.execute(sql, criteria)

      return cur.fetchall()
  except Error as e:
      print(e)
  finally:
      if conn:
          conn.close()


def execute_sql(sql, data=()):
    conn = None
    try:
        conn = sqlite3.connect(DB_FILENAME)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()

        return cur.lastrowid
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()