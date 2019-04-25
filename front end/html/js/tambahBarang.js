
// ADD MODAL ============================================================
function tambahBarang() {
    // var quiz_id = document.getElementById("quiz").value;
    var nama_barang = $('input#namabarang_').val()
    var jumlah_barang = $('input#jumlahbarang_').val()
    var satuan = $('input#satuan_').val()
    var harga_beli = $('input#hargabeli_').val()
    var harga_jual = $('input#hargajual_').val()
 

    console.log(nama_barang);
    console.log(jumlah_barang);
    console.log(satuan);
    console.log(harga_beli);
    console.log(harga_jual);


    $.ajax({
        url: `http://127.0.0.1:5000/addModal`,
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            lapak_id : 1,
            nama_barang : nama_barang,
            jumlah_barang: jumlah_barang,
            satuan : satuan,
            harga_beli: harga_beli,
            harga_jual: harga_jual,
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

// ADD MODAL ======================================
