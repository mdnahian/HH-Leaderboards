from flask import Flask, render_template
from flask_socketio import SocketIO
import MySQLdb
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hhleaderboards'
socketio = SocketIO(app)

db = MySQLdb.connect("localhost" , "root", "$Mdni00007", "hhleaderboards")
cursor = db.cursor()

@app.route('/')
def index():
	sql = "SELECT * FROM Posts INNER JOIN Users ON Posts.user_id=Users.user_id LIMIT 100"
	results = cursor.execute(sql)

	return render_template('index.html')
	

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(80))
