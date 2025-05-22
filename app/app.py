from flask import Flask
import os
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    # Example database connection
    db_url = os.getenv('DATABASE_URL')
    return 'Hello from Flask! DB URL: ' + db_url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)