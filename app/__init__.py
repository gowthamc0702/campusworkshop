"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqhm9mbg5e4khsp6dg-a.oregon-postgres.render.com",
        database="todo_oju3",
        user="root",
        password="uVGV37hBwnzeFumSxOVN536DaEXzS5jP")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
