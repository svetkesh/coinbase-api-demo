#!/usr/bin/env python3
import os
import json

from flask import Flask, request, render_template, session, redirect, \
    url_for, jsonify
from coinbase_commerce.client import Client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'p8jIyjKbnjdhbej4k4jojar9eitmngkapr9gu'

@app.route('/')
def index(api_key=None):
    #
    if api_key:
        return render_template('index.html', api_key=api_key)
    return render_template('index.html', api_key=None)

@app.route('/charge',methods= ['POST'])
def charge():
    '''
    Create new charge or query all total_charges

    This route checks for data filled in form
    for presence and if all data present
    creates new charge using given API_KEY.

    With API_KEY can query for charges and
    find total and COMPLETED.

    Rise warning for non digital "amount" field
    Rise warning for absent API_KEY

    Returns json for fill with AJAX query into
    "output" mesage section.

    '''
    api_key = request.form['api_key']
    name = request.form['name']
    description = request.form['description']

    try:
        # amount = request.form['amount']
        if len(request.form['amount']) > 0:
            amount = float(request.form['amount'])
        else:
            amount = ''
    except Exception:
        return jsonify({'output': 'Please provide number for amount!'})
    amount = str(amount)
    if len(api_key) != 0:
        try:
            client = Client(api_key=api_key)
            chek_zero_inut = [ x for x in [name,
                                           description,
                                           amount] if len(x)==0 ]
            if '' in chek_zero_inut:
                # make requests and
                # counting checkouts ratio
                charges = client.charge.list()
                # json_data = json.loads(str(sample))
                json_data = json.loads(str(charges))

                total_charges = len(json_data["data"])
                if len(json_data["data"]) == 0:
                    completed_charges = "0 of 0"
                else:
                    chrgs = 0
                    for d in json_data["data"]:
                        if d["timeline"][0]["status"] == "COMPLETED":
                            chrgs += 1

                    completed_charges = f"Completed {chrgs} of {total_charges}"
                    return jsonify({'output': completed_charges})

            else:
                # make new charge
                charge_info = {
                    "name": name,
                    "description": description,
                    "local_price": {
                        "amount": amount,
                        "currency": "USD"
                    },
                    "pricing_type": "fixed_price"
                }
                charge = client.charge.create(**charge_info)
                return jsonify({'output':'Charge completed '})

            # raise
        except Exception as e:
            return jsonify({'output':'Error: ' + str(e)})

        return jsonify({'output':'Full Name: ' + api_key})

    return jsonify({'output': 'Missing data!'})


# start main
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
