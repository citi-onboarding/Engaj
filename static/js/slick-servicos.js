$("#slick-servicos").slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: false,
  autoplaySpeed: 2000,
  prevArrow: $('.prev'),
  nextArrow: $('.next'),
  responsive:[
    {
      breakpoint: 900,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        dots: true,
        arrows: false,
        centerMode: false,
      }
    }
  ]
});