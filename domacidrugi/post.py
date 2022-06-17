import requests
import json

url = "http://localhost:8081/users"

payload = json.dumps({
  "ime": "Bogdan",
  "prezime": "Selecanin",
  "smer": "IT",
  "predmeti": [
    {
      "ime": "Microsoft",
      "espb": 6
    },
    {
      "ime": "RVAS",
      "espb": 6
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)