from Persistent.EmployeeDAO import EmployeeDAO
from Model.Employee import Employee
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
from Persistent.EmpSearchType import EmpSearchType
from typing import List  # needed to be able to declare list type


class MySQLEmployeeDAO(EmployeeDAO):
    DB_NAME = 'kuplanner'

    __pool__: pooling.MySQLConnectionPool
    __cnx__: mysql.connector.connection = None
    cursor = None

    @classmethod
    def create_database(cls):

        cls.__cnx__ = mysql.connector.connect( user='kuplanner',
                                               password='kuplanner123',
                                               host='127.0.0.1')
        cursor = cls.__cnx__.cursor()
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(cls.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    @classmethod
    def setup(cls):
        cls.__cnx__ = mysql.connector.connect(user='kuplanner',
                                              password='kuplanner123',
                                              host='127.0.0.1')

        cursor = cls.__cnx__.cursor()
        try:
            cursor.execute("USE {}".format(cls.DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(cls.DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                cls.create_database()
                print("Database {} created successfully.".format(cls.DB_NAME))
                cls.__cnx__.database = cls.DB_NAME
            else:
                print(err)
                exit(1)

        create = """
        DROP TABLE IF EXISTS `employee`;
        CREATE TABLE `employee` (
            `idEmployee` int NOT NULL AUTO_INCREMENT,
              `firstName` varchar(45) NOT NULL,
              `lastName` varchar(45) NOT NULL,
              `cpr` varchar(45) NOT NULL,
              `phone` varchar(45) DEFAULT NULL,
              `email` varchar(45) DEFAULT NULL,
              PRIMARY KEY (`idEmployee`),
                UNIQUE KEY `cpr_UNIQUE` (`cpr`)
            ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        INSERT INTO `employee` VALUES (17,'Jakob','Andersen','100469-0231','654321','jakob@andersen.dk'),(18,'Peter','Svendsen','121299-4321','11111111','peter.sv@andeby.dk');
        """
        with cls.__cnx__.cursor() as cursor:
            cursor.execute(create)

    @classmethod
    def connect(cls):
        try:
            cls.__pool__ = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, user='kuplanner',
                                                       password='kuplanner123',
                                                       host='127.0.0.1', database=cls.DB_NAME)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        # else:
        #     cls.__cnx__.close()

        cls.__cnx__ = cls.__pool__.get_connection()
        print("connection", cls.__cnx__)

    def close(cls):
        if cls.__cnx__ is not None:
            cls.__cnx__.close()

    @classmethod
    def insert_employee(cls, emp: Employee):
        firstname = emp.get_first_name()
        lastname = emp.get_last_name()
        cpr = emp.get_cpr_number()
        phone = emp.get_phone()
        email = emp.get_email()

        insert = """
                INSERT into kuplanner.employee (firstName, lastName, cpr, phone, email)  
                VALUES ("%s", "%s", "%s", "%s", "%s") 
                """ % (firstname, lastname, cpr, phone, email)

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(insert)
            cls.__cnx__.commit()

    @classmethod
    def update_employee(cls, emp: Employee):
        firstname = emp.get_first_name()
        lastname = emp.get_last_name()
        cpr = emp.get_cpr_number()
        phone = emp.get_phone()
        email = emp.get_email()

        update = """
        UPDATE kuplanner.employee 
        SET firstName = "%s", lastName = "%s", phone = "%s", email = "%s" 
        WHERE cpr="%s"
        """ % (firstname, lastname, phone, email, cpr)

        # cls.__cnx__ = mysql.connector.connect(pool_name="mypool")

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(update)
            cls.__cnx__.commit()

    @classmethod
    def delete_employee(cls, emp: Employee):
        cpr = emp.get_cpr_number()

        delete = """
                DELETE FROM kuplanner.employee 
                WHERE cpr="%s"
                """ % cpr

        # cls.__cnx__ = mysql.connector.connect(pool_name="mypool")

        with cls.__cnx__.cursor(dictionary=True) as cursor:
            cursor.execute(delete)
            cls.__cnx__.commit()

    def find_employee_by_property(self, search_type: EmpSearchType, value: object) -> List[Employee]:
        pass

    @classmethod
    def find_all(cls) -> List[Employee]:

        query = "SELECT * FROM kuplanner.employee"
        print("findall connection", cls.__cnx__)
        cursor = cls.__cnx__.cursor(dictionary=True)
        # with cls.__cnx__.cursor(dictionary = True) as cursor:
        cursor.execute(query)
        all_employees = cursor.fetchall()
        print(all_employees)
        print(cls.__pool__)
        return all_employees
