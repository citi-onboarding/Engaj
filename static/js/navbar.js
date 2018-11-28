function corverde() {
    $('.navbar').css('background-color','#FFFFFF');
    $('.navbar').css('transition-delay','0s');
        $('.navbarlogo').css('background-image','url(static/img/engaj-verde-alt.svg)');
        $('.link a').css('color','rgb(8,137,98)');
        $('.icon-facebook-alt').css('color','rgb(8,137,98)');
        $('.icon-instagram-alt').css('color','rgb(8,137,98)');
        $('.icon-menu').css('color','rgb(8,137,98)');
}

function cortransparente() {
    $('.navbar').css('transition','0.5s ease-out');
    $('.navbar').css('transition-delay','0.25s');
    $('.navbar').css('background-color','');
        $('.navbarlogo').css('background-image','url(static/img/engaj-branco-alt.svg)');
        $('.link a').css('color','#FFFFFF');
        $('.icon-facebook-alt').css('color','#FFFFFF');
        $('.icon-instagram-alt').css('color','#FFFFFF');
        $('.icon-menu').css('color','FFFFFF');
}


var c = 0;

$('.icon-menu').on("click", function() {
    if(c===0){
        c=1;
        $('.navbarmenusanduiche').animate({top:0, height:'toggle'},900);
        corverde();
    }else{
        c=0;
        $('.navbarmenusanduiche').animate({height:'toggle'},250);
        if($(window).scrollTop() < $(window).height()){
            cortransparente();
        }
    }
    
})

$(window).on("scroll", function() {
    if($(window).scrollTop() < $(window).height()){
        if(c===1) corverde();
        else cortransparente();
    } else{
        corverde();
    }
})


