$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  movies.forEach((movie) => {
    const title = movie.title;
    const text = $('<li></li>').text(title);
    $('#list_movies').append(text);
  });
})
  .fail(function (error) {
    console.error('Error fetching character data:', error);
  });
