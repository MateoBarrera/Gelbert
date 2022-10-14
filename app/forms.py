from lib2to3.pgen2.token import OP
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, DecimalField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Regexp, Length, Optional, Email

class CommonForm(FlaskForm):
    """Form general params

    Args:
        FlaskForm (WTF form): Parent class of wtf form for render content
    """    
    user_height = DecimalField(
        'User height', validators=[InputRequired()], render_kw={"placeholder": "1.7"}, description="Meters")
    use_detection = BooleanField(
        'Use detection', validators=[Optional()])  # if True, the detection mode is activated
    use_planning= BooleanField(
        'Use planning', validators=[Optional()])  # if True, the local planner mode is activated
    maximum_pcl_obstacles = DecimalField(
        'Max. PCL Obstacles', validators=[InputRequired()], render_kw={"placeholder":"3"}, description="Max. number of obstacles")  # Maximum number of "detected" obstacles in the PointCloud to describe to the user
    detection_msg_period = DecimalField(
        'Detection message period', validators=[InputRequired()], render_kw={"placeholder":"4"}, description="seconds")  # Time in seconds (NO ESTA SIENDO USADO AUN)
    detection_msg_period = DecimalField(
        'Detection message period', validators=[InputRequired()], render_kw={"placeholder": "4"},  description="seconds")  # Time in seconds (NO ESTA SIENDO USADO AUN)
    submit = SubmitField('Update')  # Submit Button
