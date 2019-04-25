// ADD MODAL ============================================================
function tambahPenjualan() {
    // var quiz_id = document.getElementById("quiz").value;
    var nama_barang = $('input#namabarang_').val()
    var jumlah_barang = $('input#jumlahbarang_').val()
    var tanggal_transaksi = $('input#tanggaltransaksi_').val()


    console.log(nama_barang);
    console.log(jumlah_barang);
    console.log(tanggal_transaksi);


    $.ajax({
        url: `http://127.0.0.1:5000/addPenjualan`,
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            nama_barang : nama_barang,
            jumlah_barang : parseInt(jumlah_barang),
            tangal_pembelian: tanggal_transaksi
        }),
        success: function () {
            alert("anda berhasil menambahkan Modal Barang");
            window.location.href = 'listbarang.html'
        },
        error: function () {
            alert("cek semua inputanya");
        },
        complete: function () {
            console.log("mantul");
        }
    });
} 

