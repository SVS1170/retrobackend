import psycopg2
import configparser


config = configparser.ConfigParser()
config.read("config.ini")  # читаем конфиг
con = psycopg2.connect(
    database=config["database"]["db"],
    user=config["database"]["user"],
    password=config["database"]["passwd"],
    host=config["database"]["host"],
    port=int(config["database"]["port"])
)

class Postgress_con:
    def init(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port


def create_table(name):
  cur = con.cursor()
  cur.execute(f'''CREATE TABLE {name}  
       (id INT PRIMARY KEY NOT NULL,
       LOGIN TEXT,
       PASSWORD TEXT,
       NAME TEXT,
       FIRSTNAME TEXT,
       EMAIL TEXT);''')
  commit()


def add_column(name, addres):
  cur = con.cursor()
  cur.execute(
    f"ALTER TABLE {name} ADD {addres} TEXT NULL;"
  )
  commit()

def del_column(name, addres):
    cur = con.cursor()
    cur.execute(
      f"ALTER TABLE {name} DROP {addres};"
    )
    commit()


def insert_data(TABLENAME="USERS1", id="1",LOGIN='COCK',PASSWORD="SUCK",NAME="TEST",FIRSTNAME="TEST1",EMAIL="GAVNO@GMAIL.COM"):
  cur = con.cursor()
  cur.execute(
    f"INSERT INTO {TABLENAME} (id,LOGIN,PASSWORD,NAME,FIRSTNAME,EMAIL ) VALUES ('1', 'COCK', 'SUCK', 'TEST', 'TEST1', 'GAVNO@GMAIL.COM');"
  )
  commit()


def read_data(login):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    con = psycopg2.connect(
        database=config["database"]["db"],
        user=config["database"]["user"],
        password=config["database"]["passwd"],
        host=config["database"]["host"],
        port=int(config["database"]["port"])
    )
    cur = con.cursor()
    cur.execute(f"SELECT * from USERS1 where LOGIN = '{login}';")
    rows = cur.fetchall()
    print(rows)
    # for row in rows:
    #     print("id =", row[0])
    #     print("LOGIN =", row[1])
    #     print("PASSWORD =", row[2])
    #     print("NAME =", row[3])
    #     print("FIRSTNAME =", row[4])
    #     print("EMAIL =", row[5], "\n")

    close()
    # id = rows[0][0]
    login = rows[0][1]
    password = rows[0][2]
    name = rows[0][3]
    firstname = rows[0][4]
    email = rows[0][5]
    return login, password, name, firstname, email

def update_data(name):
      cur = con.cursor()
      cur.execute(f"UPDATE {name} set AGE = 20 where id = 3420;")
      commit()


def close():
    con.close()


def commit():
    con.commit()
    con.close()


# insert_data("USERS1")
# print(read_data("COCK"))
# create_table("USERS1")
# add_column("nino", "age")
# del_column("nino", "age")