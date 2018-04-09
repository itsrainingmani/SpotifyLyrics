chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    console.log(sender.tab ?
                "from a content script:" + sender.tab.url :
                "from the extension");
    if (request.greeting == "hello"){
    	var sname = document.querySelector('#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__name.ellipsis-one-line > div > a');
    	sname = sname.innerHTML;
    	var aname = document.querySelectorAll('#main > div > div.nowPlayingBar-container > footer > div > div.now-playing-bar__left > div > div > div.track-info__artists.ellipsis-one-line a');
    	// console.log(artistellipsis.innerHTML);
        var anameList = [];
        for (i = 0; i < aname.length; i++){
            anameList.push(aname[i].innerHTML);
        }
        sendResponse({songName: sname, artistName: anameList});
    }
  });