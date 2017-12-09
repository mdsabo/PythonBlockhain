"""
Matthew Sabo
2017
proof.py
Proof of work/mining algorithm
"""

import hashlib
import json

from block import Block
from blockchain import Blockchain

import txion_submit
import main

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