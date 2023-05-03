// fetches and prints "hello" in a different language using an API service
$(document).ready(function() {

	$("input#btn_translate").click(function() {
		translation();
	});

	$("input#language_code").focus(function(){
		$(this).keydown(function(enter) {
			if (enter.keycode === 13) {
				translation();
			};
		});
	});
});


function translation() {
	const url = "https://hellosalut.stefanbohacek.dev/?lang=";
	let lang = $("input#language_code").val();
	$.getJSON(url + lang, function(data) {
		$("DIV#hello").text(data["hello"])
	});
}
