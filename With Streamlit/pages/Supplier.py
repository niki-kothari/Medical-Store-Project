import pandas as pd
import streamlit as st
import pymysql
import re

def checkEmail(email):
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    return re.match(regex, email)

def isNull(checkString):
    return True if (checkString == None or checkString == "" or checkString==" ") else False

db = pymysql.connect(host="localhost", user="root", password="root", database="medicalstoredb")
cursor = db.cursor()

st.set_page_config(page_title="Supplier")

opRadio = st.sidebar.radio("Select Operation", ['Add Supplier', 'Update Supplier', 'Display Supplier', 'Delete Supplier'])
st.header("Supplier Form", divider='blue')

if (opRadio == 'Add Supplier'):
    status = True
    st.subheader("Enter Supplier details : ")

    col1, col2 = st.columns([1,1])
    with col1:
        fname = st.text_input("Enter supplier first name")
    with col2:
        if (isNull(fname)):
            st.warning("⚠️ You must enter first name.")
            status = False

    lname = st.text_input("Enter supplier last name")
    if (not lname):
        st.warning("You must enter last name.")
        status = False
    add = st.text_area("Enter address")
    if (not add):
        st.warning("Address cannot be blank.")
        status = False
    area = st.text_input("Enter area")
    city = st.text_input("Enter city")
    state = st.text_input("Enter state")
    country = st.text_input("Enter country")
    ph_no = st.number_input("Enter mobile number : ", value=None, placeholder="Enter maximum 10 digits", max_value=9999999999)

    #check email when text change in text box
    email = st.text_input("Enter email : ", placeholder="abc@domain.com")
    if (not checkEmail(email)):
        st.warning("Enter valid email address")
        status = False
    pan_no = st.number_input("Enter PAN number : ", value=None, max_value=9999999999)
    if (st.button("Add Supplier")):
        if (status == True):
            sql = "insert into supplier (fname, lname, address, area, city, state, country, ph_no, email, pan_no) values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')"%(fname, lname, add, area, city, state, country, ph_no, email, pan_no)
            cursor.execute(sql)
            db.commit()
            st.success("Supplier added successfully")
        else:
            st.error("Please enter all valid values")

elif (opRadio == 'Update Supplier'):
    st.subheader("Enter Supplier details to Update", divider='blue')
    opSb = st.selectbox("Update by", ['Supplier ID', 'Supplier Name'])
    if (opSb == 'Supplier ID'):
        sql = "select supplier_id from supplier"
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        supplier_ids = [sup[0] for sup in suppliers]
        selectSup = st.selectbox("Select Supplier ID to update", supplier_ids)
        sql = "select * from supplier where supplier_id = %d"%(selectSup)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if (sup):
            st.text_input("Supplier ID", value=sup[0], disabled=True)
            fname = st.text_input("First name", value=sup[1])
            lname = st.text_input("Last name", value=sup[2])
            add = st.text_area("Address", value=sup[3])
            area = st.text_input("Area", value=sup[4])
            city = st.text_input("City", value=sup[5])
            state = st.text_input("State", value=sup[6])
            country = st.text_input("Country", value=sup[7])
            ph_no = st.text_input("Phone", value=sup[8])
            email = st.text_input("Email", value=sup[9])
            pan_no = st.text_input("PAN", value=sup[10])
            if (st.button("Update Supplier")):
                sql = "update supplier set fname='%s', lname='%s', address='%s', area='%s', city='%s', state='%s', country='%s', ph_no='%s', email='%s', pan_no='%s' where supplier_id=%d"%(fname, lname, add, area, city, state, country, ph_no, email, pan_no, sup[0])
                cursor.execute(sql)
                db.commit()
                st.success("Supplier details updated successfully.")
    else:
        sql = "select concat_ws(' ', fname, lname) from supplier"
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        supplier_names = [sup[0] for sup in suppliers]
        selectSup = st.selectbox("Select Supplier Name to update", supplier_names)
        sql = "select * from supplier where concat_ws(' ', fname, lname) = '%s'"%(selectSup)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if (sup):
            st.text_input("Supplier ID", value=sup[0], disabled=True)
            fname = st.text_input("First name", value=sup[1])
            lname = st.text_input("Last name", value=sup[2])
            add = st.text_area("Address", value=sup[3])
            area = st.text_input("Area", value=sup[4])
            city = st.text_input("City", value=sup[5])
            state = st.text_input("State", value=sup[6])
            country = st.text_input("Country", value=sup[7])
            ph_no = st.text_input("Phone", value=sup[8])
            email = st.text_input("Email", value=sup[9])
            pan_no = st.text_input("PAN", value=sup[10])
            if (st.button("Update Supplier")):
                sql = "update supplier set fname='%s', lname='%s', address='%s', area='%s', city='%s', state='%s', country='%s', ph_no='%s', email='%s', pan_no='%s' where supplier_id=%d"%(fname, lname, add, area, city, state, country, ph_no, email, pan_no, sup[0])
                cursor.execute(sql)
                db.commit()
                st.success("Supplier details updated successfully.")

