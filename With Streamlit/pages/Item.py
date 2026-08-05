import pandas as pd
import datetime
import streamlit as st
import pymysql

def getCategoryNames():
    sql = "select c_type from category"
    cursor.execute(sql)
    cats = cursor.fetchall()
    categories = []
    for cat in cats:
        categories.append(cat[0])
    return categories

def getSupplierNames():
    sql = "select concat_ws(' ', fname, lname) from supplier"
    cursor.execute(sql)
    sups = cursor.fetchall()
    suppliers = []
    for sup in sups:
        suppliers.append(sup[0])
    return suppliers

def getcategoryId(categoryName):
    sql = "select category_id from category where c_type = '%s'"%(categoryName)
    cursor.execute(sql)
    category = cursor.fetchone()
    return category[0]

def getSupplierId(supplierName):
    sql = "select supplier_id from supplier where concat_ws(' ', fname, lname) = '%s'"%(supplierName)
    cursor.execute(sql)
    supplier = cursor.fetchone()
    return supplier[0]

db = pymysql.connect(host="localhost", user="root", password="root", database="medicalstoredb")
cursor = db.cursor()

st.set_page_config(page_title="Item")
opRadio = st.sidebar.radio("Select Operation", ['Add Item', 'Update Item', 'Display Item', 'Delete Item'])
st.header("Items Form", divider='blue')

if (opRadio == 'Add Item'):
    with st.form("add_item_form"):
        st.subheader("Enter item details : ")

        categories = getCategoryNames()
        selectedCategory = st.selectbox("Select Category", categories)

        item_name = st.text_input("Enter Item name : ", placeholder="Enter item name here")

        suppliers = getSupplierNames()
        selectedSupplier = st.selectbox("Select Supplier", suppliers)

        description = st.text_area("Enter Description : ", height=50)
        rate = st.number_input("Enter Item Rate : ")
        stock_qty = st.number_input("Enter Item Quantity : ", value=10)
        mfd_date = st.date_input("Enter manufacturing date : ")
        exp_date = st.date_input("Enter expiry date : ")

        if(st.form_submit_button("Add Item")):
            category_id = getcategoryId(selectedCategory)
            supplier_id = getSupplierId(selectedSupplier)
            sql = "insert into item (category_id, i_name, supplier_id, description, rate, quantity, mfd_date, exp_date) values (%d, '%s', %d, '%s', %d, %d, '%s', '%s')"%(category_id, item_name, supplier_id, description, rate, stock_qty, mfd_date, exp_date)
            cursor.execute(sql)
            db.commit()
            st.success("Item added Successfully")

