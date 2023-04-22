from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="database_name"
        )
        
        # Query the users table for the given username and password
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        
        if result:
            return 'Login successful!'
        else:
            return 'Login unsuccessful!'
    
    return '''
        <html>
            <head>
                <title>Login Form</title>
            </head>
            <body>
                <h1>Vulnerable Website</h1>
                <form method="post">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <br>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <br>
                    <div id="login-button">
                        <button type="submit">Login</button>
                    </div>
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
