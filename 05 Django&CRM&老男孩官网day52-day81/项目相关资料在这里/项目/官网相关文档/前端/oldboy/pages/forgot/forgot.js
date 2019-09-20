$(document).ready(function () {
    
    //logo切换
	$('.logo').hover(function(){
        $('.nav-logo .logo .logo-img1').animate({marginLeft: '-165px'});
    },function(){
        $('.nav-logo .logo .logo-img1').animate({marginLeft: '0'});
    });

    $('#nextStep1').click(function () {
        $('#step1').hide();
        $('#step2').show();
        $('.process li').eq(1).addClass('this').siblings().removeClass('this');
    })
    $('#nextStep2').click(function () {
        $('#step2').hide();
        $('#step3').show();
        $('.process li').eq(2).addClass('this').siblings().removeClass('this');
    })

    var num = 60;
	$('#getCode1').click(function(){
        var _this = $(this);
		$(this).text(num+'s');
		var timer = setInterval(function(){
			if(num > 0) {
                num--;
                _this.text(num+'s');
                _this.attr('disabled', true);
			} else {
				clearInterval(timer);
				num = 60;
                _this.text('获取验证码');
                _this.reomveAttr('disabled');
			}
		}, 1000)
    })

})  