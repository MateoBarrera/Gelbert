from flask import render_template, request, redirect, flash, url_for, session, current_app as app
from . import advanced
from ..forms import PlannerForm, YoloForm, PreprocessForm_general, PreprocessForm_imu
from ..yaml import WriteYaml


@advanced.route('/', methods=['GET', 'POST'])
def advance():
    """Advance method - Advance page

    Returns:
        server response: Advance-page
    """
    planner_form = PlannerForm()
    yolo_form = YoloForm()
    preprocess_form_general = PreprocessForm_general()
    preprocess_form_imu = PreprocessForm_imu()
    context = {
        'module': 'advanced.advance',
        'forms_name': [['planner_form', 'Local Planner'], ['yolo_form', 'YOLO V5'], ['preprocess_form', 'Preprocess']],
        'forms_to_render': [['planner_form', planner_form], ['yolo_form', yolo_form], ['preprocess_form', [['general', preprocess_form_general], ['imu_filter', preprocess_form_imu]]]],
    }

    if request.method == 'POST':
        form_active = request.cookies.get('form_active')
        if planner_form.validate_on_submit() and form_active == 'planner_form':
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

        if  form_active == 'preprocess_form':
            #Capture the submit button name to specify the correct path in the .yaml file
            parents = [i for i in request.form.to_dict() if request.form.to_dict()[
                i] == "Update"]
            file_name = 'config/preprocess_node/preprocess_params.yaml'
            data = request.form.to_dict()
            del data['csrf_token']
            del data[parents[0]]
            yaml = WriteYaml()
            success, msg = yaml.dict_to_yaml(file_name, data, parents=parents)
            context['success'] = success
            context['success_text'] = msg

    return render_template('advanced.html', **context)
