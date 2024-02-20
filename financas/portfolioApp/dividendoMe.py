import requests
import json

headers = {
    'authority': 'api.dividendos.me',
    'accept': 'application/json',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6WyI2OWU3ZjU3ZS1hNTY3LTQ1ZDQtODI4Zi0zMjk4YWZmMjBhMTciLCI2OWU3ZjU3ZS1hNTY3LTQ1ZDQtODI4Zi0zMjk4YWZmMjBhMTciXSwianRpIjoiNDAzNGFiZjIxY2Q3NDBlOWIzMzU4Njc3OGQyM2ZlOTAiLCJyb2xlIjoiVXNlciIsIkVtYWlsIjoiZ3VpbGhlcm1lLnMudWNob2FAZ21haWwuY29tIiwibmJmIjoxNzA2ODc5MjEwLCJleHAiOjE4NjQ1NTkyMTAsImlhdCI6MTcwNjg3OTIxMCwiaXNzIjoiRGl2aWRlbmRvcyIsImF1ZCI6IkRpdmlkZW5kb3MifQ.8yNp4jN4rIigv0G2FpXWGcWqVD27j_BJnrgB3otsLx8',
    'cache-control': 'no-cache',
    'origin': 'https://app.dividendos.me',
    'pragma': 'no-cache',
    'referer': 'https://app.dividendos.me/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = {
    'portfolioOrSubPortfolio': '7ac27c1c-9fcc-45f2-9eee-51bdbd205a2a',
}

response = requests.get('https://api.dividendos.me/v5/Operation/operationsummary', params=params, headers=headers)

ativos = response.json()['value']['operationsSummary']

for i in ativos[0]:
    print(i, ativos[0][i])