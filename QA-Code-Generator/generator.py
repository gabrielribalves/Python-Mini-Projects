import pyqrcode

# urlTyped = input("Digite a URL para gerar o QR Code: ")
url = pyqrcode.create("urlTyped")
url.svg('uca-url.svg', scale=6)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))