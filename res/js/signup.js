
// HTML 5 Vanila Js Confirm Password validation
var real_password = document.getElementById('password'), confirm_pass = document.getElementById('confirm_pass')

function validatePass(){
    if (real_password.value !== confirm_pass.value) {
        confirm_pass.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_pass.setCustomValidity('');
    }
}

real_password.onchange = validatePass;
confirm_pass.onkeyup = validatePass;


// User Sign up Form
var mySignupForm = document.getElementById('mySignupForm')
mySignupForm.addEventListener('submit', function(eventparameter){
    eventparameter.preventDefault();
    var data = JSON.stringify(signupFormData(mySignupForm));
    console.log(data);
    SignupUser(data);
})

function signupFormData(form){
    var text_elements = form.querySelectorAll('input[type="text"]');
    var email_elements = form.querySelectorAll('input[type="email"]');
    var tel_elements = form.querySelectorAll('input[type="tel"]');
    var myData = {};

    for(var x = 0; x < text_elements.length; x++){
        var name = text_elements[x].name;
        var value = text_elements[x].value;
        myData[name] = value;
    }

    myData[document.getElementById('password').name] = document.getElementById('password').value

    for(var x = 0; x < email_elements.length; x++){
        var name = email_elements[x].name;
        var value = email_elements[x].value;
        myData[name] = value;
    }
    for(var x = 0; x < tel_elements.length; x++){
        var name = tel_elements[x].name;
        var value = tel_elements[x].value;
        myData[name] = value;
    }
    return myData;
}

function SignupUser(data) {
    const url = 'https://sekayasin-3fs-apiv2.herokuapp.com/auth/signup';
    const myData = data;
    fetch(url, {
        method: 'post',
        headers: {"Content-type":"application/json; charset-utf-8"},
        body:myData
    })
    .then(response => response.json())
    .then( function(json_data){
        console.log(json_data);
        if(json_data.message == "Username Available, Try Again") {
            document.getElementById('usernametaken').innerHTML = '<span style="color:#ff0000">'+json_data.message+'</span>';
            
            setTimeout(() => window.location.reload(true), 3000);
            
        }

        if(json_data.message == "Email Available, Try Again") {
            document.getElementById('emailtaken').innerHTML = '<span style="color:#ff0000">'+json_data.message+'</span>';
            
            setTimeout(() => window.location.reload(true), 3000);
        }

        if(json_data.message == "Success") {
            alert("Your Account Successful created, Redirecting to sigin page");
            setTimeout(() => window.location.replace('../signinup/signin.html'), 3000);
        }
    })
    .catch(error => console.log(error))
}
