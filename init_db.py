# pylint: disable=missing-module-docstring

import io
import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# -----------------------------------------------------------
# EXERCICES LIST
# -----------------------------------------------------------

data = {
    "theme": ["cross-joins", "cross-joins"],
    "exercice_name": ["beverage_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_revision": ["1980-01-01", "1970-01-01"],
}

memory_state_df = pd.DataFrame(data)
con.execute(
    "CREATE TABLE IF NOT EXISTS memory_state_df AS SELECT * FROM memory_state_df"
)


CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS FOOD_ITEMS AS SELECT * FROM food_items")

CSV = """
beverage,price
orange juice,2.5
espresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS BEVERAGES AS SELECT * FROM beverages")

SIZES = """
size,
XS,
M,
L,
XL
"""

size = pd.read_csv(io.StringIO(SIZES))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

TRADEMARKS = """
trademark,
Nike,
Asphalte,
Abercrombie
Lewis
"""

trademarks = pd.read_csv(io.StringIO(TRADEMARKS))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

con.close()
