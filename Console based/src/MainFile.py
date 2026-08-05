import pymysql, category, customer, item
#main
if (__name__ == "__main__"):
    try:
        mainSelection = 1
        while (mainSelection != 0):
            print ('\n:::::: MAIN MENU ::::::\n')
            print ('Select which data you want to access : ')
            print ('1. Items ')
            print ('2. Item Categories')
            print ('3. Customers')
            print ('0. Exit the main program')
            mainSelection  = int (input('Enter your choice :- '))
            if (mainSelection == 1):
                try:
                    itemObj = item.item()
                    selected_choice = 1
                    while (selected_choice != 0):
                        print ('\n:::::Item Menu:::::')
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
                        else:
                            print ('Wrong choice entered.')            
                except pymysql.connect.Error as err:
                    print("❌ MySQL Error:", err)
                except ValueError as ve:
                    print("❌ Date Format Error:", ve)
                except Exception as e:
                    print("❌ Unexpected Error:", e)

            elif (mainSelection == 2):
                try:
                    categoryObj = category.category()
                    choice = 1
                    while (choice != 0):
                        print ('\n::::: Category Menu :::::')
                        print ('1. Add new category')
                        print ('2. Update a category')
                        print ('3. Delete a category')
                        print ('4. Display category')
                        print ('0. Exit Category Menu')
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
                            categoryObj.db.close()
                        else:
                            print ('Wrong choice entered.')
                except Exception as ex:
                    print('Unexpected Error : ', ex)

            elif (mainSelection == 3):
                try:
                    custObj = customer.customer()
                    selected_choice = 1
                    while (selected_choice != 0):
                        print ('\n:::::Customer Menu:::::')
                        print ('1. Insert new customer record')
                        print ('2. Update an existing customer record')
                        print ('3. Delete a customer record')
                        print ('4. Display the details of a customer')
                        print ('0. Exit Customer Menu')
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
                        else:
                            print ('Wrong choice entered.')  
                except pymysql.connect.Error as err:
                    print("❌ MySQL Error:", err)
                except ValueError as ve:
                    print("❌ Date Format Error:", ve)
                except Exception as e:
                    print("❌ Unexpected Error:", e)
    except Exception as ex:
        print ('Error occurred :- ', ex)