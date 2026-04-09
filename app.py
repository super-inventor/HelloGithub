from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/message')
def get_message():
    return jsonify({
        'message': '恭喜你，你已成功运行了一个开源项目！',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
