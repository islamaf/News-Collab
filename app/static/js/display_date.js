// Array of day names
var dayNames = new Array("Sunday","Monday","Tuesday","Wednesday",
				"Thursday","Friday","Saturday");

// Array of month Names
var monthNames = new Array(
"January","February","March","April","May","June","July",
"August","September","October","November","December");

var now = new Date();
var today = dayNames[now.getDay()] + ", " +
monthNames[now.getMonth()] + " " +
now.getDate() + ", " + now.getFullYear();

document.getElementById('date_time').innerHTML = today;
