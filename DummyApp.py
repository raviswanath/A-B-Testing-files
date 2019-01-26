from __future__ import print_function, division
from builtins import range

import numpy as np
from flask import Flask, jsonify, request
from scipy.stats import beta

# create an app
app = Flask(__name__)

class Bandit:
    
    def __init__(self, name):
        self.name = name
        self.views = 0
        self.click = 0
    
    def sample(self):
        a = 1 + self.clicks
        b = 1 + self.views - self.clicks
        return np.random.beta(a,b)
    
    def add_clicks(self):
        self.clicks += 1
        
    def add_views(self):
        self.views += 1
        
# initialize bandits
banditA = Bandit('A')
banditB = Bandit('B')

@app.route('/get_ad')
def get_ad():
    if banditA.sample() > banditB.sample:
        ad = "A"
        banditA.add_view()
    else:
        ad = "B"
        banditB.add_view()
    return jsonify({'advertisement_id': ad})

@app.route('/click_ad', methods=['POST'])
def click_ad():
    result = 'OK'
    if request.form['advertisement_id'] == 'A':
        banditA.add_clicks()    
    elif request.form['advertisement_id'] == 'B':
        banditB.add_clicks()
    else:
        result = 'Invalid Input.'
    
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888')