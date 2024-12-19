import sqlite3 as sql

def dbcreate(): #создание базы данных
    con = sql.connect('manufacture.db')
    with con:
        con.execute("""
            create table Departments (
                Id integer primary key,
                DepartmentName varchar(30)
            );
        """)

        con.execute("""
            create table JobTitles (
                Id integer primary key,
                JobTitle varchar(30)
            );
        """)

        con.execute("""
            create table Employees (
                Id integer primary key,
                FullName varchar(100),
                DateBirth date,
                DateHire date,
                Department integer,
                Salary money,
                JobTitle integer,
                foreign key(Department) references Departments(Id),
                foreign key(JobTitle) references JobTitles(Id)
            );
        """)

        con.execute("""
            create table Vacations(
                Id integer primary key,
                EmployeeId integer,
                StartDate date,
                EndDate date,
                foreign key(EmployeeId) references Employees(Id)
            )
        """)

def dbfill(): #заполнение базы данных тестовыми данными
    con = sql.connect('manufacture.db')
    department_fill = 'insert into Departments (Id, DepartmentName) values(?, ?)'
    department_data = [
        (1, 'Отдел разработки'),
        (2, 'Отдел кадров'),
        (3, 'Отдел маркетинга'),
        (4, 'Отдел тестирования')
    ]

    job_fill = 'insert into JobTitles (Id, JobTitle) values(?, ?)'
    job_data = [
        (1, 'Разработчик'),
        (2, 'Старший разработчик'),
        (3, 'Директор'),
        (4, 'Маркетолог'),
        (5, 'Бухгалтер'),
        (6, 'Тестировщик'),
        (7, 'Администратор')
    ]

    employee_fill = 'insert into Employees (Id, FullName, DateBirth, DateHire, Department, Salary, JobTitle) values(?, ?, ?, ?, ?, ?, ?)'
    employee_data = [
        (1, 'Иванов Сергей Петрович', '1989-07-24', '2019-10-04', 1, 100000, 2),
        (2, 'Сергеев Петр Иванович', '1998-09-14', '2022-11-11', 1, 70000, 1),
        (3, 'Амуров Андрей Викторович', '1999-11-10', '2024-05-15', 1, 65000, 1),
        (4, 'Блатов Иван Вячеславович', '1980-05-13', '2018-09-01', 1, 150000, 3),
        (5, 'Держинский Антон Игоревич', '2000-01-30', '2021-11-27', 3, 70000, 4),
        (6, 'Аверин Максим Петрович', '1995-08-20', '2019-03-11', 3, 80000, 3),
        (7, 'Лебедева Алиса Юрьевна', '1997-10-14', '2021-07-15', 2, 60000, 5),
        (8, 'Савельев Игорь Адекснадрович', '1995-05-21', '2020-02-12', 2, 60000, 7),
        (9, 'Ибрагимова Мария Дмитриевна', '1990-11-02', '2019-12-10', 2, 100000, 3),
        (10, 'Андреев Игнат Владимирович', '1988-07-04', '2018-11-10', 4, 130000, 3),
        (11, 'Невелов Максим Алексеевич', '2001-10-12', '2022-01-13', 4, 80000, 6),
        (12, 'Орлов Дмитрий Олегович', '1997-04-24', '2021-10-04', 4, 90000, 6),
    ]

    vacation_fill = 'insert into Vacations (Id, EmployeeId, StartDate, EndDate) values(?, ?, ?, ?)'
    vacation_data = [
        (1, 1, '2020-10-11', '2020-10-25'),
        (2, 2, '2023-11-01', '2023-11-15'),
        (3, 1, '2022-07-01', '2022-07-30'),
        (4, 4, '2021-10-01', '2021-10-15'),
        (5, 5, '2023-09-10', '2023-09-24'),
        (6, 6, '2020-05-11', '2020-05-25'),
        (7, 7, '2022-10-01', '2022-10-30'),
        (8, 8, '2021-02-10', '2021-02-24'),
        (9, 9, '2022-09-01', '2022-10-01'),
        (10, 10, '2020-12-01', '2020-12-31'),
        (11, 11, '2024-05-30', '2024-06-30'),
        (12, 12, '2023-01-11', '2023-01-25'),
    ]

    with con:
        con.executemany(department_fill, department_data)
        con.executemany(job_fill, job_data)
        con.executemany(employee_fill, employee_data)
        con.executemany(vacation_fill, vacation_data)
