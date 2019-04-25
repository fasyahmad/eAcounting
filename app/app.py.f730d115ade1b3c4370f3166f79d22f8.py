from flask import Flask, jsonify, request, json, make_response
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models import Modal, Pembeli
from random import randint
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user': 'postgres',
    'pw': 'fasyaemad03',
    'db': 'accounting',
    'host': 'localhost',
    'port': '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# postgresql://username:password@localhost:5432/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)


@app.route('/addModal', methods=["POST"])
def addModal():

    body = request.json

    nama_barang = body['nama_barang']
    jumlah_barang = body['jumlah_barang']
    satuan = body['satuan']
    harga_beli = body['harga_beli']
    harga_jual = body['harga_jual']


    try:
        modal = Modal(
            nama_barang=nama_barang,
            jumlah_barang=jumlah_barang,
            satuan=satuan,
            harga_beli=harga_beli,
            harga_jual=harga_jual,
        )

        db.session.add(modal)
        db.session.commit()
        return "add modal. barang id={}".format(modal.id_barang), 200

    except Exception as e:
        return(str(e)), 400
# ADD EMPLOYEE ============
# GET MODAL ===========
@app.route('/getAllModal', methods=["GET"])
def modal():
        try:
                modal = Modal.query.order_by(Modal.id_barang).all()
                return jsonify([usr.serialize()
                                for usr in modal])
        except Exception as e:
                return (str(e))
# GET MODAL ===========
# GET MODAL ===========
@app.route('/getModalBy/<idBarang_>', methods=["GET"])
def get_modal_by(idBarang_):
        try:
                modal = Modal.query.filter_by(
                    id_barang=idBarang_).first()
                return jsonify(purchase_order.serialize())
        except Exception as e:
                return (str(e))

# GET MODAL ===========
# DELETE  ====
@app.route('/deleteModal/<idBarang_>', methods=["DELETE"])
def delete_modal(idBarang_):
    try:
        modal = Modal.query.filter_by(id_barang=idBarang_).first()
        db.session.delete(modal)
        db.session.commit()
        return 'Model deleted'
    except Exception as e:
        return(str(e))
# DELETE ====


# PEMBELII ================
@app.route('/Order', methods=["POST"])
def order():

    body = request.json
    id_ = body['id_']
    jumlah_belanja = body['jumlah_belanja']


    try:
        pembeli = Pembeli(
            id_=id_,
            jumlah_belanja=jumlah_belanja
        )

        db.session.add(pembeli)
        db.session.commit()
        return "add modal. barang id={}".format(pembeli.id_pembeli), 200

    except Exception as e:
        return(str(e)), 400
# ADD EMPLOYEE ============
