// updates the text color of the  `<header>`  element when the user clicks on the tag  `DIV#red_header`
function changeColour() {
	$("header").css("color", "#FF0000");
}
$("DIV#red_header").click(changeColour);

