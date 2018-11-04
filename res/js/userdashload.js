document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('usernameloggedin').innerHTML = 'Welcome, ' + sessionStorage.getItem('username');
}, false);