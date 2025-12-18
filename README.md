# 🏥 Medical Store Management System

A simple **Medical Store Management System** designed to manage medicines, suppliers, customers, and sales efficiently.  
This project is suitable for learning **database management**, **CRUD operations**, and **basic backend logic** using MySQL.

---

## 📌 Features

- Add, update, delete medical items
- Manage medicine stock
- Supplier management
- Customer details management
- Search items by name or ID
- Automatic stock update after sales

---

## 🛠️ Technologies Used

- Programming Language: Python
- Database: MySQL
- Interface: Console
- Tools: MySQL Workbench, Visual Studio Code

---

## 🗄️ Database Structure

Main tables used:
- `items`
- `suppliers`
- `customers`
- `category`

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/medical-store-management.git
   
2. Import the database:

- Open MySQL Workbench

- Import medical_store_db.sql

3. Configure database connection:

    Update MySQL username, password, and database name in the code

4. Run the application:

    main.py

## 📂 Project Structure
      Medical-Store-Project/
      │
      ├── database/
      │   └── medical_store_db.sql
      ├── src/
      │   ├── items.py
      │   ├── category.py
      │   ├── customers.py
      │   └── main.py
      ├── README.md

## 🎯 Purpose of the Project

Academic mini project

Practice MySQL database concepts

Learn CRUD operations

Understand basic real-world pharmacy workflows

## 📚 Explanation
   **Module : Item Category** <br>
      This module have the CRUD functions on the category table having details like category ID, Category type and its description.

   **Module : Items** <br>
      This module have the CRUD functions on the item table having details like item ID, name, category, rate, quantity, manufacturing date, expiry date, supplier, etc.

   **Module : Customer** <br>
      This module have the CRUD functions on the customer table having details like customer ID, name, address, contact no, etc.
      
## 📸 Screenshots



## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests.

## 📄 License

This project is for educational purposes only.

## 👨‍💻 Author

Niki Kothari
GitHub: https://github.com/niki-kothari
