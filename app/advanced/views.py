from flask import render_template, request, redirect, flash, url_for, session, current_app as app
from . import advanced
from ..forms import PlannerForm, YoloForm
from ..yaml import WriteYaml

@advanced.route('/', methods=['GET', 'POST'])
def advance():
    """Advance method - Advance page

    Returns:
        server response: Advance-page
    """
    planner_form = PlannerForm()
    yolo_form = YoloForm()
    context = {
        'module': 'advanced.advance',
        'forms_name': [['planner_form', 'Local Planner'], ['yolo_form', 'YOLO V5']],
        'forms_to_render': [['planner_form', planner_form], ['yolo_form', yolo_form]],
    }

    if request.method == 'POST':
        form_active = request.cookies.get('form_active')
        if planner_form.validate_on_submit() and form_active =='planner_form':
            data = request.form.to_dict()
            file_name = 'config/local_planner/params.yaml'
            data = request.form.to_dict()
            del data['csrf_token']
            del data['submit']
            yaml = WriteYaml()
            success, msg = yaml.dict_to_yaml(file_name, data)
            context['success'] = success
            context['success_text'] = msg

        if yolo_form.validate_on_submit() and form_active == 'yolo_form':
            file_name = 'config/yolov5/yolov5_params.yaml'
            parents = ['general']
            data = request.form.to_dict()
            del data['csrf_token']
            del data['submit']
            yaml = WriteYaml()
            success, msg = yaml.dict_to_yaml(file_name, data, parents=parents)
            context['success'] = success
            context['success_text'] = msg

    return render_template('advanced.html', **context)
