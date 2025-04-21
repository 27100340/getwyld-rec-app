from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/connect', methods=['POST'])
def connect():
    username = request.form.get('username')
    password = request.form.get('password')
    # Dummy authentication
    return render_template('instagram_connect.html')

@app.route('/instagram_login')
def instagram_login():
    return render_template('instagram_page.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
