searchBar = document.getElementById("search-bar");
gifWrapper = document.getElementById("gif-wrapper")

// As user types, send POST requests to /typeahead route with search query as body
searchBar.onkeyup = function() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/typeahead", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    // When client receives gifs from server, display them
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4) {
            gifWrapper.innerHTML = xhttp.responseText
        }
    }

    xhttp.send("user_input="+searchBar.value);
}

