# coinbase-api-demo
coinbase-api-demo

**This project show using Coinbase API**

Based on coinbase-commerce-python,

https://github.com/coinbase/coinbase-commerce-python

Before using this aplication you have to:

1. register with Coinbase 
https://commerce.coinbase.com/signup

2. recieve your API_KEY 
https://commerce.coinbase.com/dashboard/settings
![](https://github.com/svetkesh/coinbase-api-demo/blob/master/screenshots/Screenshot%20at%202019-05-02%2003-00-17.png)

3. whitelist localhost and Flask default development port 5000
https://commerce.coinbase.com/dashboard/settings
![](https://github.com/svetkesh/coinbase-api-demo/blob/master/screenshots/Screenshot%20at%202019-05-02%2002-59-28.png)

4. Python 3.7 installed

Please clone or download project.

Using environment highly recomended, so

Assume cbp is folder with project files

```
cd cd cbp/

python3 -m venv cbp

source cbp/bin/activate

pip install -r requirements.txt
```
run
```
python coinbaseapidemo.py
```

Open browser to https://127.0.0.1:5000/


You could see warning against self-signed SSL sertificate

Click "Advanced"
![](https://github.com/svetkesh/coinbase-api-demo/blob/master/screenshots/Screenshot%20at%202019-05-02%2002-56-20.png)

Click "Accept..."
![](https://github.com/svetkesh/coinbase-api-demo/blob/master/screenshots/Screenshot%20at%202019-05-02%2002-56-47.png)

You can use your API_KEY
to check charges clicking "Submit"
![](https://github.com/svetkesh/coinbase-api-demo/blob/master/screenshots/Screenshot%20at%202019-05-02%2003-14-15.png)

Bottom line shows COMPLETED and total charges

Or to create new coinbase charge fill in all field in rest of the form.

This version for the sake of simplicity does not count Checkouts
due to default limited connection to the Coinbase API.
