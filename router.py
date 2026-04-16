from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
#DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://neondb_owner:npg_z9PjKMr5dUWa@ep-restless-dust-aekvtftd.c-2.us-east-2.aws.neon.tech/site?sslmode=require&channel_binding=require"
db = SQLAlchemy(app)

#Data container blueprint from Flask to DB
class test01(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    payload = db.Column(db.JSON)

##############################################################
#test DB connection
@app.route('/connectiondb')
def home():
    result = db.session.execute(text("SELECT current_database();"))
    db_name = result.scalar()

    return f"connected to : {db_name}"

##############################################################
# Collecting data from User input
@app.route('/submit', methods=["POST"])
def submit():

    #collecting data into object
    collectedname = request.form.get("name")
    collectedage = request.form.get("age")
    

    #holding the data collected into the container
    package = test01(name=collectedname,age=collectedage)

    #save and send data to DB
    db.session.add(package)
    db.session.commit()

    return "Success"


##############################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
