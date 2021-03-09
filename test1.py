import mysql.connector
import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='K@lombos123',
    database='testdatabase'
    )

mycursor = db.cursor()

users = [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3")]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"
Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES(%s,%s,%s)"

for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()
mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)
"""""
mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

mycursor.execute(Q1)
mycursor.execute(Q2)

mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)

mycursor.execute("INSERT INTO Person (name, age) VALUES(%s,%s)", ("Elias", 27))
db.commit()


mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE Test2 (name varchar(50), created datetime, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")


mycursor.execute("INSERT INTO Test2 (name, created, gender) VALUES (%s,%s,%s)", ("Pol", datetime.datetime.now(), "O"))
db.commit()

mycursor.execute("SELECT * FROM Test2 WHERE gender = 'F'")

mycursor.execute("SELECT id, name FROM Test2 WHERE gender = 'M' ORDER BY id DESC")

for x in mycursor:
    print(x)

mycursor.execute("ALTER TABLE Test2 ADD COLUMN food VARCHAR(50) NOT NULL")

mycursor.execute("DESCRIBE Test2")
print(mycursor.fetchone())

mycursor.execute("ALTER TABLE Test2 DROP food")

mycursor.execute("ALTER TABLE Test2 CHANGE name first_name VARCHAR(50)")
mycursor.execute("DESCRIBE Test2")
for x in mycursor:
    print(x)
"""""