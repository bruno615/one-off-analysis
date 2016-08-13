# Jitbit Test

# https://www.jitbit.com/news/181-jitbits-sql-interview-questions/
/*
table - columns

Employees - EmployeeID, DepartmentID, BossID, Name, Salary
Departments - DepartmentID, Name
*/

## Questions ######################################################

#List employees (names) who have a bigger salary than their boss

select e.EmployeeID, e.Name
from Employees e
  left join Employees b on b.EmployeeID = e.BossID
where e.Salary > b.Salary
;
#List employees who have the biggest salary in their departments

select
    EmployeeID,
    e.Name,
    d.Name as department,
    e.Salary,
    rank() over (partition by e.DepartmentID ORDER BY salary desc)
from employees e
  left join departments d on d.DepartmentID = e.DepartmentID
group by 1,2,3,4
having rank() over (partition by e.DepartmentID ORDER BY salary desc) = 1

#List departments that have less than 3 people in it

select
  d.Name as department,
  count(e.EmployeeID) as employee_count
from departments d
  left join employees e on d.DepartmentID = e.DepartmentID
group by 1
having count(EmployeeID) < 3

#List all departments along with the number of people there (tricky - people often do an "inner join" leaving out empty departments)

select
  d.Name as department,
  count(e.EmployeeID) as employee_count
from departments d
  left join employees e on d.DepartmentID = e.DepartmentID
group by 1

#List employees that don't have a boss in the same department

select
  e.EmployeeID,
  e.Name as employee_name
from employees e
  inner join employees b on b.EmployeeID = e.BossID and e.DepartmentID <> b.DepartmentID
;
#List all departments along with the total salary there

select
  d.Name as department,
  sum(salary) as total_salary
from departments d
  left join employees e on d.DepartmentID = e.DepartmentID
group by 1
;
