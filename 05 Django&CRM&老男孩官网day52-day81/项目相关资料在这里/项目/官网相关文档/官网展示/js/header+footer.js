$(document).ready(function () {
    $(window).scroll(function () {
        var h = $(this).scrollTop();
        console.log(h);

        if (h > 110) {
            $(".header-nav").addClass("fix")
            $(".header .fix .nav-left").children().css({
                display: 'none'
            })
            $(".header-nav .nav .nav-left").addClass("left-fix")
            $(".header-nav .nav .nav-right").addClass("right-fix")
            $(".header-nav .nav-left span.train").addClass("train1")
        } else {
            $(".header-nav").removeClass("fix")
            $(".header .nav-left").children().css({
                display: 'inline-block'
            })
            $(".header-nav .nav .nav-left").removeClass("left-fix")
            $(".header-nav .nav .nav-right").removeClass("right-fix")
            $(".header-nav .nav-left span.train").removeClass("train1")
        }

    })

})