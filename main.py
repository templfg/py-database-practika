import sqlite3 as sql
from dbclass import DataBase
from dbcreate import dbcreate, dbfill

def get_command():
    try:
        cmd = int(input())
        return cmd
    except ValueError:
        return "ValueError"

def table_employees_scene(db:DataBase):
    cmd = get_command()
    if cmd == 1:
        db.show_table("Employees")
        print('\n')
        return "table_employees"
    elif cmd == 2:
        print("""
                Введите через запятую данные:
                <Id>,'<ФИО>','<Дата рождения>','<Дата приема на работу>',<Id отдела>,<Зарплата>,<Id должности>
        """)
        row = '(' + input() + ')'
        db.add_row_in_table('Employees', row)
        print(f"""
                Строка {row} успешно добалена
        """)
        return "table_employees"
    elif cmd == 3:
        print("""
                Введите через пробел данные:
                <Название столбца> <Значение столбца>
        """)
        column, value = input().split(' ')
        row = ""
        with db.con:
            for r in db.con.execute(f"select * from Employees where {column} = {value}"):
                row = r
        db.delete_row_from_table('Employees', column, value)
        print(f"""
                Строка {row} успешно удалена
        """)
        return "table_employees"
    elif cmd == 8:
        return "main"
    elif cmd == "ValueError":
        print("Error--> Введите только номер команды")
        return "table_employees"
    else:
        print("Error--> Нет такой команды")
        return "table_employees"

def table_departments_scene(db:DataBase):
    cmd = get_command()
    if cmd == 1:
        db.show_table("Departments")
        print('\n')
        return "table_departments"
    elif cmd == 2:
        print("""
                Введите через запятую данные:
                <Id>,'<Название отдела>'
        """)
        row = '(' + input() + ')'
        db.add_row_in_table('Departments', row)
        print(f"""
                Строка {row} успешно добалена
        """)
        return "table_departments"
    elif cmd == 3:
        print("""
                Введите через пробел данные:
                <Название столбца> <Значение столбца>
        """)
        column, value = input().split(' ')
        row = ""
        with db.con:
            for r in db.con.execute(f"select * from Departments where {column} = {value}"):
                row = r
        db.delete_row_from_table('Departments', column, value)
        print(f"""
                Строка {row} успешно удалена
        """)
        return "table_departments"
    elif cmd == 8:
        return "main"
    elif cmd == "ValueError":
        print("Error--> Введите только номер команды")
        return "table_departments"
    else:
        print("Error--> Нет такой команды")
        return "table_departments"

def table_jobtitles_scene(db:DataBase):
    cmd = get_command()
    if cmd == 1:
        db.show_table("JobTitles")
        print('\n')
        return "table_jobtitles"
    elif cmd == 2:
        print("""
                Введите через запятую данные:
                <Id>,'<Название должности>'
        """)
        row = '(' + input() + ')'
        db.add_row_in_table('JobTitles', row)
        print(f"""
                Строка {row} успешно добалена
        """)
        return "table_jobtitles"
    elif cmd == 3:
        print("""
                Введите через пробел данные:
                <Название столбца> <Значение столбца>
        """)
        column, value = input().split(' ')
        row = ""
        with db.con:
            for r in db.con.execute(f"select * from JobTitles where {column} = {value}"):
                row = r
        db.delete_row_from_table('JobTitles', column, value)
        print(f"""
                Строка {row} успешно удалена
        """)
        return "table_jobtitles"
    elif cmd == 8:
        return "main"
    elif cmd == "ValueError":
        print("Error--> Введите только номер команды")
        return "table_jobtitles"
    else:
        print("Error--> Нет такой команды")
        return "table_jobtitles"

def table_vacatios_scene(db:DataBase):
    cmd = get_command()
    if cmd == 1:
        db.show_table("Vacations")
        print('\n')
        return "table_vacations"
    elif cmd == 2:
        print("""
                Введите через запятую данные:
                <Id>,<Id сотрудника>,'<Дата начала отпуска>','<Дата конца отпуска>'
        """)
        row = '(' + input() + ')'
        db.add_row_in_table('Vacations', row)
        print(f"""
                Строка {row} успешно добалена
        """)
        return "table_vacations"
    elif cmd == 3:
        print("""
                Введите через пробел данные:
                <Название столбца> <Значение столбца>
        """)
        column, value = input().split(' ')
        row = ""
        with db.con:
            for r in db.con.execute(f"select * from Vacations where {column} = {value}"):
                row = r
        db.delete_row_from_table('Vacations', column, value)
        print(f"""
                Строка {row} успешно удалена
        """)
        return "table_vacations"
    elif cmd == 8:
        return "main"
    elif cmd == "ValueError":
        print("Error--> Введите только номер команды")
        return "table_vacations"
    else:
        print("Error--> Нет такой команды")
        return "table_vacations"

def count_salary_for_person(db:DataBase):
    print("""
                Введите данные через пробел:
                <Id сотрудника> <Дата начала отсчета> <Дата конца отсчета>
    """)
    id, start, end = input().split(' ')
    db.count_salary_for_period(id, start, end)
    return "main"

def personal_by_department(db:DataBase):
    print("""
                Введите Id отдела:
    """)
    id = int(input())
    db.count_department_employees(id)
    return "main"

def scene_main():
    print("""
                1. Табл. Employees
                2. Табл. Departments
                3. Табл. JobTitles
                4. Табл. Vacations
                5. Объем ЗП по сотруднику
                6. Численность отдела
                7. Общее кол-во сотрудников
                9. Выход
            """)
    cmd = get_command()
    if cmd == 1:
        return "table_employees"
    elif cmd == 2:
        return "table_departments"
    elif cmd == 3:
        return "table_jobtitles"
    elif cmd == 4:
        return "table_vacations"
    elif cmd == 5:
        return "count_salary"
    elif cmd == 6:
        return "department_popularity"
    elif cmd == 7:
        return "personal_count"
    elif cmd == 9:
        print("""
                Завершение работы...
        """)
        return "exit"
    elif cmd == "ValueError":
        print("Error--> Введите только номер команды")
        return "main"
    else:
        print("Error--> Нет такой команды")
        return "main"

def main():
    table_scene_list = """
                1. Показать данные
                2. Добавить строку
                3. Удалить строку
                8. Назад
    """
    db = DataBase()
    if not db.check_ready():
        dbcreate()
        dbfill()
    current_scene = "main"
    while current_scene != "exit":
        if current_scene == "main":
            current_scene = scene_main()
        elif current_scene == "table_employees":
            print("         Текущая таблица: Employees")
            print(table_scene_list)
            current_scene = table_employees_scene(db)
        elif current_scene == "table_departments":
            print("         Текущая таблица: Departments")
            print(table_scene_list)
            current_scene = table_departments_scene(db)
        elif current_scene == "table_jobtitles":
            print("         Текущая таблица: JobTitles")
            print(table_scene_list)
            current_scene = table_jobtitles_scene(db)
        elif current_scene == "table_vacations":
            print("         Текущая таблица: Vacations")
            print(table_scene_list)
            current_scene = table_vacatios_scene(db)
        elif current_scene == "count_salary":
            current_scene = count_salary_for_person(db)
        elif current_scene == "department_popularity":
            current_scene = personal_by_department(db)
        elif current_scene == "personal_count":
            db.count_all_employees()
            current_scene = "main"

if __name__ == '__main__':
    main()