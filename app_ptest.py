from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/start', methods=['GET', 'POST'])
def get_user_name():
    if request.method == 'GET':
        return render_template('user_name_form.html')
    else:
        return 'OOPS'


if __name__ == '__main__':
    app.run(debug=True)