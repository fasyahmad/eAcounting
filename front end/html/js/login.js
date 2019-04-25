function login() {
    var username_ = document.getElementById('username_').value
    var password_ = document.getElementById('password_').value

    console.log(username_);
    console.log(password_);

    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            username: username_,
            password: password_
        }),
        success: function (response) {
            console.log(response.username)
            console.log(response.password)
            console.log(response.id_member)
            alert("Sign In " + username_ + " berhasil")
            document.cookie = 'username=' + response.username
            document.cookie = 'id_member=' + response.id_member
            if (response.id_member == '1')
                window.location.href = 'listbarang.html';
            else if (response.id_member == '2')
                window.location.href = 'theKos.html';
        },
        error: function (error) {
            alert("masukkan username dan password dengan benar")
        },
        complete: function(e){

        }
    })
}
