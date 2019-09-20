$(document).ready(function(){

    $('.menu-title .right').click(function(){
        $(this).find('ul').slideToggle(150);
    })

    $('.right ul li').click(function(){
        $(this).parent().prev().find('span').text($(this).text());
    })
    
    var i = 5;
    $('section').bind('mouseover',function(){
        $(this).find('.cover').css({'transform':"rotateY("+180+"deg"+")"})
        $(this).find('.route-item').css('transform', "rotateY("+0+"deg"+")")
        $(this).click(function(){
            i = $(this).index();
            $(this).addClass('bor').siblings().removeClass('bor');
            $(this).siblings().find('.route-item').css({'transform':"rotateY("+-180+"deg"+")"})
            $(this).siblings().find('.cover').css('transform', "rotateY("+0+"deg"+")")
        })
    })

    $('section').bind('mouseleave',function(){
        if ($(this).index() == i) {
            $(this).find('.cover').css({'transform':"rotateY("+180+"deg"+")"})
            $(this).find('.route-item').css('transform', "rotateY("+0+"deg"+")")
        } else {
            $(this).find('.route-item').css({'transform':"rotateY("+-180+"deg"+")"})
            $(this).find('.cover').css('transform', "rotateY("+0+"deg"+")")
        }
    })
    
    //创建和初始化地图函数：
    function initMap(){
        createMap();//创建地图
        setMapEvent();//设置地图事件
        addMapControl();//向地图添加控件
    }
    
    //创建地图函数：
    function createMap(){
        var map = new BMap.Map("dituContent");//在百度地图容器中创建一个地图
        var point = new BMap.Point(116.290933,40.152249);//定义一个中心点坐标
        map.centerAndZoom(point,17);//设定地图的中心点和坐标并将地图显示在地图容器中
        window.map = map;//将map变量存储在全局
    }
    
    //地图事件设置函数：
    function setMapEvent(){
        map.enableDragging();//启用地图拖拽事件，默认启用(可不写)
        map.enableScrollWheelZoom();//启用地图滚轮放大缩小
        map.enableDoubleClickZoom();//启用鼠标双击放大，默认启用(可不写)
        map.enableKeyboard();//启用键盘上下左右键移动地图
    }
    
    //地图控件添加函数：
    function addMapControl(){
        //向地图中添加缩放控件
	var ctrl_nav = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_ZOOM});
	map.addControl(ctrl_nav);
        //向地图中添加缩略图控件
	var ctrl_ove = new BMap.OverviewMapControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT,isOpen:0});
	map.addControl(ctrl_ove);
        //向地图中添加比例尺控件
	var ctrl_sca = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_LEFT});
	map.addControl(ctrl_sca);
    }
    
    
    initMap();//创建和初始化地图
    
})