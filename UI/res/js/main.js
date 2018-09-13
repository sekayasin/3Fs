// Animate smooth scroll

$('#about').on('click', function() {
    const aboutus = $('#aboutus').position().top;
    
    $('html, body').animate(
        {
            scrollTop: aboutus
        },
        900
    );
});

$('#deliver').on('click', function() {
    const delivery = $('#delivery').position().top;
    
    $('html, body').animate(
        {
            scrollTop: delivery
        },
        900
    );
});

$('#hungry').on('click', function() {
    const hungry_signup = $('#hungry-signup').position().top;
    
    $('html, body').animate(
        {
            scrollTop: hungry_signup
        },
        900
    );
});


$('#show-me').on('click', function() {
    const meals = $('#meals').position().top;
    
    $('html, body').animate(
        {
            scrollTop: meals
        },
        900
    );
});