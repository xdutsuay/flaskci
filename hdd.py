import requests

parameters = [{
    "Account no": "",
    "Date": "",
    "Transaction Details": "",
    "Value Date": "",
    "withdrawal AMT": "",
    "Deposit AMT": "",
    "Balance AMT": ""

}]


def convert_date_format(date="26-02-96"):
    formula = {"01": "Jan", "02": "Feb", "03": "Mar",
               "04": "Apr", "05": "May", "06": "Jun",
               "07": "Jul", "08": "Aug", "09": "Sep",
               "10": "Oct", "11": "Nov", "12": "Dec"
               }
    temp_date = date.split("-")
    return temp_date[0]+" "+formula[temp_date[1]]+" "+temp_date[2]


response = requests.get("https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json")
response.raise_for_status()
data = response.json()
with open ("trasdata.txt", 'w') as file:
    file.write(str(data))
#print(data)
