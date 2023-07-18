from flask import Flask, render_template
import connectio

port = connectio.Port(8181)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chatapp.html')

@app.route('/'+port.send)
def send_message(message):
  port.addMessage(message)
  return ''
@app.route('/'+port.get)
def get_messages():
  return port.messages()

app.run(host='0.0.0.0', port=81)
