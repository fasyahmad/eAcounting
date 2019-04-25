import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db


# MEMBER =================================================
class Member(db.Model):
    __tablename__ = 'members'
    id_member = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.Integer)
    ownerorbuyer = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    # penjualan = db.relationship('Pembeli', cascade='all,delete', backref='modal', lazy=True)

    def __init__(self, username, password, balance, ownerorbuyer):
        self.username = username
        self. password = password
        self. ownerorbuyer = ownerorbuyer
        self. balance = balance

    def __repr__(self):
        return '<member id {}>'.format(self.id_member)

    def serialize(self):
        return{
            'id_member': self.id_member,
            'username': self.username,
            'password': self.password,
            'ownerorbuyer': self.ownerorbuyer,
            'balance': self.balance
            # 'penjualan': [{'id_': item.id_, 'vendor_name': item.vendor_name, 'contract_start_date': item.contract_start_date, 'contract_end_date': item.contract_end_date} for item in self.contract_status]
        }
# MEMBER =================================================


# MODAL ==================================================
class Modal(db.Model):
    __tablename__ = 'modal'

    id_barang = db.Column(db.Integer, primary_key=True)
    lapak_id = db.Column(db.Integer())
    nama_barang = db.Column(db.String())
    jumlah_barang = db.Column(db.Integer)
    satuan = db.Column(db.String())
    harga_beli = db.Column(db.Integer)
    harga_jual = db.Column(db.Integer)
    terjual = db.relationship('Penjualan', cascade='all,delete',backref='modal', lazy=True)
    # penjualan = db.relationship('Pembeli', cascade='all,delete', backref='modal', lazy=True)

    def __init__(self,lapak_id, nama_barang, jumlah_barang, satuan, harga_beli, harga_jual):
        self.lapak_id = lapak_id
        self.nama_barang = nama_barang
        self. jumlah_barang = jumlah_barang
        self. satuan = satuan
        self. harga_beli = harga_beli
        self. harga_jual = harga_jual


    def __repr__(self):
        return '<modal id {}>'.format(self.id_barang)

    def serialize(self):
        jumlahTerjual = 0
        for terjual in self.terjual:
            jumlahTerjual+= terjual.jumlah_barang

        return{
            'id_barang': self.id_barang,
            'lapak_id': self.lapak_id,
            'nama_barang': self.nama_barang,
            'jumlah_barang': self.jumlah_barang,
            'satuan': self.satuan,
            'harga_beli': self.harga_beli,
            'harga_jual': self.harga_jual,
            'terjual': jumlahTerjual,
            'laba' : (jumlahTerjual*self.harga_jual)-(jumlahTerjual*self.harga_beli)
            # 'penjualan': [{'id_': item.id_, 'vendor_name': item.vendor_name, 'contract_start_date': item.contract_start_date, 'contract_end_date': item.contract_end_date} for item in self.contract_status]
        }
# MODAL =========================================================

# PENJUALAN =================================================
class Penjualan(db.Model):
    __tablename__ = 'penjualan'
    id_penjualan = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String, db.ForeignKey('modal.nama_barang'), nullable=False)
    jumlah_barang = db.Column(db.Integer)
    tangal_pembelian = db.Column(db.DateTime)
    # harga = db.relationship('Modal', cascade='all,delete',backref='penjualan', lazy=True)
    # penjualan = db.relationship('Pembeli', cascade='all,delete', backref='modal', lazy=True)

    def __init__(self, nama_barang, jumlah_barang, tangal_pembelian):
        self.nama_barang = nama_barang
        self. jumlah_barang = jumlah_barang
        self. tangal_pembelian = tangal_pembelian

    def __repr__(self):
        return '<member id {}>'.format(self.id_member)

    def serialize(self):
        return{
            'id_penjualan': self.id_penjualan,
            'nama_barang': self.nama_barang,
            'jumlah_barang': self.jumlah_barang,
            'tangal_pembelian': self.tangal_pembelian,
            # 'harga': [{'harga_beli': item.harga_beli, 'harga_jual': item.harga_jual} for item in self.harga]
            # 'penjualan': [{'id_': item.id_, 'vendor_name': item.vendor_name, 'contract_start_date': item.contract_start_date, 'contract_end_date': item.contract_end_date} for item in self.contract_status]
        }
# PENJUALAN =================================================
