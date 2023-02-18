from flask import Flask, request, Response
import requests
import os
import json

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit_invoice():
  url = "https://sandbox.checkbook.io/v3/invoice"
  data = request.get_json()
  payload = {
    "amount": data["amount"],
    "description": data["description"],
    "name": data["name"],
    "recipient": data["email"]
  }
  headers = {
    "accept":
    "application/json",
    "content-type":
    "application/json",
    "Authorization":
    "9eb04080daf74da76074eff1be227371:" + os.environ['API_SECRET']
  }

  print(payload)
  try:
    response = json.loads(requests.post(url, json=payload, headers=headers))
    if "error" in response:
      return Response("Invoice can't be issued.", status=404)
    else:
      print(response.text)
      return Response("Invoice issued successfully.", status=200)
  except:
    return Response("Invoice not posted.", status=404)


app.run(host='0.0.0.0', port=2333)
