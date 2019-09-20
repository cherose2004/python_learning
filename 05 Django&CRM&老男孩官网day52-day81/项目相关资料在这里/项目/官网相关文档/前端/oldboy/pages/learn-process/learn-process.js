$(document).ready(function(){
    $('.all-course .full a').removeAttr('href');
    $('.all-course .full a').removeAttr('target');

    $('.menu-title .right div').click(function(){
        $(this).find('ul').slideToggle(150);
    })

    $('.right div ul li').click(function(){
        $(this).parent().prev().find('span').text($(this).text());
    })

    $('.all-course .reports').click(function(){
        $('.baomin-wrap').show();
    })

    $('.close').click(function(){
        $('.baomin-wrap').hide();
    })
})