from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