elif (opRadio == 'Update Item'):
    st.subheader("Enter item details to Update", divider='blue')
    opSb = st.selectbox("Update by", ['Item ID', 'Item Name'])
    if (opSb == 'Item ID'):
        sql = "select item_id from item"
        cursor.execute(sql)
        items = cursor.fetchall()
        item_ids = [item[0] for item in items]
        selectItem = st.selectbox("Select Item ID to update", item_ids)
        sql = "select * from item where item_id = %d"%(selectItem)
        cursor.execute(sql)
        item = cursor.fetchone()
    else:
        sql = "select i_name from item"
        cursor.execute(sql)
        items = cursor.fetchall()
        item_names = [item[0] for item in items]
        selectItem = st.selectbox("Select Item Name to update", item_names)
        sql = "select * from item where i_name = '%s'"%(selectItem)
        cursor.execute(sql)
        item = cursor.fetchone()
    if (item):
        st.text_input("Item ID", value=item[0], disabled=True)
        categories = getCategoryNames()
        current_category = ''
        if item[2] is not None:
            cursor.execute("select c_type from category where category_id = %d" % item[2])
            temp = cursor.fetchone()
            current_category = temp[0] if temp else ''
        selectedCategory = st.selectbox("Select Category", categories, index=categories.index(current_category) if current_category in categories else 0)
        item_name = st.text_input("Enter Item name", value=item[1])
        suppliers = getSupplierNames()
        current_supplier = ''
        if item[3] is not None:
            cursor.execute("select concat_ws(' ', fname, lname) from supplier where supplier_id = %d" % item[3])
            temp = cursor.fetchone()
            current_supplier = temp[0] if temp else ''
        selectedSupplier = st.selectbox("Select Supplier", suppliers, index=suppliers.index(current_supplier) if current_supplier in suppliers else 0)
        description = st.text_area("Enter Description", value=item[4], height=50)
        rate = st.number_input("Enter Item Rate", value=float(item[5]) if item[5] is not None else 0.0)
        stock_qty = st.number_input("Enter Item Quantity", value=item[6] if item[6] is not None else 0)
        mfd_date = st.date_input("Enter manufacturing date", value=item[7] if item[7] is not None else datetime.date.today())
        exp_date = st.date_input("Enter expiry date", value=item[8] if item[8] is not None else datetime.date.today())
        if(st.button("Update Item")):
            category_id = getcategoryId(selectedCategory)
            supplier_id = getSupplierId(selectedSupplier)
            sql = "update item set category_id=%d, i_name='%s', supplier_id=%d, description='%s', rate=%d, quantity=%d, mfd_date='%s', exp_date='%s' where item_id=%d"%(category_id, item_name, supplier_id, description, rate, stock_qty, mfd_date, exp_date, item[0])
            cursor.execute(sql)
            db.commit()
            st.success("Item updated successfully")

elif (opRadio == 'Display Item'):
    sql = "select i.item_id, i.i_name, c.c_type as category, concat_ws(' ', s.fname, s.lname) as supplier, i.description, i.rate, i.quantity, i.mfd_date, i.exp_date from item i left join category c on i.category_id = c.category_id left join supplier s on i.supplier_id = s.supplier_id"
    cursor.execute(sql)
    items = cursor.fetchall()
    df = pd.DataFrame(items, columns=['Item ID', 'Item Name', 'Category', 'Supplier', 'Description', 'Rate', 'Quantity', 'Manufacture Date', 'Expiry Date'])
    st.header("List of items")
    st.dataframe(df)

elif (opRadio == 'Delete Item'):
    st.subheader("Select item details to Delete", divider='blue')
    opSb = st.selectbox("Delete by", ['Item ID', 'Item Name'])
    if (opSb == 'Item ID'):
        sql = "select item_id from item"
        cursor.execute(sql)
        items = cursor.fetchall()
        item_ids = [item[0] for item in items]
        selectItem = st.selectbox("Select Item ID to delete", item_ids)
        sql = "select * from item where item_id = %d"%(selectItem)
        cursor.execute(sql)
        item = cursor.fetchone()
    else:
        sql = "select i_name from item"
        cursor.execute(sql)
        items = cursor.fetchall()
        item_names = [item[0] for item in items]
        selectItem = st.selectbox("Select Item Name to delete", item_names)
        sql = "select * from item where i_name = '%s'"%(selectItem)
        cursor.execute(sql)
        item = cursor.fetchone()
    if (item):
        st.text_input("Item ID", value=item[0], disabled=True)
        selectedCategory = st.text_input("Category ID", value=item[2], disabled=True)
        item_name = st.text_input("Enter Item name", value=item[1])
        selectedSupplier = st.text_input("Supplier ID", value=item[3], disabled=True)
        description = st.text_area("Enter Description", value=item[4], height=50)
        rate = st.number_input("Enter Item Rate", value=float(item[5]) if item[5] is not None else 0.0)
        stock_qty = st.number_input("Enter Item Quantity", value=item[6] if item[6] is not None else 0)
        mfd_date = st.date_input("Enter manufacturing date", value=item[7] if item[7] is not None else datetime.date.today())
        exp_date = st.date_input("Enter expiry date", value=item[8] if item[8] is not None else datetime.date.today())
        if(st.button("Delete Item")):
            sql = "delete from item where item_id=%d"%(item[0])
            cursor.execute(sql)
            db.commit()
            st.success("Item deleted successfully")