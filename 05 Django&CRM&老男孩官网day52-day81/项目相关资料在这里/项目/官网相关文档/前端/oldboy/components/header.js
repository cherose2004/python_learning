
//logo切换
$('.logo').hover(function(){
  $('.nav-logo .logo .logo-img1').animate({marginLeft: '-165px'});
},function(){
  $('.nav-logo .logo .logo-img1').animate({marginLeft: '0'});
});

//跳转首页
$('.logo-img2').click(function(){
  console.log('跳回首页');
})

//滚动监听
$(window).scroll(function () {
  if ($(window).scrollTop() > 110) {
    $('.old-slogan').hide();
    $('header').addClass('headFixed');
    $('.nav-course').css('top', '80px');
    $('.main').css('margin-top', '80px');
  } else {
    $('.old-slogan').show();
    $('header').removeClass('headFixed');
    $('.nav-course').css('top', '110px');
    $('.main').css('margin-top', '0');
  }
});

$('.course-center').hover(function(){
  $('.nav-course').stop().animate({
    height: '140px',
  }, 250).show()
}, function(){
  $('.nav-course').stop().animate({
    height: '0px',
  }, 250)
})

$('.nav-course').hover(function(){
  $(this).show();
  $(this).stop().animate({
    height: '140px',
  }, 250).show();
}, function(){
  $(this).stop().animate({
    height: '0px',
  }, 250)
})

$('.region-toggle').hover(function(){
  $('.region-list').stop().animate({
    height: '182px',
  }, 250).show()
},function(){
  $('.region-list').stop().animate({
    height: '0px',
  }, 250)
})

$('.region-list li').click(function(){
  $('.region-default img').attr('src',$(this).find('img')[0].src); 
  $('.region-default span').html($(this).text());
  $('.region-list').stop().animate({
    height: '0px',
  }, 250)
})

