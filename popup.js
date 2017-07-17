document.addEventListener('DOMContentLoaded', function(){
  var songName = $("#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__name > div > a").text();
  var songArtist = $("#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__artists > span > span > a").text();
  var p1 = document.getElementById("p1").innerHTML;
  var p2 = document.getElementById("p2").innerHTML;
  p1.innerHTML = songName;
  p2.innerHTML = songArtist;
  alert(document.getElementById("p1").innerHTML);
  // var spot = document.getElementById('checkSpot');
});