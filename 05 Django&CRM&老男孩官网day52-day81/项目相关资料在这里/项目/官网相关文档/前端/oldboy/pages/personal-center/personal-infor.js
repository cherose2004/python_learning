$(document).ready(function(){

    $('.signin-btn').hide();
    
    $('#changeData').click(function(){
        $(this).hide();
        $('#complete').show();
        $('.data-infor input').addClass('editor').removeAttr('disabled'); 
    })

    $('#complete').click(function(){
        $(this).hide();
        $('#changeData').show();
        $('.data-infor input').removeClass('editor').attr("disabled", true);
    })

    $('#changeBinding').click(function(){
        $('#changeWrap').show();
        $('#step1').show();
        $('#step2').hide();
        $('#step3').hide();
    })

    $('.changeClose').click(function(){
        $('#changeWrap').hide();
    })

    $('#nextStep1').click(function(){
        $('#step1').hide();
        $('#step2').show();
    })
    $('#nextStep2').click(function () {
        $('#step2').hide();
        $('#step3').show();
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
    
    var num2 = 60;
	$('#getCode2').click(function(){
        var _this = $(this);
		$(this).text(num2+'s');
		var timer = setInterval(function(){
			if(num2 > 0) {
                num2--;
                _this.text(num2+'s');
                _this.attr('disabled', true);
			} else {
				clearInterval(timer);
				num2 = 60;
                _this.text('获取验证码');
                _this.reomveAttr('disabled');
			}
		}, 1000)
	})
})  