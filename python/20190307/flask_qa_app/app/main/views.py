#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, current_app, jsonify, request, redirect, url_for
from flask_login import current_user
from app.models import Question, Answer, Comment
from app.utils import fetch_question

qa_bp = Blueprint('qa', __name__, url_prefix='')


@qa_bp.route('/', methods=["GET"])
def index():
    link, info = fetch_question(current_app.config['QUESTION_URL'])
    return render_template("index.html", link=link, info=info, current_user=current_user)


@qa_bp.route('/question/add', methods=["GET"])
def add_question():
        return render_template("ask_question.html")


@qa_bp.route('/question', methods=["GET", "POST"])
def question_info():
    try:
        _form = request.form
        if request.method == "POST":
            if not current_user.is_authenticated:
                return jsonify(status="error", info=u"请先登录")
            Question(
                name=_form.get('title'),
                content=_form.get('content'),
                author_id=current_user.id
            ).save()
            return jsonify(status="success", info=u"发布成功")
        else:
            question_list = Question.query.filter().all()
            return render_template("questions.html", qss=question_list)
    except Exception as e:
        print(e)
        if request.method == "POST":
            return jsonify(status="error", info=u"参数错误"), 400
        else:
            return redirect(url_for('qa.index'))


@qa_bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def questions(question_id):
    try:
        if request.method == "GET":
            question_instance = Question.query.filter(Question.id==question_id).first()
            print(dir(question_instance))
            if question_instance:
                return render_template("question_detail.html", qs=question_instance)
            return redirect(url_for('qa.index'))
    except Exception as e:
        print(e)
        return redirect(url_for('qa.index'))


@qa_bp.route('/question/<int:question_id>/answer', methods=['POST'])
def add_answer(question_id):
    try:
        _form = request.form
        if not current_user.is_authenticated:
            return jsonify(status="error", info=u"请先登录")
        question_instance = Question.query.filter(Question.id==question_id).first()
        if not question_instance:
            return jsonify(status="error", info=u"不存在该问题")
        else:
            if _form['rtype'] == "1":
                """回答"""
                Answer(
                    content=_form.get('content'),
                    author_id=current_user.id,
                    question_id=question_id
                ).save()
                question_instance.answers_count += 1
                question_instance.save()
                return jsonify(status="success", info=u"回复成功")
            elif _form['rtype'] == "2":
                """评论"""
                answer_instance = Answer.query.filter(Answer.id==_form['rid']).first()
                if not answer_instance:
                    return jsonify(status="error", info=u"错误")
                Comment(
                    content=_form['content'],
                    author_id=current_user.id,
                    answer_id=answer_instance.id
                ).save()
                answer_instance.comments_count += 1
                answer_instance.save()
                return jsonify(status="success", info=u"评论成功")
            else:
                return jsonify(status="error", info=u"错误")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status="error", info=u"错误")


