import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='root',
         host='127.0.0.1',
         database='dbname')

cur = conn.cursor()

query = ("SELECT * FROM stu ")

cur.execute(query)

for (stu_id, stu_name) in cur:
  #print("{}, {}".format(stu_id, stu_name))
  if (stu_id == 4):
  	print ("{}".format(stu_name))
cur.close()
conn.close()