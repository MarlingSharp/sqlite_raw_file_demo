print('Welcome to the SQL Test Bench')

import os

from common import \
  SQL_FILENAME, \
  DB_FILENAME, \
  SQL_COMMAND_TERMINATOR, \
  select_data, \
  execute_sql

try:
  sql_file = open(SQL_FILENAME, 'r')
  sql_lines = sql_file.readlines() 

  sql_commands = []

  sql_command = []
  for sql_line in [s.strip() for s in sql_lines if len(s) > 0]:
    sql_command.append(sql_line)
    if (sql_line.endswith(SQL_COMMAND_TERMINATOR)):
      sql_commands.append(sql_command)
      sql_command = []

  for sql_command in sql_commands:
    single_line_command = " ".join(sql_command).strip()
    print(single_line_command)

    if (single_line_command.upper().startswith('SELECT')):
      data = select_data(single_line_command)
      for d in data:
        print(d)
    else:
      lastrowid = execute_sql(single_line_command)
      print(f"Amended Row with ID {lastrowid}")
except Exception as e:
  print(e)
finally:
  print('Removing Database')
  os.remove(DB_FILENAME)

print('Complete')