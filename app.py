# pylint: disable=missing-module-docstring
import os
import logging
import subprocess

import duckdb
import streamlit as st

if "data" not in os.listdir():
    print("creating the folder data")
    logging.error(os.listdir())
    logging.error("creating the folder data")
    # logging.debug(os.listdir())
    # logging.debug("creating the folder data")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python","init_db.py"])


con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross-joins", "Group By", "window_functions"),
        index=None,
        placeholder="Select a them to practice...",
    )

    st.write("You selected :", theme)

    exercise = (
        con.execute(f"SELECT * FROM memory_state_df WHERE theme = '{theme}'")
        .df()
        .sort_values("last_revision")
        .reset_index()
    )
    st.write(exercise)

    exercice_name = exercise.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}_solution.sql", "r") as f:
        answer = f.read()

    solution_df = con.sql(answer).df()


st.header("Enter your code please : ")
query = st.text_area(label="Votre code SQL ici svp", key="user_input")


if query:
    con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        # result=result[["beverage","price","food_item","food_price"]]
        st.dataframe(result.compare(solution_df))

    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]

    if n_lines_difference != 0:
        st.write(
            f"result had a {n_lines_difference} lines difference with the solution"
        )


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:

    exercise_tables = exercise.loc[0, "tables"]

    for table in exercise_tables:
        st.write(f"table:, {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab3:
    st.write(answer)
