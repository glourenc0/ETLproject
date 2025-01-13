import requests

url = "https://jsonplaceholder.typicode.com/comments"
headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacap/1.0"
}
params = {"currency": "USD"} #Moeda de Consulta

reponse = requests.get(url, headers=headers, params=params)
data = reponse.json()
print(f"Preço do Bitcoin (USD):", data["data"]["amount"])