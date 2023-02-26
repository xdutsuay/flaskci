from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)

def convert_date_format(date="26-02-96"):
    temp_date = date.split("-")
    return f"{temp_date[0]} {temp_date[1]} {temp_date[2]}"

response = requests.get("https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json")
response.raise_for_status()
data = response.json()

@app.route('/transaction/<date>')
def td(date):
    date = convert_date_format(date)
    transactions = {"Transactions": []}
    for small_data in data:
        if small_data["Date"] == date:
            transactions["Transactions"].append(small_data["Transaction Details"])

    return transactions

@app.route('/balance/<date>')
def bd(date):
    date = convert_date_format(date)
    for small_data in data:
        if small_data["Date"] == date:
            return small_data["Balance AMT"]
        elif small_data["Date"] != data[-1]["Date"]:
            continue
        else:
            return "No Record for specified date"

@app.route('/details/<id>')
def deid(id): 
    return data[int(id)]

@app.route('/add', methods=['GET', 'POST']) 
def add():
    if request.method == 'POST':
        new_data = {
            "Account No": request.form["ACCNO"],
            "Date": request.form["DATE"],
            "Transaction Details": request.form["TD"],
            "Value Date": request.form["VAL"],
            "Withdrawal AMT": request.form["WIT"],
            "Deposit AMT": request.form["DP"],
            "Balance AMT": request.form["BAL"]
        }
        data.append(new_data)
        return redirect(url_for('addmoredata'))
    else:
        return '''
            <html>
               <body>
                  <form action = "http://localhost:5000/add" method = "post">
                     <p>Enter Account no:</p>
                     <p><input type = "text" name = "ACCNO" /></p>
                      <p>Enter Date like "29 Jun 17"</p>
                      <p><input type = "text" name = "DATE" /></p>
                      <p>Enter Transaction Details</p>
                      <p><input type = "text" name = "TD" /></p>
                      <p>Enter Value Date</p>
                      <p><input type = "text" name = "VAL" /></p>
                      <p>Enter Withdrawl AMT</p>
                      <p><input type = "text" name = "WIT" /></p>
                      <p>Enter Deposit AMT</p>
                      <p><input type = "text" name = "DP" /></p>
                      <p>Enter Balance AMT</p>
                      <p><input type = "text" name = "BAL" /></p>
                     <p><input type = "submit" value = "submit" /></p>
                  </form>
               </body>
            </html>
        '''

@app.route('/addmoredata')
def addmoredata():
    return 'welcome '

if __name__ == '__main__':
    app.run()
