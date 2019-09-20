$(document).ready(function(){
  
    //同学说分批加载
    $(window).scroll(function() {
      //$(document).scrollTop() 滚动条位置距页面顶部的距离；
      //$(document).height() 整个页面的总高度； 
      //$(window).height() 当前窗口的高度；
  
      //判断是否已经滚动到页面底部；
      if ($(document).scrollTop() >= $(document).height() - $(window).height() - 180) {
        //切换正在加载状态为显示；
        $("#courseLoading").stop().animate({
          opacity: 1,
        }, 150).show();
        $.ajax({                                                                                                          //加载ajax；
          url: '',
          success: function(data) {
            //当请求成功时执行的回调函数；
            console.log('加载内容追击到数据中');
            //切换正在加载状态为不显示；
            $("#courseLoading").stop().animate({
              opacity: 0,
            }).hide();
          }
        });
      }
    }); 
  
  })