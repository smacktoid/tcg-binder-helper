from flask import Flask, render_template, jsonify, request
from tcgbinderhelper.positioner import find_position

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])
def home():

    position = None
    if request.method == 'POST':
        card_no = int(request.form.get('cardNo'))
        position = find_position(card_no)
    return render_template("home.html", position=position)

if __name__ == "__main__":
    app.run(debug=True)