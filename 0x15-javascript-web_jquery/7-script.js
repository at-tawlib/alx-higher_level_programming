// fetches the character name from a URL
const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
$.getJSON(url).done(function (data) {
	$("DIV#character").text(data["name"]);
});
