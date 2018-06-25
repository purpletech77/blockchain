# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import hashlib
import json
from flash import Flask, jsonify

#1 building a blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1,previous_hash = '0' )
        
    def create_block(self, proof, previous_hash):
        '''
        Called after mining of the block
        '''
        
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash }
        
        chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        ''' should be hard to find, but easy to verify '''
        new_proof = 1
        check_proof = False
        while check_proof is False:
            #make the problem difficult
            hash_operation = hashlib.sha256( str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else :
                new_proof += 1
                
        return new_proof
                
            
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block =  chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            
            hashlib.sha256( str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
            
        return True
    
    
            
            
            
            
        
        
        

#2 mining our blockchain