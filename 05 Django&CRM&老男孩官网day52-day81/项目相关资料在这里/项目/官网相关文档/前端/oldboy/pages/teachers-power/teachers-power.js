$(document).ready(function(){
    $('.teachers-nav li').click(function(){
        $(this).addClass('this').siblings().removeClass('this');
    })
    $('.teachers-group').click(function(){
        $(this).siblings().find('li section').hide();
        $(this).siblings().stop().animate({
            height:'360px'
        }, 200)
    })
    $('.teachers-group li .teacher-module').click(function(){
        $(this).parent().parent().stop().animate({
            height: '792px'
        }, 200)
        $(this).next().show().parent().siblings().find('section').hide();
    })
    $('.teacher-module').hover(function(){
        $(this).find('.name').stop().animate({
            bottom:'-70px'
        }, 200)
        $(this).find('.intro').stop().animate({
            top: '0px'
        }, 250)
    }, function(){
        $(this).find('.name').stop().animate({
            bottom: '0px'
        }, 250)
        $(this).find('.intro').stop().animate({
            top: '360px',
        }, 200)
    })

    $(document).bind("click", function (e) {
        var target = $(e.target);
        if (target.closest("#teacherWrap").length == 0) {
            $('.teachers-group').stop().animate({
                height: '360px'
            }, 200)
        }
    })
    
})