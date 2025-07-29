from flask import Flask, render_template, request, redirect, jsonify
from blockchain import Blockchain
from wallet import Wallet

app = Flask(_name_)

blockchain = Blockchain()
wallet = Wallet()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wallet')
def wallet_page():
    address = wallet.generate_address()
    return render_template('wallet.html', address=address)

@app.route('/send', methods=['GET', 'POST'])
def send_transaction():
    if request.method == 'POST':
        sender = request.form['sender']
        receiver = request.form['receiver']
        amount = int(request.form['amount'])
        blockchain.add_transaction(sender, receiver, amount)
        blockchain.mine_block()
        return redirect('/explorer')
    return render_template('send_txn.html')

@app.route('/explorer')
def explorer():
    chain = blockchain.chain
    return render_template('explorer.html', chain=chain)

if _name_ == '_main_':
    app.run(debug=True)