# Medical Store Management App

A simple Streamlit application for managing medical store data with MySQL backend.

## Features

- Add, update, display, and delete item categories
- Add, update, display, and delete suppliers
- Add, update, display, and delete items
- Uses MySQL for data storage
- Built with Streamlit for a web-based interface

## Project Structure

- `Home Page.py` - main landing page
- `pages/Item Category.py` - category CRUD page
- `pages/Supplier.py` - supplier CRUD page
- `pages/Item.py` - item CRUD page
- `medicalstoredb.sql` - database schema and table creation script

## Database Schema

- `category` — stores category names and descriptions
- `supplier` — stores supplier details including name, contact, state, and country
- `item` — stores medical items with category and supplier relationships

## Requirements

- Python 3.10
- Streamlit
- PyMySQL
- pandas
- MySQL server

## Setup

1. Install Python dependencies:

```bash
py -3.10 -m pip install streamlit pymysql pandas
```

2. Create the MySQL database and tables using `medicalstoredb.sql`.

3. Update database connection settings in the app files if needed:

```python
db = pymysql.connect(host="localhost", user="root", password="root", database="medicalstoredb")
```

## Run

```bash
streamlit run "Home Page.py"
```

## Notes

- Make sure MySQL is running and the database `medicalstoredb` exists.
- Use the app sidebar to navigate between operations.
