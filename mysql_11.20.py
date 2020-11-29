import pymysql

connection = pymysql.connect(host='localhost',
                             user='vitya',
                             password='123',
                             db='mydb')
cursor=connection.cursor()


delete_query1="DELETE FROM `mydb`.`table1` WHERE (`id` = '23');"
delete_query2="DELETE FROM `mydb`.`journal` WHERE (`table1_id` = '23');"
insert_query1="INSERT INTO `mydb`.`table1` (`id`, `Surname`, `Name`, `SecondName`) VALUES ('23', 'Формальный', 'Теста', 'Уроженец');"
insert_query2="INSERT INTO `mydb`.`journal` (`table1_id`, `score`) VALUES ('23', '100');"
update_query1="UPDATE table1 INNER JOIN journal ON table1.id=journal.table1_id SET Result='Зачет' WHERE score>9;"
update_query2="UPDATE table1 INNER JOIN journal ON table1.id=journal.table1_id SET Result='Незачет' WHERE score<=9;"
NULLIFIER_query1="UPDATE table1 SET Result=NULL;"
NULLIFIER_query2="UPDATE journal SET score=NULL;"
RANDOMIZE_query="UPDATE journal SET score = FLOOR(RAND()*(20)) WHERE score IS NULL;"
select_query="SELECT table1.Surname, table1.Result FROM table1, journal WHERE table1.id=journal.table1_id and Result='Зачет' ORDER BY table1.id;"


try:
    cursor.execute(delete_query2)
    connection.commit()
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(delete_query1)
    connection.commit()
    print("Неизвестная жертва пала!")
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(insert_query1)
    connection.commit()
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(insert_query2)
    connection.commit()
    print("Свежее мясо!")
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(NULLIFIER_query1)
    connection.commit()
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()
try:
    cursor.execute(NULLIFIER_query2)
    connection.commit()
    print("NULLIFIED!")
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(RANDOMIZE_query)
    connection.commit()
    print("RANDOMIZED!")
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()


try:
    cursor.execute(update_query1)
    connection.commit()
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(update_query2)
    connection.commit()
    print("Score updated!")
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

try:
    cursor.execute(select_query)
    connection.commit()
except Exception as e:
    print("Exception occured:", e)
    connection.rollback()

for x in cursor:
    print(x)


connection.close()