from flask import Flask,request
import os

app = Flask(__name__)

@app.route('/test.py',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        data=request.data
        with open('test.log', 'w') as f:
            f.write(str(data)
            return str(data)

    if request.method == 'GET':
        with open('protest.log') as f:
            s=f.read()
            return str(s)


if __name__ == '__main__':
    app.run()
