// adds a class  to the  `<header>`  element when the user clicks on the tag  `DIV#red_header`
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
