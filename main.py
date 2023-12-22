from flask import Flask, render_template, request, flash


app = Flask(__name__)

@app.route("/")
def p_auto_main():
    return render_template('autogura_main.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""