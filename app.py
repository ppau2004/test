from datetime import datetime
from flask import render_template, redirect, request
#from FlaskWebProject7 import app
import pypyodbc
# creating connection Object which will contain SQL Server Connection
connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=Test;uid=sa;pwd=sA1234')  # Creating Cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM Test")
s = "<table style='border:1px solid red'>"
for row in cursor:
    s = s + "<tr>"
    for x in row:
        s = s + "<td>" + str(x) + "</td>"
    s = s + "</tr>"
connection.close()
@app.route('/')
@app.route('/home')
def home():
    return "<html><body>" + s + "</body></html>"