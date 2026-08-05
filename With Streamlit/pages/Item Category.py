import pandas as pd
import pymysql
import streamlit as st

opRadio = st.sidebar.radio("Select Operation", ['Add Category', 'Update Category', 'Display Categories', 'Delete Category'])

db = pymysql.connect(host="localhost", user="root", password="root", database="medicalstoredb")
cursor = db.cursor()

st.set_page_config(page_title="Item Category")

st.title("Item Category Form")
if (opRadio == "Add Category"):
    with st.form("add_category_form"):
        st.subheader("Enter Item Category Details", divider="blue")

        c_type = st.text_input("Enter Category name : ")
        desc = st.text_area("Enter category description : ")
        if (st.form_submit_button("Add Category")):
            sql = "insert into category (c_type, description) values ('%s', '%s')"%(c_type, desc)
            cursor.execute(sql)
            db.commit()
            st.success("Category Added Successfully.")
elif (opRadio == "Update Category"):
    st.subheader("Enter Item category Details to Update", divider="blue")
    opSb = st.selectbox("Update by", ['Category ID', 'Category Name'])
    if (opSb == "Category ID"):
        sql = "select category_id from category"
        cursor.execute(sql)
        categories = cursor.fetchall()
        cids = []
        for i in categories:
            cids.append(i[0])
        selectCat = st.selectbox("Select Category ID to update", cids)
        sql = "select * from category where category_id = %d"%(selectCat)
        cursor.execute(sql)
        cat = cursor.fetchone()
        if (cat):
            st.text_input("Category ID", value=cat[0], disabled=True)
            c_type = st.text_input("Enter Category name : ", value=cat[1])
            desc = st.text_area("Enter category description : ", value=cat[2])
            if (st.button("Update Category")):
                sql = "update category set c_type = '%s', description='%s' where category_id=%d"%(c_type, desc, cat[0])
                cursor.execute(sql)
                db.commit()
                st.success("Category details updated successfully.")
    elif (opSb == "Category Name"):
        sql = "select c_type from category"
        cursor.execute(sql)
        categories = cursor.fetchall()
        ctypes = []
        for i in categories:
            ctypes.append(i[0])
        selectCat = st.selectbox("Select Category ID to update", ctypes)
        sql = "select * from category where c_type = '%s'"%(selectCat)
        cursor.execute(sql)
        cat = cursor.fetchone()
        if (cat):
            st.text_input("Category ID", value=cat[0], disabled=True)
            c_type = st.text_input("Enter Category name : ", value=cat[1])
            desc = st.text_area("Enter category description : ", value=cat[2])
            if (st.button("Update Category")):
                sql = "update category set c_type = '%s', description='%s' where category_id=%d"%(c_type, desc, cat[0])
                cursor.execute(sql)
                db.commit()
                st.success("Category details updated successfully.")

elif (opRadio == "Display Categories"):
    sql = "select * from category"
    cursor.execute(sql)
    categories = cursor.fetchall()
    df = pd.DataFrame(categories, columns=['Category ID', 'Category Name', 'Description'])
    st.header("List of item categories")
    st.dataframe(df)

elif (opRadio == "Delete Category"):
    st.subheader("Select Item category Details to Delete", divider="blue")
    opSb = st.selectbox("Delete by", ['Category ID', 'Category Name'])
    if (opSb == "Category ID"):
        sql = "select category_id from category"
        #c_id = st.number_input("Enter Category id to delete", value=0)
        #sql = "select * from category where category_id = %d"%(c_id)
        cursor.execute(sql)
        categories = cursor.fetchall()
        cids = []
        for i in categories:
            cids.append(i[0])
        selectCat = st.selectbox("Select Category ID to delete", cids)
        sql = "select * from category where category_id = %d"%(selectCat)
        cursor.execute(sql)
        cat = cursor.fetchone()
        if (cat):
            st.text_input("Category ID", value=cat[0], disabled=True)
            c_type = st.text_input("Enter Category name : ", value=cat[1])
            desc = st.text_area("Enter category description : ", value=cat[2])

            if (st.button("Delete Category")):
                sql = "delete from category where category_id=%d"%(cat[0])
                cursor.execute(sql)
                db.commit()
                st.success("Item Category deleted successfully.")
    elif (opSb == "Category Name"):
        sql = "select c_type from category"
        cursor.execute(sql)
        categories = cursor.fetchall()
        cids = []
        for i in categories:
            cids.append(i[0])
        selectCat = st.selectbox("Select Category ID to update", cids)
        sql = "select * from category where c_type = '%s'"%(selectCat)
        cursor.execute(sql)
        cat = cursor.fetchone()
        if (cat):
            st.text_input("Category ID", value=cat[0], disabled=True)
            c_type = st.text_input("Enter Category name : ", value=cat[1])
            desc = st.text_area("Enter category description : ", value=cat[2])

            if (st.button("Delete Category")):
                sql = "delete from category where category_id=%d"%(cat[0])
                cursor.execute(sql)
                db.commit()
                st.success("Item Category deleted successfully.")
