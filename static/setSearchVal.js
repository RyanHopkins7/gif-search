// Sets text in search bar to search query from get request
searchBar = document.getElementById("search-bar");
searchQuery = window.location.search.substring(12)
searchBar.value = searchQuery.replace(/\+/g, " ")
