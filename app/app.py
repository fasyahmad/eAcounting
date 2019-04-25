from flask import Flask, jsonify, request, json, make_response
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from models import Modal, Member, Penjualan
from random import randint
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)

POSTGRES = {
    'user': 'postgres',
    'pw': 'fasyaemad03',
    'db': 'skidipay',
    'host': 'localhost',
    'port': '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# postgresql://username:password@localhost:5432/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

# ADD MEMBERS ============================
@app.route('/addMember', methods=["POST"])
def addMember():

    body = request.json
    username = body['username']
    password = body['password']
    ownerorbuyer = body['ownerorbuyer']
    balance = body['balance']

    try:
        member = Member(
            username=username,
            password=password,
            ownerorbuyer=ownerorbuyer,
            balance=balance,
        )

        db.session.add(member)
        db.session.commit()
        return "add member. member id={}".format(member.id_member), 200

    except Exception as e:
        return(str(e)), 400
# ADD MEMBERS ======================
# GET MEMBERS ======================
@app.route('/getAllMembers', methods=["GET"])
def get_all_members():
        try:
                member = Member.query.order_by(Member.id_member).all()
                return jsonify([usr.serialize()
                                for usr in member])
        except Exception as e:
                return (str(e))
# GET MEMBERS ======================
# LOG IN ============
@app.route('/login', methods=['POST'])
def login():
    response = {}
    body = request.json
    username = body['username']
    password = body['password']
    isLogin = False

    try:
        members = get_all_members().json
        for member in members:
            if username == member['username']:
                if password == member['password']:
                    isLogin = True
                    id_member = member['id_member']

    except Exception as e:
        response['Error'] = str(e)
        # return str(e)

    if isLogin:
        response['message'] = 'Login success, welcome {}'.format(username)
        response['username'] = '{}' .format(username)
        response['id_member'] = '{}' .format(id_member)
        code = 200
    else:
        response['message'] = 'Login failed, username or password is wrong'
        code = 400
    return jsonify(response), code

# LOG IN ============

@app.route('/addModal', methods=["POST"])
def addModal():

    body = request.json
    lapak_id = body['lapak_id']
    nama_barang = body['nama_barang']
    jumlah_barang = body['jumlah_barang']
    satuan = body['satuan']
    harga_beli = body['harga_beli']
    harga_jual = body['harga_jual']


    try:
        modal = Modal(
            lapak_id=lapak_id,
            nama_barang=nama_barang,
            jumlah_barang=jumlah_barang,
            satuan=satuan,
            harga_beli=harga_beli,
            harga_jual=harga_jual
        )

        db.session.add(modal)
        db.session.commit()
        return "add modal. barang id={}".format(modal.id_barang), 200

    except Exception as e:
        return(str(e)), 400
# GET MODAL ===========
@app.route('/getAllModal', methods=["GET"])
def get_all_modal():
        try:
                modal = Modal.query.order_by(Modal.id_barang).all()
                return jsonify([usr.serialize()for usr in modal])
        except Exception as e:
                return (str(e))
# GET MODAL ===========
# GET NAMA BARANG  ===========
@app.route('/getAllNamaBarang', methods=["GET"])
def get_all_nama_barang():
        try:
                modal = Modal.query.order_by(Modal.id_barang).all()
                return jsonify([usr.serialize()for usr in modal])
        except Exception as e:
                return (str(e))
# GET NAMA BARANG ===========
# GET MODAL ===========
@app.route('/getModalByLapakId/<lapakId_>', methods=["GET"])
def get_modal_by_lapakId(lapakId_):
        try:
                modal = Modal.query.filter_by(lapak_id=lapakId_).all()
                return jsonify([usr.serialize()for usr in modal])
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

# ADD PENJUALAN ============================
@app.route('/addPenjualan', methods=["POST"])
def addPenjualan():

    body = request.json
    nama_barang = body['nama_barang']
    jumlah_barang = body['jumlah_barang']
    tangal_pembelian = body['tangal_pembelian']

    try:
        penjualan = Penjualan(
            nama_barang=nama_barang,
            jumlah_barang=jumlah_barang,
            tangal_pembelian=tangal_pembelian
        )
    

        db.session.add(penjualan)
        db.session.commit()

        # update ke tabel modal

        modal = db.session.query(Modal).filter_by(nama_barang=nama_barang).first()
        barangA = (modal.serialize())
        jumlahSebelumTerjual = barangA["jumlah_barang"]
        jumlahSetelahTerjual = jumlahSebelumTerjual - jumlah_barang

        Modal.query.filter_by(nama_barang=nama_barang).update(dict(jumlah_barang=jumlahSetelahTerjual))

        db.session.commit()
        modal.serialize()
        return "add penjualan. id penjualan={}".format(penjualan.id_penjualan), 200

    except Exception as e:
        return(str(e)), 400
# ADD PENJUALAN ======================
# GET PENJUALAN ======================
@app.route('/getAllPenjualan', methods=["GET"])
def get_all_penjualan():
        try:
                penjualan = Penjualan.query.order_by(Penjualan.id_penjualan).all()
                return jsonify([usr.serialize()
                                for usr in penjualan])
        except Exception as e:
                return (str(e))
# GET PENJUALAN ======================
# DELETE PEMBELIAN ===================
@app.route('/deletepenjualan/<idPenjualan_>', methods=["DELETE"])
def delete_penjualan(idPenjualan_):
    try:
        penjualan = Penjualan.query.filter_by(id_penjualan=idPenjualan_).first()
        db.session.delete(penjualan)
        db.session.commit()
        return 'penjualan deleted'
    except Exception as e:
        return(str(e))
# DELETE PEMBELIAN ====================
