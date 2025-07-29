import time
import hashlib
import json

class Blockchain:
    def _init_(self):
        self.chain = []
        self.transactions = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block)
        self.transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.last_block['index'] + 1

    def mine_block(self):
        last_block = self.last_block
        previous_hash = last_block['hash']
        return self.create_block(previous_hash)

    @property
    def last_block(self):
        return self.chain[-1]

    def hash(self, block):
        block_copy = block.copy()
        block_copy.pop('hash', None)
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()