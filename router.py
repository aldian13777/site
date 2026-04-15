from flask import Flask, request, jsonify



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
