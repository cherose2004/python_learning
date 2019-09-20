$(document).ready(function(){
  $('.directory-list li').click(function(){
    $(this).addClass('lookthis').siblings().removeClass('lookthis');
  })
})