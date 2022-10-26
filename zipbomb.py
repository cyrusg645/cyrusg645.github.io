from zipfile import ZipFile
with ZipFile('/Users/cyrus/Documents/GitHub/cyrusg645.github.io/whitehouse_secrets.zip') as zf:
    password_str = 'BFDL'
    password = password_str.encode('ascii')
    zf.extractall(pwd=password)