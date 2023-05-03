// toggles the class of the  `<header>`  element when the user clicks on the tag  `DIV#toggle_header`
$("DIV#toggle_header").click(function() {
	const headerClass = $("header").attr("class");
	if (headerClass == "red") {
		$("header").addClass("green");
		$("header").removeClass("red");
	} else {
		$("header").addClass("red");
		$("header").removeClass("green");
	}
});
