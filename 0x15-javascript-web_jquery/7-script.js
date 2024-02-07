$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
  // Extract the character name from the response data
  var characterName = data.name;
  $("#character").text(characterName);
})
.fail(function(error) {
  console.error("Error fetching character data:", error);
});
