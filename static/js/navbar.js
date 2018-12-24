function corverde() {
    $('.navbartotal').css('transition-delay','0s');
    $('.navbartotal').css('background-color','#FFFFFF');
        $('.navbarlogo').css('background-image','url(static/img/logos/engaj-verde-alt.svg)');
        $('.link a').css('color','rgb(8,137,98)');
        $('.icon-facebook-alt').css('color','rgb(8,137,98)');
        $('.icon-instagram-alt').css('color','rgb(8,137,98)');
        $('.icon-menu').css('color','rgb(8,137,98)');
}

function cortransparente() {
    $('.navbartotal').css('transition','0.5s ease-out');
    $('.navbartotal').css('transition-delay','0.25s');
    $('.navbartotal').css('background-color','');
        $('.navbarlogo').css('background-image','url(static/img/logos/engaj-branco-alt.svg)');
        $('.link a').css('color','#FFFFFF');
        $('.icon-facebook-alt').css('color','#FFFFFF');
        $('.icon-instagram-alt').css('color','#FFFFFF');
        $('.icon-menu').css('color','FFFFFF');
}

var c = 0;

$('.icon-menu').on("click", function() {
    if(c===0){
        c=1;
        $('.navbarmenusanduiche').animate({top:0, height:'toggle'},300);
        corverde();
    }else{
        c=0;
        $('.navbarmenusanduiche').animate({height:'toggle'},300);
        if($(window).scrollTop() > ($(window).height() * 0.2)){
            corverde();
        }else cortransparente();
    }
    
})

$(window).on("scroll", function() {
    if($(window).scrollTop() < ($(window).height() * 0.2)) {
        if(c===1) corverde();
        else cortransparente();
    } else{
        corverde();
    }
})

$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
    
    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - ($(window).height() * 0.05)
    }, 800);
});




