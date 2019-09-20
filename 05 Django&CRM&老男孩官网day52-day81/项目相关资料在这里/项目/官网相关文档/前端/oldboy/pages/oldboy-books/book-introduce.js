$(document).ready(function(){
    if ($('.directory div').height() > 534) {
        $('.all1').show();
    } else {
        $('.all1').hide();
        $('.directory').css('height','auto');
    }

    if ($('.preface div').height() > 326) {
        $('.all2').show();
    } else {
        $('.all2').hide();
        $('.preface').css('height','auto');
    }

    $('.all').click(function(){
        $(this).hide().parent().prev().css('height','auto');
    })
})