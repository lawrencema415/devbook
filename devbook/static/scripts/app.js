console.log("hello");

$container = $('#news-container')


var url = 'https://newsapi.org/v2/everything?' +
          'q=Technology&' +
          'cuntry=us&' +
          'sortBy=popularity&' +
          'apiKey=f93e86b1d7ef410dbdb022bca584cb9a';

var req = new Request(url);
fetch(req)
    .then(function(response) {
      return response.json()
    }).then(function(json) {
      console.log(json.articles);
      articles = json.articles
      for(let i = 0;i< 10;i++) {
        $container.append(`
          <img src="${articles[i]['urlToImage']}" alt="article picture"/>
          <a href="${articles[i]['url']}"><h1>${articles[i]['title']}</h1></a>
          <h3>${articles[i]['description']}</h3>
          `
        )
      }
    })
