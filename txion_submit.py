"""
Matthew Sabo
2017
txion_submit.py
Transaction submit via Flask framework
"""

from flask import Flask
from flask import request

import proof
import consensus

node = Flask(__name__)

txions = []

@node.route('/txion', methods=['POST'])
def transaction():
	if (request.method == "POST"):
		new_txion = request.get_json()
		txions.append(new_txion)
		print("New Transaction")
		print("From: {0}".format(new_txion['from']))
		print("To: {0}".format(new_txion['to']))
		print("Amount: {0}".format(new_txion['amount']))
		return 1

def get_node():
	return node

def get_txions():
	return txions