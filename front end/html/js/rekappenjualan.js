// LOOPING QUZZES========================================
// jquery ajax
// sama seperti xmlHttpRequest
// sama seperti xmlHttpRequest
$.ajax({
    url: 'http://127.0.0.1:5000/getAllPenjualan',
    method: 'GET',
    // type: 'GET,
    // data:[],{}, string, int, JSON, stringify,[{}] --> kalo misalnya api 
    success: function (rekaPenjualan) {
        var totalSaldo = 0
        for (var i = 0; i < rekaPenjualan.length; i++) {
            var card =
                `
                <div class="card" style="width: 18rem; margin-right: 10px; margin-top: 10px;">
                <img src="../image/sold.png" class="card-img-top" alt="..." style:"width:50px; height:50px;">
                <div class="card-body">
                    <h5 class="card-title">Nama Barang : ${rekaPenjualan[i].nama_barang}</h5>
                    <h5 class="card-text">Tejual : ${rekaPenjualan[i].jumlah_barang}</h5>
                    <h5 class="card-text">Tanggal Transaksi : ${rekaPenjualan[i].tangal_pembelian} </h5>
                </div>
            </div>
            `
            $('#listbarang').append(card)

        }
        document.getElementById("saldo").innerHTML = totalSaldo
    }
})
// LOOPING QUZZES========================================