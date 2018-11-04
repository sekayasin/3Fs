document.addEventListener('DOMContentLoaded', function() {
    sessionStorage.clear();

    // User Sigin Form - on Logout Page
    var mySiginFormLogoutPage = document.getElementById('mySiginFormLogoutPage')
    mySiginFormLogoutPage.addEventListener('submit', function(eventparameter){
        eventparameter.preventDefault();
        var data = JSON.stringify(signinFormData(mySiginFormLogoutPage));
        console.log(data);
        SigninUserLogoutPage(data);
    })

    function signinFormData(form){
        var text_elements = form.querySelectorAll('input[type="text"]');
        var pass_elements = form.querySelectorAll('input[type="password"]');
        var myData = {};
        for(var x = 0; x < text_elements.length; x++){
            var name = text_elements[x].name;
            var value = text_elements[x].value;
            myData[name] = value;
        }
        for(var x = 0; x < pass_elements.length; x++){
            var name = pass_elements[x].name;
            var value = pass_elements[x].value;
            myData[name] = value;
        }
        return myData;
    }

    function SigninUserLogoutPage(data) {
        const url = 'https://sekayasin-3fs-apiv2.herokuapp.com/auth/login';
        const myData = data;
        fetch(url, {
            method: 'post',
            headers: {"Content-type":"application/json; charset-utf-8"},
            body:myData
        })
        .then(response => response.json())
        .then( function(json_data){
            console.log(json_data);
            if(json_data.msg == "Invalid Username") {
                document.getElementById('usernameerror').innerHTML = '<span style="color:#ff0000">'+json_data.msg+'</span>';
                window.location.replace('../signinup/signin.html');
            }
            if(json_data.msg == "Invalid Password") {
                document.getElementById('userpasserror').innerHTML = '<span style="color:#ff0000">'+json_data.msg+'</span>';
                window.location.replace('../signinup/signin.html');
            }
            if(json_data.access_token) {
                sessionStorage.setItem('token', json_data.access_token);
                username = document.getElementById('username').value;
                sessionStorage.setItem('username', username);
                if (json_data.role_id === 2) {
                    window.location.replace('../userdashboard/dashboard.html');
                } else if(json_data.role_id === 1){
                    window.location.replace('../admindashboard/admindashboard.html');
                }
            }
        })
        .catch(error => console.log(error))
    }
}, false);
