from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
