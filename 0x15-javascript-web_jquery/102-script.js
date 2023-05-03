// fetches and prints "hello" in a different language using an API service
$(document).ready(function() {

	const url = "https://hellosalut.stefanbohacek.dev/?lang=";
	$("input#btn_translate").click(function() {
		let lang = $("input#language_code").val();
		$.getJSON(url + lang, function(data) {
			$("DIV#hello").text(data["hello"])
		});

	});
});
