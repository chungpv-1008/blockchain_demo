from flask import Flask, render_template
from argparse import ArgumentParser
from time import time

class Blockchain:
  def __init__(self):
    self.transactions = []
    self.chain = []
    self.create_block(0, '00')

  def create_block(self, nonce, previous_hash):
    """
      Thêm 1 block của giao dịch
    """
    block = {
      'block_number': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.transactions,
      'nonce': nonce,
      'previous_hash': previous_hash
    }
    # đặt lại danh sách các giao dịch
    self.transactions = []
    self.chain.append(block)

# Instantiate the Blockchain
blockchain = Blockchain()

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('./index.html')


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('-p', '--port', default=5001, type=int, help="port to listen to")
  args = parser.parse_args()
  port = args.port

  app.run(host='127.0.0.1', port = port, debug=True)
