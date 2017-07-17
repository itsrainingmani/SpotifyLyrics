chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      // var firstHref = $("a[href^='http']").eq(0).attr("href");
      // var firstHref = $("div[class^='track-info__name']>div[class^=react-contextmenu-wrapper]+a[href^=/album]")
      var songName = $("#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__name > div > a").text()
      var songArtist = $("#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__artists > span > span > a").text()
      alert(songName)
      alert(songArtist)
    }
  }
);