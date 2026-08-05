# 💊 Medical Store Management App

A simple **Streamlit** web application for managing a medical store's inventory — categories, suppliers, and items — backed by a **MySQL** database.

## Features

- 📂 **Item Category** — Add, update, display, and delete item categories
- 🚚 **Supplier** — Add, update, display, and delete supplier records
- 💊 **Item** — Add, update, display, and delete medical items, linked to a category and supplier
- 🗄️ MySQL for persistent data storage
- 🖥️ Multi-page Streamlit interface with sidebar navigation

## Project Structure

```
Medical Store Project/
├── Home Page.py               # Main landing page
├── pages/
│   ├── Item Category.py       # Category CRUD page
│   ├── Supplier.py            # Supplier CRUD page
│   └── Item.py                # Item CRUD page
└── medicalstoredb.sql         # Database schema and table creation script
```

## Database Schema

| Table      | Description                                                  |
|------------|----------------------------------------------------------------|
| `category` | Stores category names and descriptions                        |
| `supplier` | Stores supplier details — name, address, contact, state, country |
| `item`     | Stores medical items, linked to `category` and `supplier`      |

## Requirements

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [PyMySQL](https://pymysql.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- MySQL Server

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/niki-kothari/Medical-Store-Project.git
   cd Medical-Store-Project
   ```

2. **Install dependencies**

   ```bash
   pip install streamlit pymysql pandas
   ```

3. **Create the database**

   Import `medicalstoredb.sql` into your MySQL server (e.g. via MySQL Workbench, phpMyAdmin, or the CLI):

   ```bash
   mysql -u root -p < medicalstoredb.sql
   ```

4. **Configure the database connection**

   Each page connects to MySQL using these default credentials — update them if your setup differs:

   ```python
   db = pymysql.connect(host="localhost", user="root", password="root", database="medicalstoredb")
   ```

## Run

```bash
streamlit run "Home Page.py"
```

The app will open in your browser at `http://localhost:8501`. Use the sidebar to navigate between Categories, Suppliers, and Items.

## Notes

- Ensure the MySQL server is running and the `medicalstoredb` database exists before starting the app.
- This is a learning/demo project and does not include authentication or input sanitization — avoid using it in a production environment as-is.
