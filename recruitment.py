import mysql.connector
con_o=mysql.connector.connect(host="localhost",user="root",password="",database="recruitment")
cur_o=con_o.cursor()

#code for deleting all the rows to get a new table
'''truncate_query = "TRUNCATE TABLE studentman"
cur_o.execute(truncate_query)
con_o.commit()'''
#end

###actual code (querying)
'''
#description of table
q1="desc studentman"
cur_o.execute(q1)
table=cur_o.fetchall()h
print("\n\tTable Description")
for atr in table
    print(atr)
print("\n\t---------------------end----------------\n")
#'''

a=input("Name: ")
b=input("Age: ")
c=input("Qualification: ")
d=input("Years of Experience: ")
e=input("Contact: ")
#insert code
q2=f"INSERT INTO recruitment_info(Name, Age, Qualification, Years of Experience, Contact) VALUES ('{a}','{b}','{c}','{d}','{e}')"
cur_o.execute(q2)
con_o.commit()
##ending steps
cur_o.close()
con_o.close()