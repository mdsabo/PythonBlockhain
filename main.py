
from flask import Flask
from flask import request

import txion_submit
from blockchain import Blockchain

chain = Blockchain()

def main():
	get_node().run()

def get_chain():
	return chain

main()