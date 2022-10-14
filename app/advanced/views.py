from flask import render_template, redirect, flash, url_for, session, current_app as app
from . import advanced

@advanced.route('/', methods=['GET', 'POST'])
def advance():
    context = {
        'message': 'Advanced route',
    }
    return render_template('advanced.html', **context)
