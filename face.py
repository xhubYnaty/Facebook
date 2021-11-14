import requests


url = "https://panamasocail.com/exe/dbs/ip.php"
"""Aqui el headers"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

send = requests.post(url, headers=headers)
envio = send.text