elif (opRadio == 'Display Supplier'):
    sql = "select * from supplier"
    cursor.execute(sql)
    suppliers = cursor.fetchall()
    df = pd.DataFrame(suppliers, columns=['Supplier ID', 'First Name', 'Last Name', 'Address', 'Area', 'City', 'State', 'Country', 'Phone', 'Email', 'PAN'])
    st.header("List of suppliers")
    st.dataframe(df)

elif (opRadio == 'Delete Supplier'):
    st.subheader("Select Supplier details to Delete", divider='blue')
    opSb = st.selectbox("Delete by", ['Supplier ID', 'Supplier Name'])
    if (opSb == 'Supplier ID'):
        sql = "select supplier_id from supplier"
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        supplier_ids = [sup[0] for sup in suppliers]
        selectSup = st.selectbox("Select Supplier ID to delete", supplier_ids)
        sql = "select * from supplier where supplier_id = %d"%(selectSup)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if (sup):
            st.text_input("Supplier ID", value=sup[0], disabled=True)
            fname = st.text_input("First name", value=sup[1])
            lname = st.text_input("Last name", value=sup[2])
            add = st.text_area("Address", value=sup[3])
            area = st.text_input("Area", value=sup[4])
            city = st.text_input("City", value=sup[5])
            state = st.text_input("State", value=sup[6])
            country = st.text_input("Country", value=sup[7])
            ph_no = st.text_input("Phone", value=sup[8])
            email = st.text_input("Email", value=sup[9])
            pan_no = st.text_input("PAN", value=sup[10])
            if (st.button("Delete Supplier")):
                sql = "delete from supplier where supplier_id=%d"%(sup[0])
                cursor.execute(sql)
                db.commit()
                st.success("Supplier deleted successfully.")
    else:
        sql = "select concat_ws(' ', fname, lname) from supplier"
        cursor.execute(sql)
        suppliers = cursor.fetchall()
        supplier_names = [sup[0] for sup in suppliers]
        selectSup = st.selectbox("Select Supplier Name to delete", supplier_names)
        sql = "select * from supplier where concat_ws(' ', fname, lname) = '%s'"%(selectSup)
        cursor.execute(sql)
        sup = cursor.fetchone()
        if (sup):
            st.text_input("Supplier ID", value=sup[0], disabled=True)
            fname = st.text_input("First name", value=sup[1])
            lname = st.text_input("Last name", value=sup[2])
            add = st.text_area("Address", value=sup[3])
            area = st.text_input("Area", value=sup[4])
            city = st.text_input("City", value=sup[5])
            state = st.text_input("State", value=sup[6])
            country = st.text_input("Country", value=sup[7])
            ph_no = st.text_input("Phone", value=sup[8])
            email = st.text_input("Email", value=sup[9])
            pan_no = st.text_input("PAN", value=sup[10])
            if (st.button("Delete Supplier")):
                sql = "delete from supplier where supplier_id=%d"%(sup[0])
                cursor.execute(sql)
                db.commit()
                st.success("Supplier deleted successfully.")
