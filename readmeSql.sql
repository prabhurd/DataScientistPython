select UPPER(EmpFname) as EmpName from EmployeeInfo

Write a query to fetch the number of employees working in the department ‘HR’.

select count(emp_id) from employees where department = 'HR'

*************************

EMPLOYEE (EMP_ID, DEPT_NO)
DEPARTMENT (DEPT_NO, DEPT_NAME)

select count(emp.EMP_ID) from EMPLOYEE emp, DEPARTMENT dep
where emp.DEPT_NO = dep.DEPT_NO and dep.DEPT_NAME = 'HR'

select count(emp.EMP_ID) from EMPLOYEE emp
where DEPT_ID = (select DEPT_ID from DEPARTMETN where DEPT_NAME = 'HR')


select count(emp.EMP_ID) from EMPLOYEE emp
join DEPARTMENT dep on emp.DEPT_NO = dep.DEPT_NO
where dep.DEPT_NAME = 'HR'

DESC DEPTARTMENT

CREATE INDEX idx_deptartment_dept_no on DEPARTMENT(DEPT_NO)


**********************************

select emp_name, location, benefit from employee

select emp_name, location,
if(location="Rural") "Dongel"
else if(location = "TOWN") "WIFI"
else if(location = "CITY")  "BB"
else "OTHER"
 from employee


*********************
Write q query to find all the employees whose salary is between 50000 to 100000.

SELECT * FROM EMPLOYEE
WHERE SALARY BETWEEN 50000 AND 100000

SELECT EMPLOYEE_NAME FROM EMPLOYEE
WHERE UPPER(EMPLOYEE_NAME) like "S%"

SELECT EMPLOYEE_NAME FROM EMPLOYEE
TOP 10
LIMIT 10

SELECT CONCATE(FIRST_NAME +", "+LASTNAME) as FULLNAME from EMPLOYEE

******************************


Write a query to fetch details of employees
whose EmpLname ends with an alphabet ‘A’ and contains five alphabets.

SELECT * FROM EMPLOYEE
WHERE EMPLOYEE_LAST_NAME like "_____A"


*******************************

Write a query to fetch all employees who also hold the managerial position.
EMPLOYEE AND MANGERPOSITIOIN TABLE

EMPLOYEE (ENAME,EMP_ID)
EMPLOYEE (EMP_ID, MANAGER_ID)

SELECT EMPLOYEE_NAME FROM EMPLOYEE e join MANAGERPOSITION m
on e.EMP_ID = m.EMP_ID


SELECT EMPLOYEE_NAME FROM EMPLOYEE e
WHERE EMP_ID IN (
SELECT MANAGER_ID from MANAGER_POSITION
)


***********************************

Write a SQL query to retrieve employee details from EmployeeInfo table
who have a date of joining in the EmployeePosition table.

EmployeeInfo:
EMPLOYEE_NAME
EMPLOYEE_ID

EmployeePosition:
EMPLOYEE_ID
DATE_OF_JOINING

SELECT e.ENAME, ep.DOJ from EmployeeInfo e join  EmployeePosition ep
on e.EMPLOYEE_ID = ep.EMPLOYEE_ID and ep.DOJ != NULL


****************************************


Write a query to retrieve two minimum and maximum salaries from the EmployeePosition table.
EmployeeInfo:
NAME EID

EmployeePosition:
EID SALARY POSITION
select NAME
(SELECT SALARY FROM EmployeePosition GROUP BY POSITION  order by SALARY desc LIMIT 2) as "MAX"
(SELECT SALARY FROM EmployeePosition GROUP BY POSITION  order by SALARY LIMIT 2) as "MIN"


*********************

EMPLOYEE

EMPID EMPNAME EMPADD


selec EMPID FROM EMPLOYEE  e1
WHERE 2 >= (select count(EMPID) from EMPLOYEE e2 where e1.EMPID = e2.EMPID)


********************************************


The following two tables are part of the database you are working with.
Write a query that will display the salaries received by the last contract of a given employee as a result.
Limit the number of obtained records to 1,000.

emp							     contract
empo empname salary fromdate      empno  fromdate

select e.empno, e.salary, c.fromdate from emp e
left join (select empno,max(fromdate) from contract)  c
where c.empno = e.empno and e.fromdate = c.fromdate


********************************************************

How to test for NULL values in a database?

empno empname dept        empno empname dept
100    Bhavani RD         100   Bhavani RD
101    Prabhu             101   Prabhu
102    Prabhu  fct        102   prabhu  fct

select
case
when count(*) == m.count
    return "ALL Matched"
otherwise
    retunr "NOT MATCHE"
end as 'Result'
from source s
left join (
select count(*) as count from src s
left join (

select empno, empname,dept from target

) t
coallesce(s.empno,0) = coallesce(t.empno,0) and
coallesce(s.empname,"") = coallesce(t.empname,"") and
coallesce(s.dept,"") = coallesce(t.dept,"") and
) matched_records m


---
select count(*) form s
left join ( select empno, empname,dept from target ) t
on
coallesce(s.empno,0) = coallesce(t.empno,0) and
coallesce(s.empname,"") = coallesce(t.empname,"") and
coallesce(s.dept,"") = coallesce(t.dept,"")
--------------

select count(*)
join
(select coallesce(s.empno,0) as empname,
        coallesce(s.empname,"") as empname,
        coallesce(s.dept,"") as dept from source) s
 join
(select coallesce(s.empno,0) as empname,
        coallesce(s.empname,"") as empname,
        coallesce(s.dept,"") as dept from target) t
on s.empno = t.empno and s.empname = t.empname and s.dept = t.dept


***************************************


table_1
table_2


out
120 135


select count(*) from table_1

select count(*) from table_2


