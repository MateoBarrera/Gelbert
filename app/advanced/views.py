from flask import render_template, request, redirect, flash, url_for, session, current_app as app
from . import advanced
from ..forms import PlannerForm, YoloForm, PreprocessForm_general, PreprocessForm_imu, PreprocessForm_blur, IsaacForm_general,IsaacForm_disparity, IsaacForm_pointclouds, ZedcommonForm
from ..yaml import WriteYaml


@advanced.route('/', methods=['GET', 'POST'])
def advance():
    """Advance method - Advance page

    Returns:
        server response: Advance-page
    """
    #INIT Forms to render
    planner_form = PlannerForm()
    yolo_form = YoloForm()
    preprocess_form_general = PreprocessForm_general()
    preprocess_form_imu = PreprocessForm_imu()
    preprocess_form_blur = PreprocessForm_blur()
    isaac_form_general = IsaacForm_general()
    isaac_form_disparity = IsaacForm_disparity()
    isaac_form_pointclouds = IsaacForm_pointclouds()
    zedcommon_form = ZedcommonForm()

    context = {
        'module': 'advanced.advance',
        'forms_name': [['planner_form', 'Local Planner'],
                       ['yolo_form', 'YOLO V5'],
                       ['preprocess_form', 'Preprocess'],
                       ['isaac_form', 'Isaac'],
                       ['zedcommon_form', 'ZED Common']
                       ],
        'forms_to_render': [['planner_form', planner_form],
                            ['yolo_form', yolo_form],
                            ['preprocess_form', [['general', preprocess_form_general], [
                                'imu_filter', preprocess_form_imu], ['blur', preprocess_form_blur]]],
                            ['isaac_form', [['general', isaac_form_general], [
                                'disparity', isaac_form_disparity], ['pointclouds', isaac_form_pointclouds]]],
                            ['zedcommon_form', zedcommon_form]],
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

        if (preprocess_form_general.validate_on_submit() or preprocess_form_blur.validate_on_submit() or preprocess_form_imu.validate_on_submit()) and form_active == 'preprocess_form':
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
        
        if (isaac_form_general.validate_on_submit() or isaac_form_disparity.validate_on_submit() or isaac_form_pointclouds.validate_on_submit()) and form_active == 'isaac_form':
            #Capture the submit button name to specify the correct path in the .yaml file
            parents = [i for i in request.form.to_dict() if request.form.to_dict()[
                i] == "Update"]
            file_name = 'config/isaac/isaac_params.yaml'
            data = request.form.to_dict()
            del data['csrf_token']
            del data[parents[0]]
            yaml = WriteYaml()
            success, msg = yaml.dict_to_yaml(file_name, data, parents=parents)
            context['success'] = success
            context['success_text'] = msg

        if zedcommon_form.validate_on_submit() and form_active == 'zedcommon_form':
            parents = ['video']
            data = request.form.to_dict()
            file_name = 'config/zed_wrapper/common.yaml'
            data = request.form.to_dict()
            del data['csrf_token']
            del data['submit']
            yaml = WriteYaml()
            success, msg = yaml.dict_to_yaml(file_name, data, parents=parents)
            context['success'] = success
            context['success_text'] = msg

    return render_template('advanced.html', **context)
