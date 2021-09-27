from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField
from yong.models.predict_model import Predict

import joblib

bp = Blueprint('test', __name__, url_prefix='/test')





@bp.route('/form', methods=['GET', 'POST'])
def form():

    return render_template('test_form.html')



