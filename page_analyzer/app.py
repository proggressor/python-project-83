from flask import Flask
from flask import render_template
# from flask import request
# from flask import redirect


app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def main_page():
    url = ''
    return render_template(
        'index.html',
        url=url
    )
