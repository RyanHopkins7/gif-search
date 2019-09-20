searchBar = document.getElementById("search-bar");
gifWrapper = document.getElementById("gif-wrapper");

// As user types, send POST requests to /typeahead route with search query as body

let sendRequest = true;

searchBar.onkeyup = function () {
    // Only send requests every 300 ms rather than every keystroke
    if (sendRequest) {
        sendRequest = false;
        setTimeout(function () {
            sendRequest = true;

            let xhttp = new XMLHttpRequest();
            xhttp.open("POST", "/typeahead", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
            // When client receives gifs from server, display them
            xhttp.onreadystatechange = function () {
                if (xhttp.readyState == 4) {
                    gifWrapper.innerHTML = xhttp.responseText;
                }
            }
    
            xhttp.send("user_input=" + searchBar.value);
        }, 300);
    }    
}

