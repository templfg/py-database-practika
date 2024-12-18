import sqlite3 as sql
from datetime import datetime

class DataBase:
    def __init__(self):
        self.con = sql.connect('manufacture.db')
        self.tables = ['Departments', 'JobTitles', 'Employees', 'Vacations']
    
    def check_ready(self):
        with self.con:
            data = []
            for row in self.con.execute("select tbl_name from sqlite_master where type = 'table'"):
                data.append(row[0])
            return data == self.tables

    def show_table(self, table):
        if table in self.tables:
            with self.con:
                data = self.con.execute('select * from ' + table)
                for r in data:
                    print(r)
            return ""
        return "TableNotFound"
    
    def count_salary_for_period(self, id, start, end):
        with self.con:
            for row in self.con.execute(f"select DateHire, Salary, FullName from Employees where Id='{id}'"):
                datehire = row[0]
                salary = row[1]
                name = row[2]
            s = max(datetime.strptime(datehire, '%Y-%m-%d'), datetime.strptime(start, '%Y-%m-%d'))
            e = min(datetime.strptime(end, '%Y-%m-%d'), datetime.now())
            daydiff = abs((s - e).days)
            print(f"За {daydiff} дней сотруднику {name} было выплачено {daydiff // 30 * salary} руб.\n")
    
    def count_all_employees(self):
        with self.con:
            for row in self.con.execute("select count(*) from Employees"):
                print(f"Общее количество сотрудников: {int(row[0])}")
    
    def count_department_employees(self, department_code):
        with self.con:
            for row in self.con.execute(f"select count(*) from Employees where Department={department_code}"):
                value = int(row[0])
            for row in self.con.execute(f"select DepartmentName from Departments where Id={department_code}"):
                department = row[0]
            print(f"В отеделе {department} числятся {value} сотрудников\n")
    
    def add_row_in_table(self, table, row):
        query = f"insert into {table} values {row}"
        with self.con:
            self.con.execute(query)
    
    def delete_row_from_table(self, table, column_name, value):
        with self.con:
            self.con.execute(f"delete from {table} where {column_name} = {value}")