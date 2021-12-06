-- 1. Вывести всех работников чьи зарплаты есть в базе, вместе с зарплатами.
select employees_name, monthly_salary from employees
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id;

-- 2. Вывести всех работников у которых ЗП меньше 2000.
select employees_name, monthly_salary from employees
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where monthly_salary < 2000;

-- 3. Вывести все зарплатные позиции, но работник по ним не назначен. (ЗП есть, но не понятно кто её получает.)
select employees_name, monthly_salary from employee_salary
join salary on salary.id = employee_salary.salary_id
left join employees on employees.id = employee_salary.employee_id
where employees_name is null;
;
-- 4. Вывести все зарплатные позиции  меньше 2000 но работник по ним не назначен. (ЗП есть, но не понятно кто её получает.)
select employees_name, monthly_salary from employee_salary
join salary on salary.id = employee_salary.salary_id
left join employees on employees.id = employee_salary.employee_id
where employees_name is null and monthly_salary < 2000;

-- 5. Найти всех работников кому не начислена ЗП.
select employees_name, monthly_salary from employee_salary
join salary on salary.id = employee_salary.salary_id
right join employees on employees.id = employee_salary.employee_id
where monthly_salary is null;

-- 6. Вывести всех работников с названиями их должности.
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id;

-- 7. Вывести имена и должность только Java разработчиков.
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%Java %';

-- 8. Вывести имена и должность только Python разработчиков.
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%Python%';

-- 9. Вывести имена и должность всех QA инженеров.
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%QA%';

-- 10. Вывести имена и должность ручных QA инженеров.
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%Man%QA%';

-- 11. Вывести имена и должность автоматизаторов QA
select employees_name, role_name from roles_employee
join employees on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%Auto%QA%';

-- 12. Вывести имена и зарплаты Junior специалистов
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Junior%';

-- 13. Вывести имена и зарплаты Middle специалистов
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Middle%';

-- 14. Вывести имена и зарплаты Senior специалистов
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Senior%';

-- 15. Вывести зарплаты Java разработчиков
select monthly_salary from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Java %';

-- 16. Вывести зарплаты Python разработчиков
select monthly_salary from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Python%';

-- 17. Вывести имена и зарплаты Junior Python разработчиков
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Jun%Python%';

-- 18. Вывести имена и зарплаты Middle JS разработчиков
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Mid%JavaS%';

-- 19. Вывести имена и зарплаты Senior Java разработчиков
select employees_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Sen%Java %';

-- 20. Вывести зарплаты Junior QA инженеров
select monthly_salary, role_name from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Jun%QA%';

-- 21. Вывести среднюю зарплату всех Junior специалистов
select role_name, avg(monthly_salary) as average_salary from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%Junior%'
group by role_name;

-- 22. Вывести сумму зарплат JS разработчиков
select role_name, sum (monthly_salary) as salary_sum from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%JavaSc%'
group by role_name;

-- 23. Вывести минимальную ЗП QA инженеров
select role_name, min (monthly_salary) as min_salary from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%QA%'
group by role_name;

-- 24. Вывести максимальную ЗП QA инженеров
select role_name, max (monthly_salary) as max_salary from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%QA%'
group by role_name;

-- 25. Вывести количество QA инженеров
select count (employees.id) as amount from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%QA%';

-- 26. Вывести количество Middle специалистов.
select count (employees.id) as amount from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%Middle%';

-- 27. Вывести количество разработчиков
select count (employees.id) as amount from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
where role_name like '%developer%';

-- 28. Вывести фонд (сумму) зарплаты разработчиков.
select sum(monthly_salary) as funds from roles_employee
join roles on roles_employee.role_id = roles.id
join employee_salary on roles_employee.employee_id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where role_name like '%developer%';

-- 29. Вывести имена, должности и ЗП всех специалистов по возрастанию
select employees_name, role_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
order by monthly_salary asc;

-- 30. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП от 1700 до 2300
select employees_name, role_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where monthly_salary between 1700 and 2300
order by monthly_salary asc;

-- 31. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП меньше 2300
select employees_name, role_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where monthly_salary < 2300
order by monthly_salary asc;

-- 32. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП равна 1100, 1500, 2000
select employees_name, role_name, monthly_salary from employees
join roles_employee on employees.id = roles_employee.employee_id
join roles on roles_employee.role_id = roles.id
join employee_salary on employees.id = employee_salary.employee_id
join salary on employee_salary.salary_id = salary.id
where monthly_salary in (1100, 1500, 2000)
order by monthly_salary asc;