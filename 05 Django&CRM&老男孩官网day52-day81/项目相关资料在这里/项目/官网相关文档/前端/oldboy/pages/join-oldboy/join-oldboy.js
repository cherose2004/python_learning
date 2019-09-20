$(document).ready(function(){
    $('.recruitment-list li .position').click(function(){
        if ($(this).children("p:last-child").text() == '-') {
            $(this).children("p:last-child").text('+');
        } else {
            $(this).children("p:last-child").text('-');
        }
        $(this).parent().siblings().find('.position').children("p:last-child").text('+');
        $(this).next().slideToggle().parent().siblings().find('.position-item').slideUp();
    })
})