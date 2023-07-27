from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
app.route('/index')
def index():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
