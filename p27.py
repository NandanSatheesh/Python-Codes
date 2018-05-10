
"""
Create an employee table with attributes
    name , email , phone number , hire datedept_id  , job id , salary , manager_id

Write a query to display the names

first name , last name , from the employeees relation
"""

write a query to get all employee deatils from the employee table and order by their first name

select * from employee order by first_name ;

select first_name , (0.12* salary ) as pf from employee ;


write a query to get the total salaries payable to employees

select sum(salary) from employee ;

select max(salary) , min(salary) , avg(salary) from employee ;

write a qurey to get the number of employees in the employee table

select count(*) from employee ;

write a query to get the number of jobs available in the job

select * from employee where departent_number = 30 or departmen_number = 100 order by first_name asc  ;


select * from employee where