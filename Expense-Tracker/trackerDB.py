import sqlite3

def insertInTracker(rowObj):
    con = sqlite3.connect("tracker.db")
    instruction = f"""\
    INSERT INTO tracker(date, category, value, balance)
    VALUES ('{rowObj["date"]}','{rowObj["category"]}',{rowObj["value"]}, {rowObj["balance"]});
    """
    con.execute(instruction)
    con.commit()

    reorderIDs("tracker")

def insertCategory(category):
    con = sqlite3.connect("tracker.db")
    instruction = f"""\
    INSERT INTO category(category)
    VALUES('{category}')
    """
    con.execute(instruction)
    con.commit()

    reorderIDs('category')

def reorderIDs(table):
    con = sqlite3.connect("tracker.db")
    instruction = f"""\
    WITH cte AS (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
        FROM {table}
    )
    UPDATE {table} AS t
    SET id = c.new_id
    FROM cte AS c
    WHERE t.id = c.id;
    """
    con.execute(instruction)

    con.commit()

def deleteRow(table, id):
    con = sqlite3.connect('tracker.db')
    instruction = f"""\
    DELETE FROM {table}
    WHERE id={id}
    """
    con.execute(instruction)
    con.commit()

    reorderIDs(table)


def updateBalance(value:int) -> None:
    con = sqlite3.connect('tracker.db')
    instruction = f"""\
    UPDATE balance
    SET value={value}
    """
    con.execute(instruction)
    con.commit()

def selectAll(table) -> list:
    con = sqlite3.connect("tracker.db")
    instruction = f"SELECT * FROM {table};"

    cur = con.cursor()
    result = cur.execute(instruction)
    listReturn = []
    for row in result:
         listReturn.append(row)
    return listReturn
