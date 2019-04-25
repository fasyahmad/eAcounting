// LOOPING QUZZES========================================
// jquery ajax
// sama seperti xmlHttpRequest
// sama seperti xmlHttpRequest
$.ajax({
    url: 'http://127.0.0.1:5000/getAllModal',
    method: 'GET',
    // type: 'GET,
    // data:[],{}, string, int, JSON, stringify,[{}] --> kalo misalnya api 
    success: function (modal) {
        var totalSaldo = 0

        for (var i = 0; i < modal.length; i++) {
            totalSaldo+= modal[i].laba 
                var card =
                `
                <div class="card" style="width: 18rem; margin-right: 10px; margin-top: 10px;">
                <img src="../image/iwiw.png" class="card-img-top" alt="..." style:"width:50px; height:50px;">
                <div class="card-body">
                    <h5 class="card-title">${modal[i].nama_barang}</h5>
                    <p class="card-text">Harga Jual : Rp. ${modal[i].harga_jual} per ${modal[i].satuan} </p>
                    <p class="card-text">Harga Beli : Rp. ${modal[i].harga_beli} per ${modal[i].satuan} </p>
                    <p class="card-text">Laba : Rp. ${(modal[i].harga_jual * modal[i].jumlah_barang) - (modal[i].harga_beli * modal[i].jumlah_barang)} </p>
                    <p class="card-text">Tersisa : ${modal[i].jumlah_barang}</p>
                    <p class="card-text">Terjual : ${modal[i].terjual}</p>
                    <a href="#" class="btn btn-primary">Cek Barang</a>
                </div>
            </div>
            `
            $('#listbarang').append(card)

        }
        document.getElementById("saldo").innerHTML = totalSaldo
    }
})
// LOOPING QUZZES========================================