$( ".card .imagem" ).each(function() {
  var attr = $(this).attr('data-img-src');
  var aux = '../..';
  
  attr = aux.concat(attr);

  if (typeof attr !== typeof undefined && attr !== false) {
    $(this).css('background-image', 'url('+attr+')');
  }

});
