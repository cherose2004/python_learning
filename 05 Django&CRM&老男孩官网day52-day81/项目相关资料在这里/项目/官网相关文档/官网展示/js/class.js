$(document).ready(function () {
    $('.navBox a').mouseover(function () {
        var x = $(".navBox a").index(this);
        $('.lineBox div').css('display', 'none').eq(x).css('display', 'block');
    });
    $('.navBox a').mouseout(function () {
        var x = $(".navBox a").index(this);
        $('.lineBox div').css('display', 'none');
    });

});
