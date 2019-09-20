
$(document).ready(function(){
	//banner-nav
	$(".banner-itme .item-list li").bind("mouseover",function(){
		var _this = $(this);
		$(this).addClass('lithis').siblings().removeClass('lithis');
		$('.submenu-box').show().stop().animate({width: '460px'}, 300)
		$('.submenu-box').hover(function(){
				$(_this).addClass('lithis').siblings().removeClass('lithis');
				$(this).show().stop().animate({width: '460px'}, 300);
		},function(){
				$(_this).removeClass('lithis')
				$(this).stop().animate({width: '0px'}, 300);
		})
	})
	$(".banner-itme .item-list li").bind("mouseleave",function(){
		$(this).removeClass('lithis');
		$('.submenu-box').stop().animate({width: '0px'}, 300);
	})
	
	//banner轮播
	var beijinhomeBanner = new Swiper('#bannerSwiper', {
		loop: true,
		speed: 800,
		effect: 'fade',
		autoplay: 5000,
		spaceBetween: 30,
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
		pagination: '#bannerPagination',
		onAutoplay(swiper){
			$('.banner-bg img').eq(swiper.realIndex).stop().animate({
				opacity: 1
			}).siblings().stop().animate({
				opacity: 0
			});
		}
	});

	$("#bannerSwiper .swiper-pagination-bullet").hover(function() {
		$(this).click();
		$('.banner-bg img').eq($(this).index()).stop().animate({
			opacity: 1
		}).siblings().stop().animate({
			opacity: 0
		});
	},function() {
		beijinhomeBanner.autoplay.start();
	})
	
	//访谈轮播
	var interviewSwiper = new Swiper('#interviewSwiper', {
		loop: true,
		autoplay: 4000,
		direction: 'vertical',
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
		pagination: '#interviewPagination',
	});

	var intervieWrapper = document.getElementById('intervieWrapper');
	intervieWrapper.onmouseenter = function () {
		interviewSwiper.stopAutoplay();
	};
	intervieWrapper.onmouseleave = function () {
		interviewSwiper.startAutoplay();
	}

	//鼠标划入触发点击事件
	setTimeout(function(){
		$(".oldboy-interview .swiper-pagination-bullet").hover(function() {
			$(this).click();
		},function() {
			interviewSwiper.autoplay.start();
		})
	},100)

	setTimeout(function(){
		$('<i></i>').prependTo(".oldboy-interview .swiper-pagination-bullet");
		$('.oldboy-interview .swiper-pagination-bullet').eq(0).css('background-image', 'url(../../images/home/banner1.jpg)');
		$('.oldboy-interview .swiper-pagination-bullet').eq(1).css('background-image', 'url(../../images/home/banner2.png)');
		$('.oldboy-interview .swiper-pagination-bullet').eq(2).css('background-image', 'url(../../images/home/banner1.jpg)');
		$('.oldboy-interview .swiper-pagination-bullet').eq(3).css('background-image', 'url(../../images/home/banner2.png)');
	},100)

	//查看更多
	$('.employment-more').click(function(){
		$('.employment-module').addClass('h');
		$(this).hide();
	})

	$('.weekend-more').click(function(){
		$('.weekend-module').addClass('h');
		$(this).hide();
	})

	//师资力量
	var index = 0;
	function teacherToggle () {
		index++;
		if (index > 17) index = 0;
		$('.shallow').find('span').show();
		$('.deep').find('span').show();
		$('.faculty-list li').eq(index).addClass('this').siblings().removeClass('this');
		$('.this').find('span').hide().siblings().find('span').show();
		$('.faculty-item li').eq(index).show().siblings().hide();
	}
	var start = setInterval(teacherToggle, 3000)
	$('.faculty-list li').hover(function(){
		$('.shallow').find('span').show();
		$('.deep').find('span').show();
		$(this).addClass('this').siblings().removeClass('this');
		$('.this').find('span').hide().siblings().find('span').show();
		$('.faculty-item li').eq($(this).index()).show().siblings().hide();
		clearInterval(start);
		index = $(this).index();
	}, function(){
		start = setInterval(teacherToggle, 3000);
	})

	//书籍
	$('.all-books .books1').hover(function(){
		$(this).stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '250px'})
		$('.books3').stop().animate({left: '340px'})
		$('.books4').stop().animate({left: '450px'})
		$('.books5').stop().animate({left: '560px'})
		$('.books6').stop().animate({left: '670px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})
	$('.all-books .books2').hover(function(){
		$(this).stop().animate({left: '140px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books3').stop().animate({left: '340px'})
		$('.books4').stop().animate({left: '450px'})
		$('.books5').stop().animate({left: '560px'})
		$('.books6').stop().animate({left: '670px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '190px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})
	$('.all-books .books3').hover(function(){
		$(this).stop().animate({left: '240px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books4').stop().animate({left: '450px'})
		$('.books5').stop().animate({left: '560px'})
		$('.books6').stop().animate({left: '670px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '310px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})
	$('.all-books .books4').hover(function(){
		$(this).stop().animate({left: '340px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books5').stop().animate({left: '560px'})
		$('.books6').stop().animate({left: '670px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '420px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})

	$('.all-books .books5').hover(function(){
		$(this).stop().animate({left: '440px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books4').stop().animate({left: '340px'})
		$('.books6').stop().animate({left: '670px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '530px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})

	$('.all-books .books6').hover(function(){
		$(this).stop().animate({left: '570px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books4').stop().animate({left: '340px'})
		$('.books5').stop().animate({left: '440px'})
		$('.books7').stop().animate({left: '780px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '640px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})

	$('.all-books .books7').hover(function(){
		$(this).stop().animate({left: '680px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books4').stop().animate({left: '340px'})
		$('.books5').stop().animate({left: '440px'})
		$('.books6').stop().animate({left: '570px'})
		$('.books8').stop().animate({left: '890px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '750px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books8').stop().animate({left: '860px'})
		$('.books9').stop().animate({left: '970px'})
	})

	$('.all-books .books8').hover(function(){
		$(this).stop().animate({left: '790px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books4').stop().animate({left: '340px'})
		$('.books5').stop().animate({left: '440px'})
		$('.books6').stop().animate({left: '570px'})
		$('.books7').stop().animate({left: '680px'})
		$('.books9').stop().animate({left: '1000px'})
	},function(){
		$(this).stop().animate({left: '860px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books9').stop().animate({left: '970px'})
	})
	
	$('.all-books .books9').hover(function(){
		$(this).stop().animate({left: '1000px'})
		$('.books1').stop().animate({left: '40px'})
		$('.books2').stop().animate({left: '140px'})
		$('.books3').stop().animate({left: '240px'})
		$('.books4').stop().animate({left: '340px'})
		$('.books5').stop().animate({left: '440px'})
		$('.books6').stop().animate({left: '570px'})
		$('.books7').stop().animate({left: '680px'})
		$('.books8').stop().animate({left: '790px'})
	},function(){
		$(this).stop().animate({left: '970px'})
		$('.books1').stop().animate({left: '80px'})
		$('.books2').stop().animate({left: '190px'})
		$('.books3').stop().animate({left: '310px'})
		$('.books4').stop().animate({left: '420px'})
		$('.books5').stop().animate({left: '530px'})
		$('.books6').stop().animate({left: '640px'})
		$('.books7').stop().animate({left: '750px'})
		$('.books8').stop().animate({left: '860px'})
	})

	//校内活动
	$('.campus-activitie .menu-title-right a').hover(function(){
		$(this).addClass('activity-a').siblings().removeClass('activity-a');
		$('.activitie-box section').eq($(this).index()).stop().animate({
			opacity: 1,
		}, 600).siblings().stop().animate({
			opacity: 0
		}, 600);
		$('.activitie-box section').eq($(this).index()).show().siblings().hide();
	})

	new Swiper('#cooperativeContainer', {
		loop: true,
		speed: 800,
		autoplay: 4000,
		direction: 'horizontal',
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
	});

	//环境
	$('.learning-environment .menu-title-right a').hover(function(){
		$(this).addClass('activity-a').siblings().removeClass('activity-a');
		$('.learning-box section').eq($(this).index()).stop().animate({
			opacity: 1,
		}, 600).siblings().stop().animate({
			opacity: 0
		}, 600);
		$('.learning-box section').eq($(this).index()).show().siblings().hide();
	})

	//全部校区
	$('.home-item').on('click','.campus-toggle',function(){
		$(this).find('ul').slideToggle(200);
	})

	$(".campus-toggle").on("click","li",function(){
		$(this).parent().parent().find('span').text($(this).text());
		$(this).parent().parent().find('ul').slideDown(200);
	});
	
	//访谈 视频切换
	$(".interview-content .swiper-slide").bind("mouseenter",function(){
		$(this).find('.swiper-img').hide();
		$(this).find('.home-video-box').show();
		$("HomeVideo"+$(this).index()).html('');
		var vid = [
			'http://mpv.cuplayer.net/e6f20bc588/b/e6f20bc588f22678ad02e81e25061eab_2.mp4',
			'http://mpv.cuplayer.net/e6f20bc588/d/e6f20bc5881055bf4230f9c99290017d_2.mp4',
			'http://mpv.cuplayer.net/e6f20bc588/3/e6f20bc5882e60a39da2e83735413db3_3.mp4',
			'http://mpv.cuplayer.net/e6f20bc588/e/e6f20bc588b96d30964e64f619aa66ee_2.mp4'
		]
		createAliPlayer("HomeVideo"+$(this).index(), true, vid[$(this).index()]);
	})

	$(".interview-content .swiper-slide").bind("mouseleave",function(){
		$(this).find('.swiper-img').show();
		$(this).find('.home-video-box').hide();
		$("HomeVideo"+$(this).index()).html('');
	})

})


