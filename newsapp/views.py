# importing API
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    # Initialize the News API client
    newsapi = NewsApiClient(api_key='2302cc6b36b94c9483e41b804815a0e5')

    # Fetch top headlines
    headlines = newsapi.get_top_headlines(sources='techcrunch,bbc-news,the-verge,google-news')

    # Fetch everything
    everything = newsapi.get_everything(sources='techcrunch,bbc-news,the-verge,google-news', sort_by='relevancy')

    # Extract data for headlines
    headline_articles = headlines.get('articles', [])
    headline_list = [
        {
            'author': article.get('author', 'Unknown'),
            'title': article.get('title', 'No Title'),
            'description': article.get('description', 'No Description'),
            'image': article.get('urlToImage', ''),
            'url': article.get('url', '#')
        }
        for article in headline_articles
    ]

    # Extract data for everything
    everything_articles = everything.get('articles', [])
    everything_list = [
        {
            'author': article.get('author', 'Unknown'),
            'title': article.get('title', 'No Title'),
            'description': article.get('description', 'No Description'),
            'image': article.get('urlToImage', ''),
            'url': article.get('url', '#')
        }
        for article in everything_articles
    ]

    # Render the context to the template
    return render(request, 'index.html', context={
        "headlines": headline_list,
        "everything": everything_list
    })
