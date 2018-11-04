document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('adminloggedin').innerHTML = 'Hello, ' + sessionStorage.getItem('username');
}, false);