"""
Matthew Sabo
2017
blockchain.py
Represents a blockchain
"""

from flask import Flask
from flask import request

import datetime
import json
import hashlib

from block import Block

class Blockchain:
	def __init__(self):
		self.num_blocks = 0
		self.current = "0"
		self.blocks = []
		self.add_block("Genesis")
		self.current = self.blocks[0]

	def add_block(self, data):
		time = datetime.datetime.now()
		new_block = Block(self.num_blocks, time, data, self.current)
		self.blocks.append(new_block)
		print("Block #{0} added to chain.".format(self.num_blocks))
		self.num_blocks += 1
		self.current = new_block

chain = Blockchain()

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

miner_addr = hashlib.sha256().update(str(input("Name: ")).encode('utf-8'))

def proof_of_work(last_proof):
	incrementor = last_proof + 1
	while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
		incrementor += 1

	return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
	last_proof = chain.current.data['proof_of_work']
	proof = proof_of_work(last_proof)
	txions.append(
		{"from":"network", "to":miner_addr, "amount":1}
	)
	new_data = {
		"proof_of_work":proof,
		"transactions":list(get_txions().data)
	}
	del txions[:]
	get_chain().add_block(new_data)
	return 1

@node.route('/blocks', method = ['GET'])
def get_blocks():
	chain_to_send = get_chain()
	for block in chain_to_send.blocks:
		block = {
			"index":block.index,
			"timestamp":block.timestamp,
			"data":block.data,
			"hash":block.hash
		}
	
	chain_to_send = json.dumps(chain_to_send)
	return chain_to_send

def find_new_chains():
	other_chains = []
	for node_url in peer_nodes:
		block = requests.get(node_url+"/blocks").content
		block = json.loads(block)
		other_chains.append(block)
	return other_chains

def consensus():
	other_chains = find_new_chains()
	longest_chain = chain
	for chain in other_chains:
		if (chain.num_blocks > longest_chain.num_blocks):
			longest_chain = chain
	chain = longest_chain

node.run()