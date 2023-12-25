#!interpreter [optional-arg]
# -*- coding: utf-8 -*-
#
"""
task_routes.py

"""

#Built-in/Generic
import datetime

#Libs
from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
		Table, Column, Integer, String, MetaData, ForeignKey, Boolean
	)


#Modules
from flask_app import db, app
from models import Task

@app.route("/task_create", methods=('GET', 'POST'))
def task_create():
	
	if request.method == 'POST':
		
		title = request.form['new_task']
		
		new_task = Task(title=title)

		db.session.add(new_task)
		db.session.commit()
	
	return redirect(request.referrer)


