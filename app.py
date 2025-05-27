from flask import Flask, request,render_template
import requests


app = Flask(__name__)
API_KEY="435VFNYZBYX4590C"
@app.route("/", methods=['GET','POST'])
def stockMarketHome():
    stock_data = None
    error = None
    if request.method=='POST':
        symbol=request.form['stock'].upper().strip()
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
        response =requests.get(url)
        data = response.json()
        try:
            current_stock =data["Global Quote"]
            stock_data ={
                "symbol":current_stock["01. symbol"],
                 "price":current_stock["05. price"],
                  "change":current_stock["09. change"],
            
            }
        except KeyError:
            error = f"No data found for '{symbol}'."
        


    return render_template("index.html",stock_data=stock_data, error = error)

if __name__ =="__main__":
    app.run(debug=True)
