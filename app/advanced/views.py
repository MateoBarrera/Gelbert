from flask import render_template, request, redirect, flash, url_for, session, current_app as app
from . import advanced
from ..forms import PlannerForm
from ..yaml import WriteYaml

yaml = WriteYaml()

@advanced.route('/', methods=['GET', 'POST'])
def advance():
    """Advance method - Advance page

    Returns:
        server response: Advance-page
    """
    planner_form = PlannerForm()
    context = {
        'module': 'advanced.advance',
        'form_name': 'Local Planner',
        'form_to_render': planner_form,
    }
    if planner_form.validate_on_submit():
        file_name = 'config/local_planner/params.yaml'
        data = request.form.to_dict()
        del data['csrf_token']
        del data['submit']
        yaml.dict_to_yaml(file_name, data)
        context['success'] = True
        context['success_text'] = file_name


    return render_template('advanced.html', **context)
