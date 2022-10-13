from flask import Flask, request, make_response, render_template, redirect, session, url_for, flash, Response
from app import create_app
from app.forms import CommonForm

app = create_app()

@app.route('/')
def index():
    """Index method to redirect to home page

    Returns:
        server response: redirect to /home route 
    """
    user_ip = request.remote_addr
    response = make_response(redirect('/home'))
    session['user_ip'] = user_ip
    return response


@app.route('/home', methods=['GET', 'POST'])
def home():
    """Home method - welcome page

    Returns:
        server response: Home-page for platform welcome
    """
    context = {
        'anonymous': True,
        'form_to_render':CommonForm(),
        'user_ip': "UserIp",
    }
    return render_template('home.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
