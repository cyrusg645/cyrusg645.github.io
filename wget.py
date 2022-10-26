'''
A wget program is a program that "get"s information from the "w"eb
'''

#get the url to download from the command line
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--filename') #, default
args = parser.parse_args()
url = args.url

print('url=', url)

#download the url
import requests
response = requests.get(url)
text = response.text

#save the file
# 'w' = write
# 'r' = read
# 't' = text => automatically apply the encoding
# 'b' = binary / bytes => don't appy to coding
# x = write, but if the file already exists throw an errow 
filename = 'webpage'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)