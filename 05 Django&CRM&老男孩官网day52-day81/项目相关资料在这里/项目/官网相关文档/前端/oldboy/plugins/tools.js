
// 创建阿里点播播放器
var createAliPlayer = function (ele, isPlay, source) {
  if (window.AliPlayer && window.AliPlayer._options.id === ele){
    window.AliPlayer.dispose();
  }
  window.AliPlayer = new Aliplayer({
    "id": ele,
    "source": source,
    "width": "100%",
    "height": "100%",
    "autoplay": isPlay,
    "isLive": false,
    "rePlay": false,
    "playsinline": true,
    "preload": true,
    "controlBarVisibility": "hover",
    "useH5Prism": true
  });
};
