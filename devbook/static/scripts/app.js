console.log("hello");

$container = $('#news-container')


var url = 'https://newsapi.org/v2/everything?' +
          'q=Technology&' +
          'cuntry=us&' +
          'sortBy=popularity&' +
          'apiKey=f93e86b1d7ef410dbdb022bca584cb9a';

const convertTime = (string) => {
  return string.substring(0,10)
}

var req = new Request(url);
fetch(req)
    .then(function(response) {
      return response.json()
    }).then(function(json) {
      console.log(json.articles);
      articles = json.articles
      for(let i = 0;i< 10;i++) {
        $container.append(`
          <div class="news">
          <img class="news-image" src="${articles[i]['urlToImage']}" alt="article picture" width="1000" height="1000"/>
          <a class="news" href="${articles[i]['url']}"><h1>${articles[i]['title']}</h1></a>
          <h2 class="author">${articles[i]['author']}</h2>
          <h5 class="news-time">${convertTime(articles[i]['publishedAt'])}</h5>
          <h3 class="article">${articles[i]['description']}</h3>
          </div>
          `
        )
      }
    })
