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

