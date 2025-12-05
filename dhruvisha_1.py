#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1. Display employee information such as employee id, employee name,designation,gender,position.

employee_id = 1
employee_name = "abc"
designation = "manager"
gender = "female"
position = 1

print("employee id: ",employee_id, "\nemployee_name: ",employee_name,"\ndesignation: ",designation,
      "\ngender: ",gender,"\nposition: ",position)


# In[10]:


#2. Input the basic salary,DA,HRA (DA is 10% of basic salary and HRA is 8% of basic salary) and calculate 
#the gross salary is basic salary + DA+HRA of the employee.

basic_salary = float(input("Enter the basic salary:"))
# DA = input("Enter DA:")
# HRA = input("Enter HRA:")
DA = float(basic_salary*(10/100))
HRA = float(basic_salary*(8/100))
gross_salary = (basic_salary + DA + HRA)

print("Basic_salary: ",basic_salary,"\nDA: ",DA,"\nHRA: ",HRA,"\ngross_salary: ",gross_salary)


# In[19]:


#3 If the user gender is ‘male’ then display an employee name,designation and basic salary.

employee_name = "abc"
designation = "manager"
gender = "male"
basic_salary = 1300

if gender=="male":
   print("employee_name: ",employee_name,"\ndesignation: ",designation,"\ngender: ",gender,"\nBasic_salary: ",basic_salary)
else:
   print("no output")


# In[23]:


#4.Display an employee's gross salary is greater than 40000 then show employee name,designation.

employee_name = "abc"
designation = "manager"
gross_salary = 45000

if gross_salary > 40000:
   print("employee_name: ",employee_name,"\ndesignation: ",designation)
else:
   print("no output")


# In[32]:


#5. Write a python code to take the gross salary of 3 employees, calculate tax as 10% of
# gross salary if employee ‘s gross salary is more than 5 lacks and deduct the tax and
#display the net salary.

g_salary1 = float(input("Enter the gross salary of employee1:"))
g_salary2 = float(input("Enter the gross salary of employee2:"))
g_salary3 = float(input("Enter the gross salary of employee3:"))

if g_salary1 > 500000:
    tax = float(g_salary1/10)
    net_salary = float(g_salary1-tax)
    print("Employee1 tax is: ",tax,"\nEmployee1 net_salary is: ",net_salary)
    
elif g_salary2 > 500000:
    tax = float(g_salary2/10)
    net_salary = float(g_salary2-tax)
    print("Employee2 tax is: ",tax,"\nEmployee2 net_salary is: ",net_salary)

elif g_salary3 > 500000:
    tax = float(g_salary3/10)
    net_salary = float(g_salary3-tax)
    print("Employee3 tax is: ",tax,"\n Employee3 net_salary is: ",net_salary)
    
else:    
    print("no output")


# In[ ]:


#6. Write a python code which display company name and department name with total
# number of employees in each department. Display highest employee total number of
# employees of department.

company_name = "abcd"
mb_dp = 70
cs_dp = 80
it_dp = 90

if mb_dp > cs_dp && mb_dp > it_dp:
    print("Highest employee is: ",mb_dp)

elif

