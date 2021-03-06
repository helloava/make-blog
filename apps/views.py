# -*- coding: utf-8 -*-
from flask import render_template, request, render_template, url_for, redirect, flash
from apps import app, db
from sqlalchemy import desc
from apps.forms import ArticleForm, CommentForm
from apps.models import Article, Comment


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

#
#@index & article list
#


@app.route('/', methods=['GET'])
def article_list():
    # first scene showing thes lit of blog articles
    # html 파일에 전달할 데이터 Context
    context = {}

    context['article_list'] = Article.query.order_by(
        desc(Article.date_created)).all()
    # desc 는 내림차순

    return render_template('home.html', context=context, active_tab="timeline")


#
#@article controllers
#
@app.route('/article/create', methods=['GET', 'POST'])
def article_create():
    # view creating new articㅣe, saving the article in database
    form = ArticleForm()
    if request.method == 'GET':
        return render_template('article/create.html', form=form, active_tab='article_create')
    elif request.method == 'POST':
        article_data = request.form
        article = Article(
            title=article_data['title'],
            author=article_data['author'],
            category=article_data['category'],
            content=article_data['content']
        )

        db.session.add(article)
        db.session.commit()

        flash(u'게시글을 작성하였습니다.', 'success')

        return redirect(url_for('article_list'))


@app.route('/article/detail/<int:id>', methods=['GET'])
def article_detail(id):
    # show detail of the blog article and list of comments
    article = Article.query.get(id)
    comments = Comment.query.order_by(desc(Comment.date_created)).all()
    return render_template('article/detail.html', article=article, comments=comments)


@app.route('/article/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
    # controller editting blog article
    article = Article.query.get(id)
    form = ArticleForm(request.form, obj=article)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(article)
            db.session.commit()
        return redirect(url_for('article_detail', id=id))
    return render_template('article/update.html', form=form)


@app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
    # deleting blog's article
    if request.method == 'GET':
        return render_template('article/delete.html', article_id=id)
    elif request.method == 'POST':
        article_id = request.form['article_id']
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        flash(u'게시글을 삭제하였습니다.', 'success')
        return redirect(url_for('article_list'))


@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment(
                author=form.author.data,
                email=form.email.data,
                content=form.content.data,
                password=form.password.data,
                # article_id=article_id
            )
            db.session.add(comment)
            db.session.commit()

            flash(u'댓글을 작성하였습니다.', 'success')
        return redirect(url_for('article_detail', id=article_id))
    return render_template('comment/create.html', form=form)
