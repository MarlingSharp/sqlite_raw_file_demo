import sqlite3

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
    finally:
        if conn:
            conn.close()