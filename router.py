from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
#DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://neondb_owner:npg_z9PjKMr5dUWa@ep-restless-dust-aekvtftd.c-2.us-east-2.aws.neon.tech/site?sslmode=require&channel_binding=require"
db = SQLAlchemy(app)

#test DB connection
@app.route('/connectiondb')
def home():
    result = db.session.execute(text("SELECT current_database();"))
    db_name = result.scalar()

    return f"connected to : {db_name}"

# Collecting data from User input
@app.route('/submit', methods=["POST"])
def submit():

    #collecting data into array
    user_data = {
        "name" : request.form.get("name"),
        "age" : request.form.get("age")
    }

    return jsonify(user_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
