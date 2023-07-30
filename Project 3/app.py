from flask import Flask, redirect, render_template, flash, url_for, request
import sqlite3 as sql

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database.db')
