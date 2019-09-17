searchBar = document.getElementById("search-bar");

searchBar.onkeyup = function() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("user="+searchBar.value);
}

