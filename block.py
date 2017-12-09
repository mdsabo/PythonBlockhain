"""
Matthew Sabo
2017
block.py
Represents a block in the blockchain
"""

import hashlib
import json

class Block:
	def __init__(self, index, timestamp, data, previous):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous = previous
		self.hash = self.generate_hash()
		print ("Block created with hash: {0}".format(self.hash))
		json.dumps({
			"index":self.index,
			"timestamp":str(self.timestamp),
			"data":self.data,
			"hash":self.hash
		})

	def generate_hash(self):
		sha = hashlib.sha256()
		sha.update(
			(str(self.index)+
			str(self.timestamp)+
			str(self.data)+
			str(self.previous)).encode('utf-8'))
		return sha.hexdigest()