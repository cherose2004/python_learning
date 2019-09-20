$(document).ready(function(){
  
  //banner
  var videoContainer = new Swiper('#videoContainer', {
		speed: 800,
		autoplay: 4000,
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
    pagination: '#videoPagination',
  });
  
  $("#videoPagination .swiper-pagination-bullet").hover(function() {
    $(this).click();
  },function() {
    videoContainer.autoplay.start();
  })

  //导航
  $('.video-category li').click(function(){
    $(this).addClass('category1').siblings().removeClass('category1');
    if ($(this).text() == '职场窍门') {
      $('.college-category').hide(150);
    } else {
      $('.college-category').show(150);
    }
  })

  $('.college-category li').click(function(){
    $(this).addClass('this').siblings().removeClass('this');
  })
  $('.sorting-way li').click(function(){
    $(this).addClass('this').siblings().removeClass('this');
  })

  //课程分批加载
  $(window).scroll(function() {
    //$(document).scrollTop() 滚动条位置距页面顶部的距离；
    //$(document).height() 整个页面的总高度； 
    //$(window).height() 当前窗口的高度；

    //判断是否已经滚动到页面底部；
    if ($(document).scrollTop() >= $(document).height() - $(window).height() - 180) {
      //切换正在加载的数据的图片状态为显示；
      $("#courseLoading").stop().animate({
        opacity: 1,
      }, 150).show();
      $.ajax({                                                                                                          //加载ajax；
        url: '',
        success: function(data) {
          //当请求成功时执行的回调函数；
          console.log('加载内容追击到id为courseBox的div中');
          //切换正在加载数据图片状态为不显示；
          $("#courseLoading").stop().animate({
            opacity: 0,
          }).hide();
        }
      });
    }
  }); 

})