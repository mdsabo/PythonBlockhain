"""
Matthew Sabo
2017
block.py
Represents a block in the blockchain
"""

import json

import txion_submit
import main

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
	longest_chain = get_chain()
	for chain in other_chains:
		if (chain.num_blocks > longest_chain.num_blocks):
			longest_chain = chain

	return longest_chain

