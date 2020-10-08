// document.getElementById('click-like-btn').onclick = function(){
//   var like = document.getElementById("click-like-btn");
//   var dislike = document.getElementById("click-dislike-btn");
//
//   like.style.backgroundColor = "blue";
//   dislike.style.backgroundColor = "rgba(255,138,128 ,0.3)";
// }

$('.like').click(function() {
  $(this).toggleClass("likeActive");
  // $('.dislike').css("background-color", "white");
});

$('.dislike').click(function() {
  $(this).toggleClass("dislikeActive")
  // $('.like').css("background-color", "black");
});


//
// document.getElementById('click-dislike-btn').onclick = function(){
//   var like = document.getElementById("click-like-btn");
//   var dislike = document.getElementById("click-dislike-btn");
//
//   like.style.backgroundColor = "rgba(38,166,154 ,0.3)";
//   dislike.style.backgroundColor = "red";
// }
