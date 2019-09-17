searchBar = document.getElementById("search-bar");

searchBar.onkeypress = function() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/", true);
    xhttp.send("val="+searchBar.value);
}

