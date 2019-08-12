console.log("hello");

$container = $('#news-container')


var url = 'https://newsapi.org/v2/top-headlines?' +
          'sources=bbc-news&' +
          'apiKey=f93e86b1d7ef410dbdb022bca584cb9a';
var req = new Request(url);
fetch(req)
    .then(function(response) {
        console.log(response.json());
    })
