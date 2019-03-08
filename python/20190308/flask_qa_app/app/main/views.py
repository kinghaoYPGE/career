from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template, current_app
from app.utils import fetch_question

qa_bp = Blueprint('qa', __name__, url_prefix='')


@qa_bp.route('/')
def index():
    link, info = fetch_question(current_app.config['QUESTION_URL'])
    return render_template('index.html', link=link, info=info)
