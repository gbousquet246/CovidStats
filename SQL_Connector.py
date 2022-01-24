import mysql.connector
import dataimporter as di

conn = mysql.connector.connect(user='root', password='Fallout2112#', host='127.0.0.1', port='3306',
                               database='covid_stats')
cursor = conn.cursor()


def into_table(csv, table_name):
    df = di.dataframe(csv)
    df_col_names = di.get_columns(df)
    new_table(table_name, df_col_names)


def new_table(table_name, column):
    # this makes a table, but you still need to work out how to get the data type.
    sql = "CREATE TABLE table_name (id INT AUTO_INCREMENT PRIMARY KEY, column"
    cursor.execute(sql)


def update_table(table_name, column, values):
    # This currenly only works staticly need to work out how to make it dynamic
    sql = "UPDATE table_name (column) VALUES(%s,%s)"
    cursor.execute(sql, values)


def select(sql):
    cursor.execute(sql)


def close_conn():
    if conn.is_connected():
        conn.close()
        cursor.close()
