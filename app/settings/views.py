from flask import render_template, redirect, flash, url_for, session, current_app as app
from . import settings


@settings.route('/', methods=['GET', 'POST'])
def setting():
    context = {
        'module': 'settings.setting',
        'message': 'Settings route',
    }
    return render_template('settings.html', **context)
