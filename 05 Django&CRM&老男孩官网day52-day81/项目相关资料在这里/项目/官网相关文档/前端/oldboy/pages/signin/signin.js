$(document).ready(function(){

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
	
	//登录btn
  $('.p-login').click(function(){
      $('.error-wrap').show();
			$('.passwrod-login .name').addClass('error-box');
      $('.passwrod-login .pwd').addClass('error-box');
			
	})
	$('.s-login').click(function(){
			$('.error-wrap').show();
			$('.sms-login .phone').addClass('error-box');
      $('.sms-login .validate').addClass('error-box');
	})

	//input获取焦点
  $('input').focus(function(){
    $('.error-wrap').hide();
    $('.login-wrap .i-box').removeClass('error-box');
	})

	$(".clearfix input").bind("input propertychange",function(event){
		if ($(this).val() != '') {
			$(this).prev().show();
			$(this).prev().prev().prev().hide();
		} else {
			$(this).prev().hide();
			$(this).prev().prev().prev().show();
		}
	});

	//免密
  $('.toggle').click(function(even){
			$('.error-wrap').hide();
      if ($('.pwd input').attr('type') == 'password'){
        $('.pwd input').attr('type','text');
        $('.icon3').show();
        $('.icon4').hide();
      } else {
        $('.pwd input').attr('type','password');
        $('.icon4').show();
        $('.icon3').hide();
      }
	})
	
	//tab切换
  $('.tab-title span').click(function(){
		$('.error-wrap').hide();
		$('.login-wrap .i-box').removeClass('error-box');
		$(this).addClass('this').siblings().removeClass('this');
		if ($(this).text() == '短信登录') {
			$('.sms-login').show();
			$('.passwrod-login').hide();
		} else {
			$('.passwrod-login').show();
			$('.sms-login').hide();
		}
	})
	
	//获取验证码倒计时
	var num = 60;
	$('.getcode').click(function(){
		var _this = $(this);
		$('.countdown').find('span').text(num);
		var timer = setInterval(function(){
			if(num > 0) {
				$('.countdown').find('span').text(num--);
				_this.hide();
				$('.countdown').show();
			} else {
				clearInterval(timer);
				num = 60;
				_this.show();
				$('.countdown').hide();
			}
		}, 1000)
	})

	//滑动验证码 geetest网站:https://docs.geetest.com/install/deploy/server/python
	var handlerEmbed = function (captchaObj) {
		$("#embed-submit").click(function (e) {
				var validate = captchaObj.getValidate();
				if (!validate) {
					$("#notice")[0].className = "show";
					setTimeout(function () {
							$("#notice")[0].className = "hide";
					}, 2000);
					e.preventDefault();
				}
		});
		// 将验证码加到id为captcha的元素里，同时会有三个input的值：geetest_challenge, geetest_validate, geetest_seccode
		captchaObj.appendTo("#embed-captcha");
		captchaObj.onReady(function () {
				$("#wait")[0].className = "hide";
		});
		// 更多接口参考：http://www.geetest.com/install/sections/idx-client-sdk.html
	};
	$.ajax({
			// 获取id，challenge，success（是否启用failback）
			url: "/pc-geetest/register?t=" + (new Date()).getTime(), // 加随机数防止缓存
			type: "get",
			dataType: "json",
			success: function (data) {
				// 使用initGeetest接口
				// 参数1：配置参数
				// 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
				initGeetest({
						gt: data.gt,
						challenge: data.challenge,
						product: "embed", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
						offline: !data.success, // 表示用户后台检测极验服务器是否宕机，一般不需要关注
						new_captcha:data.new_captcha,
						api_server:"api.geetest.com"  
						// 更多配置参数请参见：http://www.geetest.com/install/sections/idx-client-sdk.html#config
				}, handlerEmbed);
			}
	});
  
})