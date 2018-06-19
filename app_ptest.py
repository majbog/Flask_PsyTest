from flask import Flask, request, render_template, session
import os


app = Flask(__name__)
app.secret_key = os.urandom(50)


@app.route('/start', methods=['GET', 'POST'])
def get_user_name():
    if request.method == 'GET':
        return render_template('user_name_form.html')
    else:
        session['user'] = request.form['user_name']
        return render_template(
            'welcome_user.html',
            user=session['user']
        )

    
@app.route('/test', methods=['GET', 'POST'])
def do_the_test():
    pass


if __name__ == '__main__':
    app.run(debug=True)