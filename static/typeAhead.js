searchBar = document.getElementById("search-bar");
gifWrapper = document.getElementById("gif-wrapper")

searchBar.onkeyup = function() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/typeahead", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4) {
            console.log(xhttp.responseText)
            gifWrapper.innerHTML = xhttp.responseText
        }
    }
    xhttp.send("user_input="+searchBar.value);
}

