from flask import Flask, request, make_response, render_template, redirect, session, url_for, flash, Response
from app import create_app
from app.forms import CommonForm
from app.yaml import WriteYaml

app = create_app()
app.system_status = "Stopped"
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
    context = {
        'module': 'home',
        'form_name': 'Welcome!',
        'system_status': app.system_status,
    }
    if request.method=='POST':
        context['system_status'] = app.system_status

    return render_template('home.html', **context)


@app.route('/system', methods=['POST'])
def system():
    """Systems control method

    Returns:
        context: Alert context to frontend modals
    """    
    system_request = request.form.to_dict()
    user_exec = system_request['system']
    if(user_exec == 'Start'):
        app.system_status = 'Running'
    else:
        app.system_status = 'Stopped'


    print("##Status_system --> "+user_exec) 


    return ({'result': True, 'info': 'Systems response to '+user_exec+' command'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
