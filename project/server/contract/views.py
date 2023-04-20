import os
from flask import Blueprint, jsonify, request
from project.server import mysql
from project.server import mail
from flask_mail import Message
from project.server.utils.xml import write

contract_blueprint = Blueprint("contract", __name__, url_prefix='/api/contract')


@contract_blueprint.route("/list", methods=["GET"])
def get_list():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()

    msg = Message("Hello",
                  sender=os.getenv('MAIL_USERNAME'),
                  recipients=["receiver@staff.com"])

    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)
    return jsonify(data), 200


@contract_blueprint.route("/add", methods=["POST"])
def add():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
            mysql.connection.commit()
            data = 'Contact Added successfully'
            return jsonify(data), 200
        except Exception as e:
            data = 'Failed to Added Contact'
            return jsonify(data), 200


@contract_blueprint.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
        data = 'Contact Updated Successfully'
        mysql.connection.commit()
        return jsonify(data), 200


@contract_blueprint.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    data = 'Contact Removed Successfully'
    return jsonify(data), 200


@contract_blueprint.route('/contract/genxml', methods=['GET'])
def generate_xml():
    write()
    data = 'Generate XML Successfully'
    return jsonify(data), 200
