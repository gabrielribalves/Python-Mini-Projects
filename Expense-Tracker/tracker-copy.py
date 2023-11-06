import csv
import gspread

MONTH = 'october'
file = f"inter_{MONTH}.csv"
CATEGORY_NAMES = {
    "COMPRA CARTAO": "Compra Débito",
    "PIX ENVIADO - Cp :60701190-Paroquia Sao Jose": "Dízimo",
    "PAGAM. ELETROPAULO - Pagamento": "Conta",
    "CREDITO EVENTOS RENDA FIXA - LCI DI FLUT TB": "Investimento",
}

def handleData(row, row1, row2):
    row = row.split(";")
    row1 = row1.split(";")
    value = f"{row[2]},{row1[0]}"
    balance = f"{row1[1]},{row2}"
    returnList = [row[0].rstrip(" "), row[1].rstrip(" "),value.rstrip(" "), balance]

    returnList[2] = returnList[2].replace(".", "").replace(",",".")
    returnList[3] = returnList[3].replace(".", "").replace(",",".")
    return returnList

def interFin(file, CATEGORY_NAMES):
    transactionsList = []
    count = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            count += 1
            if count >= 7:
                
                dataList = handleData(row[0], row[1], row[2])
                date = dataList[0]
                category = dataList[1]
                transactionValue = float(dataList[2])
                balance = float(dataList[3])

                if category in CATEGORY_NAMES:
                    category = CATEGORY_NAMES[category]

                transactionsList.append((date, category, transactionValue, balance))

        return transactionsList


sa = gspread.service_account()
sh = sa.open("My Finances")

wks = sh.worksheet(f"{MONTH}")


rows = interFin(file, CATEGORY_NAMES)
count = 7
for row in rows:
    wks.insert_row([row[0],row[1],row[2],row[3]], count)
    count += 1

