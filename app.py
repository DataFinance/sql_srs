# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb",read_only=False)


#solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross-joins", "Group By", "window_functions"),
        index=None,
        placeholder="Select a them to practice...",
    )

    st.write("You selected :", theme)

    exercise = con.execute(f"SELECT * FROM memory_state_df WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("Enter your code please : ")
query = st.text_area(label="Votre code SQL ici svp", key="user_input")


if query:
    con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
    result = con.execute(query).df()
    st.dataframe(result)

#    try:
#        result = result[solution_df.columns]
        # result=result[["beverage","price","food_item","food_price"]]
#        st.dataframe(result.compare(solution_df))

#    except KeyError as e:
#        st.write("Some columns are missing")

#    n_lines_difference = result.shape[0] - solution_df.shape[0]

#    if n_lines_difference != 0:
#        st.write(
#            f"result had a {n_lines_difference} lines difference with the solution"
#        )



tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0,"tables"])
    for table in exercise_tables:
        st.write(f"table:, {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)


with tab3:
    exercice_name = exercise.loc[0,"exercice_name"]
    with open(f"answers/{exercice_name}_solution.sql","r") as f:
        answer = f.read()
    st.write(answer)
