from MySQLEmployeeDAO import MySQLEmployeeDAO
from Model.Employee import Employee


employeeDAO = MySQLEmployeeDAO()


peter=Employee('Peter','Svendsen','121299-4321','11111111','peter.sv@andeby.dk')
jakob=Employee('Jakob', 'Larson','100469-0231','88888888','jakob.larsson@dvconsulting.dk')


#employeeDAO.connect()
employeeDAO.setup()
employeeDAO.connect()
employeeDAO.find_all()

employeeDAO.delete_employee(peter)
employeeDAO.delete_employee(jakob)

employeeDAO.insert_employee(jakob)
employeeDAO.find_all()

jakob.set_phone('123456')
employeeDAO.update_employee(jakob)
employeeDAO.find_all()

jakob.set_phone('654321')
jakob.set_last_name('Andersen')
jakob.set_email('jakob@andersen.dk')
employeeDAO.update_employee(jakob)
employeeDAO.find_all()

peter=Employee('Peter','Svendsen','121299-4321','11111111','peter.sv@andeby.dk')
employeeDAO.insert_employee(peter)
employeeDAO.find_all()

employeeDAO.close()




