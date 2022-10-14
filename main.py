from lib2to3.pgen2.pgen import generate_grammar
from flask import Flask, request, make_response, render_template, redirect, session, url_for, flash, Response
from app import create_app
from app.forms import CommonForm
from app.yaml import WriteYaml

app = create_app()
yaml = WriteYaml()

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
    home_form = CommonForm()
    context = {
        'module': 'home',
        'form_name': 'Basic parameters',
        'form_to_render': home_form,
    }

    if home_form.validate_on_submit():
        file_name = 'config/common/common.yaml'
        data = request.form.to_dict()
        del data['csrf_token']
        del data['submit']
        success, msg = yaml.dict_to_yaml(file_name,data)
        context['success'] = success
        context['success_text'] = msg


    return render_template('home.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
