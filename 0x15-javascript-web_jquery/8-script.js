// fetches and lists the title for all movies from a URL
const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.getJSON(url, function(data) {
	const results = data["results"];
	results.forEach((result) => {
		$("UL#list_movies").append("<li>"+result['title']+"</li>");
	});
});
