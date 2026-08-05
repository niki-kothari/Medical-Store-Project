import pymysql

class category:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', database='apollomedicaldb')
        self.cursor = self.db.cursor()

    def addCategory(self):
        ctype = input ('Enter new category type : ')
        if (not ctype):
            print('Category name cannot be null')
            self.addCategory()
        else:
            description = input ('Enter category descriptioon : ')
            sql = "insert into category (c_type, description) values ('%s', '%s')"%(ctype, description)
            self.cursor.execute(sql)
            self.db.commit()

    def updateCategory(self):
        ctype = input('Enter category you want to update : ')
        search_pattern = "%" + ctype + "%"
        sql = "select * from category where c_type like %s"
        self.cursor.execute(sql, (search_pattern,))
        data = self.cursor.fetchone()
        if (not data):
            print('No such category found')
        else:
            cNewType = input ('Enter new category name to update : ')
            cNewDescription = input('Enter new category description to update : ')
            sql = "update category set c_type = '%s', description = '%s' where category_id = %d"%(cNewType, cNewDescription, data[0])
            self.cursor.execute(sql)
            self.db.commit()

    def deleteCategory(self):
        ctype = input('Enter category you want to delete : ')
        search_pattern = "%" + ctype + "%"
        sql = "select * from category where c_type like %s"
        self.cursor.execute(sql, (search_pattern,))
        data = self.cursor.fetchall()
        if (not data):
            print('No such category found')
        else:
            for i in data:
                sql = "delete from category where category_id = '%d'"%(i[0])
                self.cursor.execute(sql)
                self.db.commit()

    def displayCategory (self):
        sql = "select * from category"
        self.cursor.execute(sql)
        categoryList = self.cursor.fetchall()
        print ('Different categories available are : ')
        for cat in categoryList:
            print (f'\tCategory Id : {cat[0]}')
            print (f'\tCategory Name : {cat[1]}')
            print (f'\tCategory Description : {cat[2]}')

#main
if(__name__ == '__main__'):
    try:
        categoryObj = category()
        choice = 1
        while (choice != 0):
            print ('::::: Category Menu :::::')
            print ('1. Add new category')
            print ('2. Update a category')
            print ('3. Delete a category')
            print ('4. Display category')
            print ('0. Exit')
            choice = int(input('Enter your choice : '))
            if (choice == 1):
                categoryObj.addCategory()
                print ('Category added successfully.')
            elif (choice == 2):
                categoryObj.updateCategory()
                print('Category updated successfully.')
            elif (choice == 3):
                categoryObj.deleteCategory()
                print ('Category deleted successfully.')
            elif (choice == 4):
                categoryObj.displayCategory()
            elif (choice == 0):
                print('Thank you.')
            else:
                print ('Wrong choice entered.')
    except Exception as ex:
        print('Unexpected Error : ', ex)
