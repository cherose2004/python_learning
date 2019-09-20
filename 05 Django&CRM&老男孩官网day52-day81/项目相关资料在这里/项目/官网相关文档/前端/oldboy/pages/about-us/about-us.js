$(document).ready(function(){
    $('.about-nav li').click(function(){
        setTimeout(function(){
            $(window).scrollTop($(window).scrollTop()-100)
        })
    })
    $('.full-video').click(function(){
        $('.video-popup').stop().animate({
            opacity: 1
        }).show();
    })
    $('.close-btn').click(function(){
        $('.video-popup').stop().animate({
            opacity: 0
        }).hide(100);
    })
})