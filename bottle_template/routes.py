"""
Routes and views for the bottle application.
"""

"""
Change UserProfile and AddPayslip "years":"2021" on 2022.

"""
from bottle import route, view, redirect, request, Bottle, run, template, get, post, static_file
from datetime import datetime
import random
import pymongo 
import json
from pymongo import MongoClient
from pandas import DataFrame
import pandas as pd
from bson import ObjectId
import requests
from bson.json_util import dumps


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.18r0y.mongodb.net/mongodb?retryWrites=true&w=majority")
db = client.qay
holiday = db.holiday

# mydb = myclient["performance_kpi"]
# main_table = mydb["main_table"]

@route('/manageUser')
def manageUserPage():
    
    column_title = DataFrame(list(main_table.find({})))
    column_title1 = list(main_table.find({},{"_id":0, "password":0}))
    print column_title
    return template('manageUser.html', column_title = column_title , column_title1 = column_title1)

@post('/addUser')
def addUser():
    staffname = request.forms.get("staffname") 
    kpi1 = request.forms.get("kpi1")                           
    kpi2 = request.forms.get("kpi2")
    kpi3 = request.forms.get("kpi3")

    insert = main_table.insert_one({"staffname": staffname , "kpi1": kpi1, "kpi2": kpi2, "kpi3": kpi3})

    column_title = dict(col_header.find({}))
    column_title = json.dumps(column_title)
    return template('manageUser.html', column_title = column_title)

@post('/addColumn')
def addColumn():
    return template('')

@route("/calendar")
def calendar():

    # holidays = DataFrame(list(holidays.find({})))

    df = DataFrame(list(holiday.find().sort([("date_holiday",pymongo.ASCENDING)])))

    calendar = DataFrame(list(holiday.find({},{'_id': 0, 'date_holiday':1, 'holiday_name':1}).sort([("date_holiday", pymongo.ASCENDING)])))

    title = []
    start = []
    test = [['All Day', '2021-03-01'], ['Qayyum Birthday', '2021-03-13']]

    for i in range(len(calendar)):
        title.append(calendar.holiday_name[i])
        
    for j in range(len(calendar)):
        start.append(calendar.date_holiday.dt.strftime('%Y-%m-%d')[j])
    
    
    q = list(zip(title,start))
    print q
    return template('displayCalendar.html', holidays= df, calendar= q)

@route("/isahamCalendar")
def calendar():

    # holidays = DataFrame(list(holidays.find({})))

    df = DataFrame(list(holiday.find().sort([("date_holiday",pymongo.ASCENDING)])))

    calendar = DataFrame(list(holiday.find({},{'_id': 0, 'date_holiday':1, 'holiday_name':1}).sort([("date_holiday", pymongo.ASCENDING)])))

    title = []
    start = []
    test = [['All Day', '2021-03-01'], ['Qayyum Birthday', '2021-03-13']]

    for i in range(len(calendar)):
        title.append(calendar.holiday_name[i])
        
    for j in range(len(calendar)):
        start.append(calendar.date_holiday.dt.strftime('%Y-%m-%d')[j])
    
    
    q = list(zip(title,start))
    print q
    return template('calendarClient.html', holidays= df, calendar= q)

@post('/addHolidays')
def addHolidays():

    date_holiday = request.forms.get("date_holiday")
    date_holiday = datetime.strptime(date_holiday, '%m/%d/%Y')
    holiday_name = request.forms.get("holiday_name")
    states = request.forms.get("states")
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day_holiday = date_holiday.weekday()
    day_holiday = day_name[day_holiday]

    print day_holiday

    insert = holiday.insert_one({"date_holiday": date_holiday, "day_holiday": day_holiday, "holiday_name": holiday_name, "description": states})

    df = DataFrame(list(holiday.find().sort([("date_holiday",pymongo.ASCENDING)])))
    calendar = DataFrame(list(holiday.find({},{'_id': 0, 'date_holiday':1, 'holiday_name':1}).sort([("date_holiday", pymongo.ASCENDING)])))

    for i in range(len(calendar)):
        title.append(calendar.holiday_name[i])
        
    for j in range(len(calendar)):
        start.append(calendar.date_holiday.dt.strftime('%Y-%m-%d')[j])
    
    
    q = list(zip(title,start))

    return template('displayCalendar.html', holidays= df, calendar=q)

@post('/deleteBursa')
def deleteBursa():

    deleteBursa = request.forms.get("deleteBursa")

    remove = holiday.delete_one({"holiday_name": deleteBursa})
    redirect('/calendar')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@route('/isahamquiz')
def isahamquiz():
    return template('quizisaham.html')