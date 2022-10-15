from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Regexp, Length, Optional, Email

class CommonForm(FlaskForm):
    """Form general params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """    
    user_height = DecimalField(
        'User height', validators=[InputRequired()], render_kw={"value": "1.7"}, description="Meters")
    use_detection = BooleanField(
        'Use detection', validators=[Optional()])  # if True, the detection mode is activated
    use_planning= BooleanField(
        'Use planning', validators=[Optional()])  # if True, the local planner mode is activated
    maximum_pcl_obstacles = DecimalField(
        'Max. PCL Obstacles', validators=[InputRequired()], render_kw={"value":"3"}, description="Max. number of obstacles")  # Maximum number of "detected" obstacles in the PointCloud to describe to the user
    detection_msg_period = DecimalField(
        'Detection message period', validators=[InputRequired()], render_kw={"value":"4"}, description="seconds")  # Time in seconds (NO ESTA SIENDO USADO AUN)
    detection_msg_period = DecimalField(
        'Detection message period', validators=[InputRequired()], render_kw={"value": "4"},  description="seconds")  # Time in seconds (NO ESTA SIENDO USADO AUN)
    submit = SubmitField('Update')  # Submit Button

class PlannerForm(FlaskForm):
    """Form Local Planner params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    KP = DecimalField(
        'KP', validators=[Optional()], render_kw={"value": "5.0"}, description="attractive potential gain")
    ETA = DecimalField(
        'ETA',  validators=[Optional()], render_kw={"value": "100.0"}, description="repulsive potencial gain")
    AREA_WIDTH = DecimalField(
        'Area width',  validators=[Optional()], render_kw={"value": "2"}, description="potential area [m]")
    OSCILLATIONS_DETECTION_LENGTH = DecimalField(
        'Oscillations detection length', validators=[Optional()], render_kw={"value": "3"}, description="# of prev positions to check oscillations")   
    Maximun_distance = DecimalField(
        'Maximum distance', validators=[Optional()], render_kw={"value": "2.5"}, description="Distance [m] to search free space and calculate paths")
    submit = SubmitField('Update')  # Submit Button

class YoloForm(FlaskForm):
    """Form Yolo V5 params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    weights = StringField(
        'Weights', validators=[Optional()], render_kw={"value": "Yolov5_S_Freeze_subir4_pto_simpl_half.engine"})
    data = StringField(
        'data',  validators=[Optional()], render_kw={"value": "data.yaml"})
    confidence_threshold = DecimalField(
        'Confidence threshold',  validators=[Optional()], render_kw={"value": "0.25"})
    iou_threshold = DecimalField(
        'Iou threshold', validators=[Optional()], render_kw={"value": "0.45"})
    maximum_detections = DecimalField(
        'Maximum detections', validators=[Optional()], render_kw={"value": "10"})
    inference_size_ = DecimalField(
        'Inference size', validators=[Optional()], render_kw={"value": "416"})
    input_image_topic = StringField(
        'Input image topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/image_rect_color"})
    submit = SubmitField('Update')  # Submit Button

class PreprocessForm(FlaskForm):
    """Form Preprocess params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    blur_filter = BooleanField(
        'Blur filter', validators=[Optional()])
    use_hist_equ = BooleanField(
        'Use hist equ',  validators=[Optional()])
    left_image_topic = StringField(
        'left_image_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/image_rect_color"}, description="ROS topic string")
    left_camera_info_topic = StringField(
        'left_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/camera_info"},  description="ROS topic string")
    right_image_topic = StringField(
        'right_image_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/right/image_rect_color"},  description="ROS topic string")
    right_camera_info_topic = StringField(
        'right_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/right/camera_info"},  description="ROS topic string")
    submit = SubmitField('Update')  # Submit Button
