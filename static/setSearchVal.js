// Sets text in search bar to search query from get request
searchBar = document.getElementById("search-bar");
if (window.location.search.includes("user_input")) {
    searchQuery = window.location.search.substring(12);
    searchBar.value = searchQuery.replace(/\+/g, " ");
}
