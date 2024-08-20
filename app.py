import streamlit as st
import pandas as pd
import duckdb




data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("Hello World")

tab1, tab2, tab3, tab4 = st.tabs(["Cat", "Dog", "Owl", "text"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
    sql_query= st.text_area(label="Entrez votre query ici svp")
    resultat=duckdb.query(sql_query)
    st.write(f"Vous avez entré la requête sql suivante : {sql_query}")


    st.dataframe(resultat.df())
    st.write(resultat)









#resultat= duckdb.sql("""
#SELECT * from df
#""").df()

#st.write(duckdb.sql("""SELECT * from df""").df())
#st.write("resultat est : ", resultat)








