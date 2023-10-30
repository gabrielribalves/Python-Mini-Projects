import sqlite3

def convertDateToDB(date):
    if date == "--":
        return "0"

    date = date.replace("-", "")
    return date

def convertDateToFront(date):
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    return f"{year}-{month}-{day}"

def insertInDB(rowObj):
    rowObj['date'] = convertDateToDB(rowObj['date'])
    con = sqlite3.connect("todoList.db")
    instruction = f"""\
    INSERT OR REPLACE INTO todorow(idrow, taskdate, task)
    VALUES ({rowObj['idrow']}, {rowObj['date']}, '{rowObj['task']}');
    """
    con.execute(instruction)
    
    con.commit()

def reorderIDRow():
    con = sqlite3.connect("todoList.db")
    instruction = """\
    WITH cte AS (
        SELECT idrow, ROW_NUMBER() OVER (ORDER BY idrow) AS new_idrow
        FROM todorow
    )
    UPDATE todorow AS t
    SET idrow = c.new_idrow
    FROM cte AS c
    WHERE t.idrow = c.idrow;
    """
    con.execute(instruction)

    con.commit()

def deleteInDB(idRow):
    con = sqlite3.connect("todoList.db")

    instruction = f"""\
    DELETE FROM todorow
    WHERE (idrow={idRow});
    """
    con.execute(instruction)
   
    con.commit()

    reorderIDRow()

def saveEdit(idRow, date, task):
    con = sqlite3.connect('todoList.db')
    convertedDate = convertDateToDB(date)
    instruction = f"""\
    UPDATE todorow 
    SET taskdate="{convertedDate}", task='{task}'
    WHERE idrow={idRow};
    """
    # SET taskdate={convertedDate}, task='{task}'
    con.execute(instruction)
    con.commit()
    
def getInitialValues():
    initialList = []
    idrow = 0

    con = sqlite3.connect("todoList.db")
    instruction = f"SELECT taskdate, task FROM todorow"
    cur = con.cursor()
    result = cur.execute(instruction)
    for row in result:
        idrow += 1
        if row[0] == "0":
            dateConverted = "--"
        else:
            dateConverted = convertDateToFront(row[0])
        initialList.append([idrow, dateConverted, row[1]])
    
    return initialList