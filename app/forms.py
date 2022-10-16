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
        'KP', validators=[Optional()], render_kw={"value": "5.0"}, description="Attractive potential gain.")
    ETA = DecimalField(
        'ETA',  validators=[Optional()], render_kw={"value": "100.0"}, description="Repulsive potencial gain.")
    AREA_WIDTH = DecimalField(
        'Area width',  validators=[Optional()], render_kw={"value": "2"}, description="Potential area in meters.")
    OSCILLATIONS_DETECTION_LENGTH = DecimalField(
        'Oscillations detection length', validators=[Optional()], render_kw={"value": "3"}, description="# of prev positions to check oscillations.")   
    Maximun_distance = DecimalField(
        'Maximum distance', validators=[Optional()], render_kw={"value": "2.5"}, description="Distance in meters to search free space and calculate paths.")
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

class PreprocessForm_general(FlaskForm):
    """Form Preprocess general params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    blur_filter = BooleanField(
        'Blur filter', validators=[Optional()])
    use_hist_equ = BooleanField(
        'Use hist equ',  validators=[Optional()])
    left_image_topic = StringField(
        'left_image_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/image_rect_color"}, description="ROS topic string.")
    left_camera_info_topic = StringField(
        'left_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/camera_info"},  description="ROS topic string.")
    right_image_topic = StringField(
        'right_image_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/right/image_rect_color"},  description="ROS topic string.")
    right_camera_info_topic = StringField(
        'right_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/right/camera_info"},  description="ROS topic string.")
    general = SubmitField('Update')  # Submit Button

class PreprocessForm_imu(FlaskForm):
    """Form Preprocess imu filter params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    max_angle = DecimalField(
        'Maximum angle', validators=[Optional()], render_kw={"value": 45}, description="The maximum angle difference / head inclination before the filter of images.")
    num_samples = DecimalField(
        'Number of samples',  validators=[Optional()], render_kw={"value": 20}, description="Number of samples to use for the initial reference of the Imu / TF tree.")
    imu_filter = SubmitField('Update')  # Submit Button

class PreprocessForm_blur(FlaskForm):
    """Form Preprocess blur params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    kernel_size = DecimalField(
        'Kernel size', validators=[Optional()], render_kw={"value": 3}, description="Ther kernel size of the Sobel operator used by the Laplacian.")
    minZero = DecimalField(
        'MinZero',  validators=[Optional()], render_kw={"value": 100}, description="The decision threshold between non blur and blur image.")
    blur = SubmitField('Update')  # Submit Button


class IsaacForm_general(FlaskForm):
    """Form Isaac general params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    left_image_topic = StringField(
        'left_image_topic', validators=[Optional()], render_kw={"value": "/gelbert/left/image_rect_color"}, description="ROS topic string.")
    left_camera_info_topic = StringField(
        'left_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/left/camera_info"},  description="ROS topic string.")
    right_image_topic = StringField(
        'right_image_topic', validators=[Optional()], render_kw={"value": "/gelbert/right/image_rect_color"},  description="ROS topic string.")
    right_camera_info_topic = StringField(
        'right_camera_info_topic', validators=[Optional()], render_kw={"value": "/zedm/zed_node/right/camera_info"},  description="ROS topic string.")
    general = SubmitField('Update')  # Submit Button


class IsaacForm_disparity(FlaskForm):
    """Form Preprocess Issac disparity filter params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    backends  = StringField(
        'Backends', validators=[Optional()], render_kw={"value": 'CUDA'}, description="The VPI backend to use, which is CUDA by default (options: 'CUDA', 'XAVIER', 'ORIN').")
    max_disparity = DecimalField(
        'Maximum disparity',  validators=[Optional()], render_kw={"value": 64}, description="The maximum value for disparity per pixel, which is 64 by default. With ORIN backend, this value must be 128 or 256.")
    disparity = SubmitField('Update')  # Submit Button


class IsaacForm_pointclouds(FlaskForm):
    """Form Preprocess Issac disparity filter params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    use_color = BooleanField(
        'Use color', validators=[Optional()])
    pointclouds = SubmitField('Update')


class ZedcommonForm(FlaskForm):
    """Form Zed common params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """
    
    extrinsic_in_camera_frame = BooleanField(
        'Extrinsic in camera frame', validators=[Optional()], description="If `false` extrinsic parameter in `camera_info` will use ROS native frame (X FORWARD, Z UP) instead of the camera frame (Z FORWARD, Y DOWN).")
    img_downsample_factor = DecimalField(
        'img_downsample_factor', validators=[Optional()], render_kw={"value": 0.5}, description="Resample factor for image data matrices [0.01,1.0] The SDK works with native data sizes, but publishes rescaled matrices.")
    brightness = DecimalField(
        'Brightness', validators=[Optional()], render_kw={"value": 4}, description="[DYNAMIC]")
    contrast = DecimalField(
        'Contrast', validators=[Optional()], render_kw={"value": 4}, description="[DYNAMIC]")
    hue = DecimalField(
        'hue', validators=[Optional()], render_kw={"value": 0}, description="[DYNAMIC]")
    saturation = DecimalField(
        'Saturation', validators=[Optional()], render_kw={"value": 4}, description="[DYNAMIC]")
    sharpness = DecimalField(
        'Sharpness', validators=[Optional()], render_kw={"value": 4}, description="[DYNAMIC]")
    gamma = DecimalField(
        'Gamma', validators=[Optional()], render_kw={"value": 8}, description="[DYNAMIC] - Requires SDK >=v3.1.")
    auto_exposure_gain = BooleanField(
        'Auto exposure gain', validators=[Optional()], description="[DYNAMIC]")
    exposure = DecimalField(
        'Exposure', validators=[Optional()], render_kw={"value": 80}, description="[DYNAMIC]")
    gain = DecimalField(
        'Gain', validators=[Optional()], render_kw={"value": 80}, description="[DYNAMIC]")
    auto_whitebalance = BooleanField(
        'Auto whitebalance', validators=[Optional()], description="[DYNAMIC]")
    whitebalance_temperature = DecimalField(
        'Whitebalance temperature', validators=[Optional()], render_kw={"value": 42}, description="[DYNAMIC] - [28,65] works only if `auto_whitebalance` is false.")
    qos_history = DecimalField(
        'qos_history', validators=[Optional()], render_kw={"value": 1}, description="'1': KEEP_LAST - '2': KEEP_ALL.")
    qos_depth = DecimalField(
        'qos_depth', validators=[Optional()], render_kw={"value": 1}, description="'1': KEEP_LAST - '2': KEEP_ALL.")
    qos_reliability = DecimalField(
        'qos_reliability', validators=[Optional()], render_kw={"value": 1}, description="'1': RELIABLE - '2': BEST_EFFORT.")
    qos_durability = DecimalField(
        'qos_durability', validators=[Optional()], render_kw={"value": 2}, description="'1': TRANSIENT_LOCAL - '2': VOLATILE.")
    submit = SubmitField('Update')  # Submit Button
