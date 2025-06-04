"""
Flask application connected to MySQL database
"""
from flask import Flask, render_template
import mysql.connector
from config import MYSQL_CONFIG

app = Flask(__name__)

def get_db_connection():
    """Create and return a connection to MySQL database"""
    try:
        connection = mysql.connector.connect(
            host=MYSQL_CONFIG['host'],
            user=MYSQL_CONFIG['user'],
            password=MYSQL_CONFIG['password'],
            port=MYSQL_CONFIG['port']
        )
        return connection, None
    except mysql.connector.Error as err:
        return None, f"Database connection error: {err}"

@app.route('/')
def home():
    """Home page route that displays MySQL connection status and databases"""
    connection, error = get_db_connection()
    
    if error:
        return render_template('home.html', 
                              connected=False, 
                              error=error,
                              databases=[])
    
    # Get list of databases
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return render_template('home.html', 
                          connected=True, 
                          error=None,
                          databases=databases)

if __name__ == '__main__':
    app.run(debug=True)