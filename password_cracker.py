from zipfile import ZipFile
with ZipFile('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/whitehouse_secrets.zip') as zf:
    password_str = 'BFDL'
    password = password_str.encode('ascii')
    zf.extractall(pwd=password)
with open('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/whitehouse_secrets.zip', 'br') as f:
    text = f.read()
    text = text.decode('utf-8')
print("text=",text)