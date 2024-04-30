import pymysql
import magic_address_processor
from flask import Flask, request

app = Flask(__name__)


@app.route("/address")
def get_address():
    user_id = request.values.get("user_id")

    db = pymysql.connect("localhost")
    cursor = db.cursor()

    cursor.execute(f"SELECT street FROM address WHERE user_id = '{user_id}'")

    record = cursor.fetchone()
    if record is None:
        return "No address found for user", 404
    db.close()

    return magic_address_processor.do(record[0])
