#!interpreter [optional-arg]
# -*- coding: utf-8 -*-
#
"""
routes.py: All Routes 

"""

#Built-in/Generic
import datetime

#Libs
from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
		Table, Column, Integer, String, MetaData, ForeignKey, Boolean
	)
from sqlalchemy import or_

#Modules
from flask_app import db, app
from models import Task
import task_routes
from task_routes import *

	
@app.route("/")
def index():
	tasks = db.session.query(Task)
	return render_template('list/dashboard.html', tasks=tasks)
	
