# Django News App

This is a **Django News App** that pulls the latest news from various sources using the NewsAPI and displays the headlines and full articles on the website. The app includes a clean and responsive design using Bootstrap, with features like viewing headlines, reading full articles, and navigating through different categories of news.

## Features

- Fetches the latest news from multiple sources such as TechCrunch, BBC News, The Verge, and Google News.
- Displays top headlines with images and descriptions.
- Allows users to click on a headline to read the full article.
- Sections for viewing both headlines and all articles.
- A navbar to navigate between the headlines and all articles sections.

## Technologies Used

- **Django**: Web framework used for backend development.
- **NewsAPI**: API used to fetch the latest news from different sources.
- **Bootstrap 4**: Front-end framework for responsive design and layout.
- **HTML5**: Markup language for structuring the content.
- **CSS**: Styling and layout customization.

## Installation

Follow these steps to get your local copy of the project up and running:

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/Manju-Shree-Yadav/Django-news-app.git
```
### 2. Navigate to the Project Directory
Change into the project directory:
```bash
cd Django-news-app
```

### 3. Set Up a Virtual Environment
It's a good practice to set up a virtual environment to isolate your project dependencies. Use the following commands:

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Set Up Your NewsAPI Key
Visit NewsAPI to get an API key.
Once you have the API key, open the views.py file and replace the placeholder YOUR_API_KEY_HERE with your actual API key:
```bash
newsapi = NewsApiClient(api_key='YOUR_API_KEY_HERE')
```
