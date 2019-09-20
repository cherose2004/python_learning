$(document).ready(function(){
    $('.parallel .inp').click(function(){
        $(this).find('ul').slideToggle(200);
        $(this).siblings().find('ul').slideUp(200);
    })

    $('.drop-down li').click(function(){
        $(this).parent().siblings('span').text($(this).text());
    })

    $(window).scroll(function () {
        var pos = $('.steps-box').offset().top;
        var winTop = $(window).scrollTop();
        if (pos < winTop + window.innerHeight) {
            setTimeout(function(){$('.s1').show().stop().animate({top:'76px'}, 300)})
            setTimeout(function(){$('.s2').show().stop().animate({top:'76px'}, 300)}, 200)
            setTimeout(function(){$('.s3').show().stop().animate({top:'76px'}, 300)}, 400)
            setTimeout(function(){$('.s4').show().stop().animate({top:'76px'}, 300)}, 600)
            setTimeout(function(){$('.s5').show().stop().animate({top:'76px'}, 300)}, 800)
            setTimeout(function(){$('.s6').show().stop().animate({top:'76px'}, 300)}, 1000)
        }
      });
})