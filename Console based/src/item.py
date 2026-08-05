import pymysql
from datetime import datetime, date

class item: 
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', database='apollomedicaldb')
        self.cursor = self.db.cursor()

    def addItem(self):
        itemId = int(input('Enter item id : '))
        categoryId = int(input('Enter category id : '))
        iname = input('Enter item name : ')
        supplierId = int(input('Enter supplier id : '))
        description = input('Enter description of the item : ')
        i_rate = float(input('Enter rate of the item : '))
        iStockQty = int(input('Enter stock quantity of the item : '))
        rackId = int(input('Enter location rack id : '))
        iMfgDate = input('Enter manufacturing date (yyyy-mm-dd): ')
        iMfgDate = datetime.strptime(iMfgDate, '%Y-%m-%d').date()
        iExpDate = input('Enter expiry date (yyyy-mm-dd): ')
        iExpDate = datetime.strptime(iExpDate, '%Y-%m-%d').date()
        while (iMfgDate > iExpDate or iMfgDate > date.today()):
            print ('Manufacturing date cannot be greater than today or Expiry Date.')
            iMfgDate = input('Enter manufacturing date (yyyy-mm-dd): ')
            iMfgDate = datetime.strptime(iMfgDate, '%Y-%m-%d').date()
            iExpDate = input('Enter expiry date (yyyy-mm-dd): ')
            iExpDate = datetime.strptime(iExpDate, '%Y-%m-%d').date()

        sql = "insert into item values(%d,%d,'%s',%d,'%s',%d,%d,'%s','%s',%d)"%(itemId, categoryId, iname, supplierId, description, i_rate, iStockQty, iMfgDate, iExpDate, rackId)
        self.cursor.execute(sql)
        self.db.commit()
        print ('\nData added successfully.')

    def updateItemDetail(self, field, field_value, id):
            sql = "update item set %s = '%s' where item_id = %d"%(field, field_value, id)
            self.cursor.execute(sql)
            self.db.commit()

    def updateItem(self):
        itemId = int(input('Enter Item ID which item details you want to update : '))
        if (not self.isAvailable('item_id', itemId)):
            print ('No such record found.')
        else:
            print ('\nWhich data you want to update?')
            print ('1. Item Name')
            print ('2. Item Rate')
            print ('3. Item Stock')
            print ('4. Item Rack Location')
            print ('5. Item Category')
            curr_selection = int(input('Select your choice : '))
            if (curr_selection == 1):
                iname = input('Enter item name to update : ')
                self.updateItemDetail('i_name',iname, itemId)
                print ('Item Name updated successfully.')
            elif (curr_selection == 2):
                irate = input('Enter item rate to update : ')
                self.updateItemDetail('i_rate',irate, itemId)
                print ('Item Rate updated successfully.')
            elif (curr_selection == 3):
                istock = input('Enter item stock to update : ')
                self.updateItemDetail('i_stock_qty',istock, itemId)
                print ('Item stock updated successfully.')
            elif (curr_selection == 4):
                irack = input('Enter item rack location to update : ')
                irack = self.getRackId(irack)
                self.updateItemDetail('rack_id',irack, itemId)
                print ('Rack location updated successfully.')
            elif (curr_selection == 5):
                icategory = input('Enter item category to update : ')
                icategory = self.getCategoryId(icategory)
                self.updateItemDetail('category_id',icategory, itemId)
                print ('Item Category updated successfully.')
            else:
                print('Wrong choice entered.')

    def isAvailable(self, field, field_value):
        sql = "select * from item where %s = '%s'"%(field, field_value)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return True if (data) else False
    
    def deleteItem(self):
        print('By which field you want to delete the item records?')
        print('1. By Item Id')
        print('2. By Item Category')
        print('3. By Supplier')
        print('4. By Item Name')
        curr_choice = int(input('Enter your choice : '))
        if (curr_choice == 1):
            field_value = int(input('Enter Item Id which item you want to delete : '))
            self.deleteItemByField('item_id', field_value)
        elif (curr_choice == 2):
            field_value = input('Enter Category whose all items you want to delete : ')
            field_value = self.getCategoryId(field_value)
            self.deleteItemByField('category_id', field_value)
        elif (curr_choice == 3):
            field_value = input('Enter Supplier name whose all items you want to delete : ')
            field_value = self.getSupplierId(field_value)
            self.deleteItemByField('supplier_id', field_value)
        elif (curr_choice == 4):
            field_value = input('Enter Item Name which item you want to delete : ')
            self.deleteItemByField('item_name', field_value)
        else:
            print('Wrong choice entered.')

    def deleteItemByField(self, field, field_value):
        if (self.isAvailable, field, field_value):
            sql = "delete from item where %s = '%s'"%(field, field_value)
            self.cursor.execute(sql)
            self.db.commit()
            print('Record deleted.')
        else:
            print('No such item found')

    def getCategoryId(self, field_value):
        sql = "select category_id from category where c_type = '%s'"%(field_value)
        self.cursor.execute(sql)
        id = self.cursor.fetchone()
        return id[0] if (id) else False
        
    def getSupplierId(self, field_value):
        sql = "select supplier_id from supplier where s_fname like '%s'"%(field_value)
        self.cursor.execute(sql)
        id = self.cursor.fetchone()
        return id[0] if (id) else False
    
    def getRackId(self, field_value):
        sql = "select rack_id from rack where location = '%s'"%(field_value)
        self.cursor.execute(sql)
        id = self.cursor.fetchone()
        return id[0] if (id) else False

    def displayItem(self, cust=''):
        print ('\nSelect display type : ')
        print ('1. List all items')
        print ('2. List particular item details by item id')
        print ('3. List items by item category')
        print ('4. List items by supplier')
        print ('5. List items by rack location')
        curr_choice = int(input('Enter your choice : '))
        if (curr_choice == 1):
            self.displayAllItem()
        elif (curr_choice == 2):
            itemId = int(input('Enter item id whose detail you want to display : '))
            self.displayItemById(itemId)
        elif (curr_choice == 3):
            field_value = input('Enter which category items you want to display : ')
            field_value = self.getCategoryId(field_value)
            if (field_value == False):
                print ('No such category found')
            else:
                self.displayItemByField('category_id', field_value)
        elif (curr_choice == 4):
            field = 'supplier_id'
            field_value = input('Enter supplier name whose items you want to display : ')
            field_value = self.getSupplierId(field_value)
            if (field_value == False):
                print ('No such category found')
            else:
                self.displayItemByField(field, field_value)
        elif (curr_choice == 5):
            field = 'rack_id'
            field_value = input('Enter which rack location items you want to display : ')
            field_value = self.getRackId(field_value)
            self.displayItemByField(field, field_value)
            if (field_value == False):
                print ('No such category found')
            else:
                print('Wrong choice entered.')

    def displayAllItem(self):
            sql = "select * from item"
            self.cursor.execute(sql)
            item_list = self.cursor.fetchall()
            for item in item_list:
                self.printItemDetail(item)

    def displayItemById(self, itemid):
        sql = "select * from item where item_id = '%d'"%(itemid)
        self.cursor.execute(sql)
        item = self.cursor.fetchone()
        if (self.isAvailable('item_id', itemid)):
            self.printItemDetail(item)
        else:
            print('Item ID not found.')

    def displayItemByField(self, field, field_value):
            sql = "select * from item where %s='%s'"%(field, field_value)
            self.cursor.execute(sql)
            item_list = self.cursor.fetchall()
            for item in item_list:
                self.printItemDetail(item)

    def printItemDetail(self, item):
        print ('\nItem Details: ')
        print (f'\tItem Id : {item[0]}')
        print (f'\tItem Category : {item[1]}')
        print (f'\tItem Name : {item[2]}')
        print (f'\tItem Supplier Id : {item[3]}')
        print (f'\tItem Description : {item[4]}')
        print (f'\tItem Rate  : {item[5]}')
        print (f'\tItem Stock available : {item[6]}')
        print (f'\tItem Manufacturing Date : {item[7]}')
        print (f'\tItem Expiry Date : {item[8]}')
        print (f'\tItem Location Id : {item[9]}')
'''
#main
if (__name__ =="__main__"):
    try:
        itemObj = item()
        selected_choice = 1
        while (selected_choice != 0):
            print ('\n:::::MENU:::::')
            print ('1. Insert new item record')
            print ('2. Update an existing item record')
            print ('3. Delete an item record')
            print ('4. Display the details of an item')
            print ('0. Exit Item Menu')
            selected_choice = int(input('Please enter what operation you want to perform : '))

            if (selected_choice == 1):
                itemObj.addItem()
            elif (selected_choice == 2):
                itemObj.updateItem()
            elif (selected_choice == 3):
                itemObj.deleteItem()
            elif (selected_choice == 4):
                itemObj.displayItem()
            elif (selected_choice == 0):
                itemObj.db.close()
                print ('\nThank you')            
            else:
                print ('Wrong choice entered.')            
    
    except pymysql.connect.Error as err:
        print("❌ MySQL Error:", err)
    except ValueError as ve:
        print("❌ Date Format Error:", ve)
    except Exception as e:
        print("❌ Unexpected Error:", e)
'''