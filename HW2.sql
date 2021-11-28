--1) Создать таблицу employees
--- id. serial,  primary key,
--- employee_name. Varchar(50), not null
create table employees(
	id serial primary key,
	employees_name varchar(50) not null
)

--2) Наполнить таблицу employee 70 строками.
insert into employees (employees_name)
values ('Wade Perez'),
	   ('Marsha Blanton'),
	   ('Arthur Grubb'),
	   ('Juan Jones'),
	   ('Nellie Ding'),
	   ('Mary Roberts'),
	   ('Jason Johnson'),
	   ('Stephen Mcgriff'),
	   ('Darlene Odell'),
	   ('Marvin Thompson'),
	   ('Michael Lindburg'),
	   ('Edward Dean'),
	   ('Donald Gagne'),
	   ('Lisa Harriss'),
	   ('Joan Bridgewater'),
	   ('Ashli Delarosa'),
	   ('Peter Mortensen'),
	   ('Ezra Trent'),
	   ('Cheryl Oakes'),
	   ('Cynthia Rhew'),
	   ('Shanika Cheatom'),
	   ('William Bettis'),
	   ('Clifford Napier'),
	   ('Karen Braunstein'),
	   ('Carrie Artis'),
	   ('Denise Doire'),
	   ('Gloria Howell'),
	   ('Alicia Wilkerson'),
	   ('Herschel Walker'),
	   ('Jan Wood'),
	   ('Maria Underwood'),
	   ('Paul Holmes'),
	   ('Ida Castro'),
	   ('Ronald Bowlin'),
	   ('Bob Petrillo'),
	   ('Pauline Wyatt'),
	   ('Nicholas Crume'),
	   ('Mary Tuggle'),
	   ('Velma Gillispie'),
	   ('Frances Hancock'),
	   ('Sandra Dudley'),
	   ('Patricia Cohran'),
	   ('Kum Cipriani'),
	   ('Ivan Holliday'),
	   ('Herschel Walker'),
	   ('Jeraldine Garcia'),
	   ('Tyler Lopez'),
	   ('Williams Benincase'),
	   ('Thomas Rundell'),
	   ('Demetrius Goodell'),
	   ('Kevin Taylor'),
	   ('Van Waite'),
	   ('Milford Jimenez'),
	   ('Chelsea Legore'),
	   ('Alma Sasso'),
	   ('Michael Weatherly'),
	   ('Courtney Wu'),
	   ('Mary Grinder'),
	   ('Regina Morgan'),
	   ('James Mullane'),
	   ('Joni Story'),
	   ('Frances Castle'),
	   ('Leonard Dominguez'),
	   ('Andrew Sprague'),
	   ('Marissa Morrow'),
	   ('Warren Price'),
	   ('Betty Keeling'),
	   ('Charles Evans'),
	   ('Christopher Olney'),
	   ('Eric Frey'),
	   ('Marva Day');
	  
-- 3) Создать таблицу salary
--- id. Serial  primary key,
--- monthly_salary. Int, not null

create table salary(
	id serial primary key,
	montly_salary int not null
)

-- 4) Наполнить таблицу salary 15 строками:
/*- 1000
- 1100
- 1200
- 1300
- 1400
- 1500
- 1600
- 1700
- 1800
- 1900
- 2000
- 2100
- 2200
- 2300
- 2400
- 2500*/

insert into salary (monthly_salary)
values (1000),
       (1100),
       (1200),
       (1300),
       (1400),
       (1500),
       (1600),
       (1700),
       (1800),
       (1900),
       (2000),
       (2100),
       (2200),
       (2300),
       (2400),
       (2500);
      
-- 5) Создать таблицу employee_salary
--- id. Serial  primary key,
--- employee_id. Int, not null, unique
--- salary_id. Int, not null
     
create table employee_salary(
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null
)

-- 6) Наполнить таблицу employee_salary 40 строками:
--- в 10 строк из 40 вставить несуществующие employee_id

insert into employee_salary (employee_id, salary_id)
values (3, 2),
       (7, 3),
       (6, 7),
       (5, 9),
       (88, 1),
       (10, 4),
       (11, 6),
       (22, 5),
       (25, 1),
       (16, 3),
       (78, 5),
       (4, 8),
       (36, 10),
       (14, 10),
       (95, 2),
       (47, 11),
       (54, 3),
       (30, 5),
       (42, 13),
       (68, 12),
       (2, 4),
       (13, 1),
       (96, 8),
       (12, 9),
       (23, 15),
       (1, 14),
       (41, 14),
       (28, 2),
       (32, 7),
       (83, 6),
       (55, 5),
       (99, 12),
       (72, 14),
       (19, 10),
       (92, 7),
       (26, 6),
       (84, 11),
       (75, 8),
       (24, 6),
       (58, 1);
      
-- 7) Создать таблицу roles
--- id. Serial  primary key,
--- role_name. int, not null, unique

create table roles(
	id serial primary key,
	role_name int not null unique
)

-- 8) Поменять тип столба role_name с int на varchar(30)

alter table roles
alter column role_name type varchar(30);

-- 9) Наполнить таблицу roles 20 строками:
-- Junior Python developer
-- Middle Python developer
-- Senior Python developer
-- Junior Java developer
-- Middle Java developer
-- Senior Java developer
-- Junior JavaScript developer
-- Middle JavaScript developer
-- Senior JavaScript developer
-- Junior Manual QA engineer
-- Middle Manual QA engineer
-- Senior Manual QA engineer
-- Project Manager
-- Designer
-- HR
-- CEO
-- Sales manager
-- Junior Automation QA engineer
-- Middle Automation QA engineer
-- Senior Automation QA engineer

insert into roles (role_name)
values ('Junior Python developer'),
	   ('Middle Python developer'),
       ('Senior Python developer'),
       ('Junior Java developer'),
       ('Middle Java developer'),
       ('Senior Java developer'),
       ('Junior JavaScript developer'),
       ('Middle JavaScript developer'),
       ('Senior JavaScript developer'),
       ('Junior Manual QA engineer'),
       ('Middle Manual QA engineer'),
       ('Senior Manual QA engineer'),
       ('Project Manager'),
       ('Designer'),
       ('HR'),
       ('CEO'),
       ('Sales manager'),
       ('Junior Automation QA engineer'),
       ('Middle Automation QA engineer'),
       ('Senior Automation QA engineer');
      
-- 10) Создать таблицу roles_employee
--- id. Serial  primary key,
--- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
--- role_id. Int, not null (внешний ключ для таблицы roles, поле id)

create table roles_employee(
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key (employee_id)
		references employees(id),
	foreign key (role_id)
		references roles(id)
)

-- 11) Наполнить таблицу roles_employee 40 строками

insert into roles_employee (employee_id, role_id)
values (2, 10),
       (10, 6),
       (30, 8),
       (52, 1),
       (7, 4),
       (31, 3),
       (38, 2),
       (70, 6),
       (55, 7),
       (61, 10),
       (35, 12),
       (19, 9),
       (44, 11),
       (20, 5),
       (28, 8),
       (3, 17),
       (36, 13),
       (63, 18),
       (50, 6),
       (42, 19),
       (23, 20),
       (14, 7),
       (21, 12),
       (62, 4),
       (17, 15),
       (29, 13),
       (41, 16),
       (45, 5),
       (53, 6),
       (16, 7),
       (54, 8),
       (66, 4),
       (37, 13),
       (24, 2),
       (59, 6),
       (69, 9),
       (13, 5),
       (49, 1),
       (65, 11),
       (68, 12);
      

	 