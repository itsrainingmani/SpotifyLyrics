window.onload = function(){
	document.getElementById('checkSpot').onclick = function fun() {
		chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
			chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response){
				// alert(response.songName);
				var songfield = document.getElementById('songName');
				var artistField = document.getElementById('artistName');
				songfield.textContent = response.songName;
				artistField.textContent = "".concat(...response.artistName);
			});
		});
	}
}