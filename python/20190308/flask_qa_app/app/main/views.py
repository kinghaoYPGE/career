from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template, current_app
from flask_login import current_user

from app.utils import fetch_question
from app.models import Question, Answer, Comment

qa_bp = Blueprint('qa', __name__, url_prefix='')


@qa_bp.route('/')
def index():
    link, info = fetch_question(current_app.config['QUESTION_URL'])
    return render_template('index.html', link=link, info=info)


@qa_bp.route('/question/add')
def add_question():
    return render_template('ask_question.html')


@qa_bp.route('/question', methods=['GET', 'POST'])
def question_info():
    try:
        _form = request.form
        if request.method == 'POST':
            if not current_user.is_authenticated:
                return jsonify(status='error', info='请先登录')
            Question(
                name=_form.get('title'),
                content=_form.get('content'),
                author_id=current_user.id
            ).save()
            return jsonify(status='success', info='发布成功')
        else:
            question_list = Question.query.filter().all()
            return render_template('questions.html', qss=question_list)

    except Exception as e:
        print(e)
        raise


@qa_bp.route('/questions/<int:question_id>')
def questions(question_id):
    question_instance = Question.query.filter(Question.id == question_id).first_or_404()
    print(dir(question_instance))
    if question_instance:
        return render_template('question_detail.html', qs=question_instance)
    return redirect(url_for('qa.index'))


@qa_bp.route('/question/<int:question_id>/answer', methods=['POST'])
def add_reply(question_id):
    _form = request.form
    if not current_user.is_authenticated:
        return jsonify(status='error', info='请先登录')
    question_instance = Question.query.filter(Question.id == question_id).first_or_404()
    if _form.get('rtype') == '1':
        # 回答
        Answer(
            content=_form.get('content'),
            author_id=current_user.id,
            question_id=question_id
        ).save()
        question_instance.answers_count += 1
        question_instance.save()
        return jsonify(status='success', info='回复成功')
    elif _form.get('rtype') == '2':
        answer_instance = Answer.query.filter(Answer.id==_form.get('rid')).first_or_404()
        # 评论
        Comment(
            content=_form.get('content'),
            author_id=current_user.id,
            answer_id=answer_instance.id
        ).save()
        answer_instance.comments_count += 1
        answer_instance.save()
        return jsonify(status='success', info='评论成功')


