import csv

MONTH = 'october'

file = f"inter_{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# txt = "'09/10/2023;PAGAMENTO DE TITULO - Pagamento;-731', '62;11.819', '41'"

# print(txt[0].split(";"))