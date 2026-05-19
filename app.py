from flask import Flask, request, render_template, redirect
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    # Send to Pipedrive
    response = utils.send_to_pipedrive(form_data)
    return "Lead submitted!" if response else "Failed to submit lead."

if __name__ == "__main__":
    app.run(debug=True)
