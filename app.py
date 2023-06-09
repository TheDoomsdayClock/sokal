from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from requests import post

# os.environ['OPENAI_API_KEY'] = openai.api_key = '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'

app = Flask(__name__)

template = open('template.txt', 'r').read()
jargon = open('jargon.txt', 'r').read()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_message():
    prompt = request.json['message']

    prompt = f'{template}\n{jargon}\n问题为:\n{prompt}\n回答:'
    # response = post('http://45.77.167.174:5000/', json={'message':'Hello'}).json()['response']
    # response = openai.ChatCompletion.create(
    #    model='gpt-3.5-turbo', 
    #    messages=[{"role": "user", "content":prompt}])['choices'][0]['message']['content']
    return jsonify({"response": prompt})

if __name__ == '__main__':
    app.run()
