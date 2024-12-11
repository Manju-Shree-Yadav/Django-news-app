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

### 5. Run the Django Development Server
Now, you are ready to run the Django development server. Run the following command:
```bash
python manage.py migrate
python manage.py runserver
```

## Project Structure
Here's an overview of the project folder structure:
```bash
Django-news-app/
│
├── newsapp/                     # Main app folder
│   ├── migrations/               # Database migrations
│   ├── templates/                # HTML files
│   │   └── index.html            # Main template file
│   ├── __init__.py               # Python package marker
│   ├── admin.py                  # Admin configurations
│   ├── apps.py                   # App configurations
│   ├── models.py                 # Database models
│   ├── tests.py                  # Unit tests
│   └── views.py                  # Main logic for handling requests
│
├── manage.py                     # Django management file
├── db.sqlite3                    # SQLite database file (used by default)
└── README.md                     # Project README
```

## OUTPUT:
![n1](https://github.com/user-attachments/assets/97e10fa6-8282-4670-96eb-7a5d9ed62626)
![n2](https://github.com/user-attachments/assets/0c42fffb-e365-4031-87fc-5996b7d39eb5)
