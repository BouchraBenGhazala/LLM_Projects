import streamlit as st
import langchain_helper

st.title(":red[Restaurant Name Generator]")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Moroccan","Algerian","Tunisian","Egyptian","French","Italian","Spanish"))

if cuisine:
    response=langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip().strip('"'))
    menu_items=response['menu_items'].strip().split(",")
    st.write("**Menu items**")
    for item in menu_items:
        st.write(item.strip())



