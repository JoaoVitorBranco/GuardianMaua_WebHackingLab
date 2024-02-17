$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var username = $('#username').val();
        var password = $('#password').val();
        if (username === 'admin' && password === 'admin') {
            $('#message').text('Login successful! Redirecting...');
            setTimeout(function() {
                window.location.href = '/dashboard';
            }, 2000);
        } else {
            $('#message').text('Invalid username or password.');
        }
    });
});
