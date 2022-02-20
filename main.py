from flask import Flask, request, redirect, url_for
from hdd import *
import hdd

app = Flask(__name__)


# @app.route('/hello')
# def hello_world():
#     return 'hello world'

@app.route('/transaction/<date>')
def td(date):
    date = hdd.convert_date_format(date)
    transactions = {"Transactions": []
                    }
    for small_data in data:
        if small_data["Date"] == date:
            transactions["Transactions"].append(small_data["Transaction Details"])

    return transactions

    pass


@app.route('/balance/<date>')
def bd(date):
    date = hdd.convert_date_format(date)
    # print(date)
    for small_data in data:
        # print(data)
        # print(small_data["Date"])
        if small_data["Date"] == date:
            return small_data["Balance AMT"]
        elif small_data["Date"] != data[-1]["Date"]:
            # print(small_data["Date"],data[-1]["Date"],date)
            continue
        else:
            return "No Record for specified date"
    # print(type(small_data))
    pass


@app.route('/details/<id>')
def deid(id):  # id not given in data assuming index of data as id

    return data[int(id)]
    pass


@app.route('/addmoredata')
def addmoredata():
    return 'welcome '


@app.route('/add')  # post req to add more data in appropriate formate
def add():
    # basically hitting this url should redirect to addmoredata.html and that should take values and provide to backend
    # redirect(url_for('addmoredata'))
    # if request.method == 'POST':
    #     account = request.form["ACCNO"]
    #     date = request.form["DATE"]
    #     td = request.form["TD"]
    #     val = request.form["VAL"]
    #     wit = request.form["WITH"]
    #     dp = request.form["DP"]
    #     bal = request.form["BAL"]
    #     return redirect(url_for('success', accno=account))

    pass


# deploy of aws lambda


if __name__ == '__main__':
    app.run()
