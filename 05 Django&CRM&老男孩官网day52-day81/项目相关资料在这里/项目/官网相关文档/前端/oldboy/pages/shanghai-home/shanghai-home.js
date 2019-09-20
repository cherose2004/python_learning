
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
	var shanghaiBanner = new Swiper('#shanghaiSwiper', {
		loop: true,
		speed: 800,
		effect: 'fade',
		autoplay: 5000,
		spaceBetween: 30,
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
		pagination: '#shanghaiPagination',
	});

	$("#shanghaiSwiper .swiper-pagination-bullet").hover(function() {
		$(this).click();
	},function() {
		shanghaiBanner.autoplay.start();
	})

	$('.content-right li').hover(function(){
		$('.content-left section').eq($(this).index()).show().siblings().hide();
		$(this).addClass('this').siblings().removeClass('this');
		if($(this).index() == 0 || $(this).index() == 1 || $(this).index() == 2) {
			$(this).addClass('aftertop').siblings().removeClass('aftertop');
			$(this).siblings().removeClass('afterbottom');
		} else {
			$(this).addClass('afterbottom').siblings().removeClass('afterbottom');
			$(this).siblings().removeClass('aftertop');
		}
	})

	var shanghaiswiper = new Swiper('#shanghai2Container', {
		// loop: true,
		speed: 800,
		autoplay: 5000,
		slidesPerView: 3,
		spaceBetween: 25,
		slidesPerGroup: 3,
		loopFillGroupWithBlank: true,
		paginationClickable: true,
		autoplayDisableOnInteraction: false,
		pagination: '#shanghai2Pagination',
	});

	$("#shanghai2Container .swiper-pagination-bullet").hover(function() {
		$(this).click();
	},function() {
		shanghaiswiper.autoplay.start();
	})

	var teacherswiper = new Swiper('#teacherContainer', {
		slidesPerView: 4,
		spaceBetween: 20,
		nextButton: '#teacherPrev',
		prevButton: '#teacherNext',
	  });

	  //创建和初始化地图函数：
	  function initMap(){
		createMap();//创建地图
		setMapEvent();//设置地图事件
		addMapControl();//向地图添加控件
		addMapOverlay();//向地图添加覆盖物
	  }
	  function createMap(){ 
		map = new BMap.Map("map"); 
		map.centerAndZoom(new BMap.Point(121.619376,31.040516),15);
	  }
	  function setMapEvent(){
		map.enableScrollWheelZoom();
		map.enableKeyboard();
		map.enableDragging();
		map.enableDoubleClickZoom()
	  }
	  function addClickHandler(target,window){
		target.addEventListener("click",function(){
		  target.openInfoWindow(window);
		});
	  }
	  function addMapOverlay(){
	  }
	  //向地图添加控件
	  function addMapControl(){
		var scaleControl = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_LEFT});
		scaleControl.setUnit(BMAP_UNIT_IMPERIAL);
		map.addControl(scaleControl);
		var navControl = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_LARGE});
		map.addControl(navControl);
		var overviewControl = new BMap.OverviewMapControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT,isOpen:true});
		map.addControl(overviewControl);
	  }
	  var map;
		initMap();
})


