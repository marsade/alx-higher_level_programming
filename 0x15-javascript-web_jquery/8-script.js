$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
  let movies = data.results;
  movies.forEach((movie) => {
    let title = movie.title
    let text = $('<li></li>').text(title);
    $('#list_movies').append(text);
  })
})
.fail(function(error) {
  console.error("Error fetching character data:", error);
});
