function switchVisible() {
  var trending = document.getElementById("trending");
  var article = document.getElementById("article");
  if (trending.style.display == 'block') {
      trending.style.display = 'none';
      article.style.display = 'block';
  }
  else {
      trending.style.display = 'block';
      article.style.display = 'none';
  }
}
