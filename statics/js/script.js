/**
 * Created by Becker on 16/5/16.
 */

$(document).ready(function () {
    // alert("good");
    $("#login").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username": user, "password": pwd}
        $.ajax({
            type: "post",
            url: "/",
            data: pd,
            cache: false,
            success: function (data) {
                // alert(data);
                window.location.href = "/user?user=" + data;
            },
            error: function () {
                alert("error")
            }
        });
        // alert("username: " + user)
    });

});