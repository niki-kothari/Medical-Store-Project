import pymysql, re
from datetime import datetime 

class customer: 
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', database='apollomedicaldb')
        self.cursor = self.db.cursor()

    def addCustomer(self):
        cid = int(input('Enter customer id : '))
        fname = input('Enter your first name : ')
        lname = input('Enter your last name : ')
        add = input('Enter address : ')
        area = input('Enter area : ')
        city = input('Enter city : ')
        state = input('Enter state : ')
        country = input('Enter country : ')
        phno = input('Enter mobile number : ')
        while (not self.isValidPhNo(phno)):
            print('Phone Number should contain only 10 digits')
            phno = input('Enter mobile number : ')
        dob = input('Enter date of birth (yyyy-mm-dd): ')
        dob = datetime.strptime(dob, '%Y-%m-%d').date()
        sql = "insert into customer values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(cid, fname, lname, add, area, city, state, country, phno, dob)
        self.cursor.execute(sql)
        self.db.commit()
        print ('\nData added successfully.')

    def isValidPhNo(self, phno):
        pattern = re.compile(r'^\d{10}$')
        return bool(pattern.match(phno))

    def isAvailable(self, field, field_value):
        sql = "select * from customer where %s = '%s'"%(field, field_value)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return True if (data) else False

    def updateCustomer(self, cid):
        sql = "select * from customer where cust_id = '%d'"%(cid)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        print ('\nWhich data you want to update?')
        print ('1. Name')
        print ('2. Address')
        print ('3. Mobile Number')
        print ('4. Date Of Birth')
        curr_selection = int(input('Select your choice (1/2/3/4): '))
        if (curr_selection == 1):
            fname = input('Enter your first name to update : ')
            lname = input('Enter your last name to update : ')
            sql = "update customer set c_fname = '%s', c_lname = '%s' where cust_id = '%d'"%(fname, lname, cid)
            self.cursor.execute(sql)
            self.db.commit()
            print ('Name updated successfully.')
        elif (curr_selection == 2):
            add1 = input('Enter new flat/bunglow number : ')
            area = input('Enter new area to update : ')
            city = input('Enter new city to update : ')
            state = input('Enter new state to update : ')
            country = input('Enter new country to update : ')
            sql = "update customer set c_address = '%s', c_area = '%s', c_city = '%s', c_state = '%s', c_country = '%s' where cust_id = '%d'"%(add1, area, city, state, country, cid)
            self.cursor.execute(sql)
            self.db.commit()
            print ('Address updated successfully.')
        elif (curr_selection == 3):
            phno = input('Enter your new mobile number : ')
            while (not self.isValidPhNo(phno)):
                print('Mobile number should contain only 10 digits.')
                phno = input('Enter your new mobile number : ')
            sql = "update customer set c_ph_no = '%s' where cust_id = '%d'"%(phno, cid)
            self.cursor.execute(sql)
            self.db.commit()
            print ('Mobile number updated successfully.')
        elif (curr_selection == 4):
            dob = input('Enter date of birth to update (yyyy-mm-dd): ')
            sql = "update customer set c_dob = '%s' where cust_id = '%d'"%(dob, cid)
            self.cursor.execute(sql)
            self.db.commit()
            print ('Date of birth updated successfully.')

    def deleteCustomer(self, cid):
        sql = "delete from customer where cust_id = '%d'"%(cid)
        self.cursor.execute(sql)
        self.db.commit()
        print('Record deleted.')

    def displayCustomer(self, cust=''):
        print ('\nSelect display type : ')
        print ('1. List all customers')
        print ('2. List particular customer details by customer id')
        print ('3. List all customers by particular field')
        curr_choice = int(input('Enter your choice : '))
        if (curr_choice == 1):
            self.displayAllCustomer()
        elif (curr_choice == 2):
            cid = int(input('Enter customer id whose detail you want to display : '))
            self.displayCustomerById(cid)
        elif (curr_choice == 3):
            field = input('Enter field name of which you want customers record : ')
            field_value = input(f'Enter {field} value for details : ')
            self.displayCustomerByField(field, field_value)
        else:
            print('Wrong choice entered.')

    def displayAllCustomer(self):        
        sql = "select * from customer"
        self.cursor.execute(sql)
        customer_list = self.cursor.fetchall()
        for cust in customer_list:
            self.printCustomerDetail(cust)

    def displayCustomerById(self, cid):
        sql = "select * from customer where cust_id = '%d'"%(cid)
        self.cursor.execute(sql)
        cust = self.cursor.fetchone()
        if (cust): 
            self.printCustomerDetail(cust)
        else:
            print('No such customer found')

    def displayCustomerByField(self, field, field_value):
            sql = "select * from customer where %s='%s'"%(field, field_value)
            self.cursor.execute(sql)
            customer_list = self.cursor.fetchall()
            if (customer_list): 
                for cust in customer_list:
                    self.printCustomerDetail(cust)
            else:
                print('No such customer found')                

    def printCustomerDetail(self, cust):
        print ('\nCustomer Details: ')
        print (f'\tCustomer Id : {cust[0]}')
        print (f'\tCustomer Name : {cust[1]} {cust[2]}')
        print (f'\tCustomer Address : {cust[3]},{cust[4]},{cust[5]}.')
        print (f'\tCustomer Mobile No.  : {cust[8]}')
        print (f'\tCustomer Date Of Birth : {cust[9]}')

#main
if (__name__ =="__main__"):
    try:
        custObj = customer()
        selected_choice = 1
        while (selected_choice != 0):
            print ('\n:::::MENU:::::')
            print ('1. Insert new customer record')
            print ('2. Update an existing customer record')
            print ('3. Delete a customer record')
            print ('4. Display the details of a customer')
            print ('0. Exit')
            selected_choice = int(input('Please enter what operation you want to perform : '))
            if (selected_choice == 1):
                custObj.addCustomer()
            elif (selected_choice == 2):
                curr_cid = int(input('Enter customer id whose data you want to update : '))
                custObj.updateCustomer(curr_cid)
            elif (selected_choice == 3):
                curr_cid = int(input('Enter customer id whose data you want to delete : '))
                custObj.deleteCustomer(curr_cid)
            elif (selected_choice == 4):
                custObj.displayCustomer()
            elif (selected_choice == 0):
                custObj.db.close()
                print ('\nThank you')
            else:
                print ('Wrong choice entered.')
    except pymysql.connect.Error as err:
        print("❌ MySQL Error:", err)
    except ValueError as ve:
        print("❌ Date Format Error:", ve)
    except Exception as e:
        print("❌ Unexpected Error:", e)