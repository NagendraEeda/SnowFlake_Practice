CREATE DATABASE PRAC;

CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(30),
    Salary DECIMAL(10,2),
    JoinDate DATE
);

INSERT INTO Employees (ID, Name, Department, Salary, JoinDate) VALUES 
(1, 'Alice', 'HR', 55000, '2020-05-10'),
(2, 'Bob', 'IT', 62000, '2019-03-15'),
(3, 'Charlie', 'Finance', 70000, '2021-08-20'),
(4, 'David', 'IT', 48000, '2018-11-05'),
(5, 'Eva', 'HR', 75000, '2017-07-14'),
(6, 'Frank', 'Finance', 62000, '2016-09-25');


SELECT * FROM Employees;


-- ROW_NUMBER() – Assigns a unique number to each row based on the order specified.

SELECT *,
ROW_NUMBER() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY DESC) RWN
FROM Employees;

SELECT * FROM 
(SELECT *,
ROW_NUMBER() OVER(ORDER BY SALARY DESC) RWN
FROM Employees)A
WHERE A.RWN = 1;


-- The RANK() function assigns a ranking based on the order specified in a query.
-- If duplicate values exist, they receive the same rank, but the next rank is skipped.


SELECT *,
RANK() OVER(ORDER BY SALARY DESC) RA
FROM EMPLOYEES;

SELECT * FROM(
SELECT *,
RANK() OVER(ORDER BY SALARY DESC) RA
FROM EMPLOYEES
)A
WHERE A.RA =3;

---The DENSE_RANK() function is similar to RANK(), but does not skip ranks when there are duplicates.
--It ensures that rankings remain continuous without gaps.


SELECT *,
DENSE_RANK() OVER (ORDER BY SALARY DESC) DR
FROM EMPLOYEES;


SELECT * FROM (
SELECT *,
DENSE_RANK() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY DESC) DR
FROM EMPLOYEES)A
WHERE A.DR = 1;



SELECT *,
ROW_NUMBER() OVER(ORDER BY SALARY DESC) RN,
RANK() OVER(ORDER BY SALARY DESC) RA,
DENSE_RANK() OVER(ORDER BY SALARY DESC) DR
FROM EMPLOYEES;


-- LAG() – Get Previous Row Value

SELECT * FROM EMPLOYEES;

SELECT ID, Name, Salary,
       LAG(Salary, 1, 0) OVER (ORDER BY ID) AS PrevSalary
FROM Employees;


--LEAD() – Get Next Row Value

SELECT ID, Name, Salary,
        LAG(Salary, 1, 0) OVER (ORDER BY ID) AS PrevSalary,
       lead(Salary, 1, 0) OVER (ORDER BY ID) AS NextSalary
FROM Employees;


-- NTILE(n)	Distributes rows into n equal groups

SELECT *,
NTILE(2) OVER(ORDER BY ID) D2,
NTILE(3) OVER(ORDER BY ID) D3,
NTILE(4) OVER(ORDER BY ID) D3
FROM EMPLOYEES;


SELECT *
FROM EMPLOYEES;

SELECT *,
SUM(SALARY) OVER(ORDER BY ID ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AA
FROM EMPLOYEES;


---> CUMMLATIVE SUM

SELECT *,
SUM(SALARY) OVER(ORDER BY ID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AA
FROM EMPLOYEES;


----> MOVING AVG

SELECT *,
AVG(SALARY) OVER(ORDER BY ID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AA
FROM EMPLOYEES;
