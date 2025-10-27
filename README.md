# AI Social Media Content Generator & Analyzer

An intelligent system to generate and analyze social media posts for **Instagram, LinkedIn, TikTok, And Facebook**. Built with **Django** and **n8n**, this project allows users to automatically create captions, hashtags, image prompts, and analyze post engagement.

---

## Features

* Auto-generate creative captions and descriptions based on user input.
* Generate trending and relevant hashtags.
* Provide image design prompts (compatible with Canva or MidJourney).
* Analyze post engagement (scored from 1 to 100).
* User authentication and profile management with Django.
* Store projects and track user history.

---

## Project Structure

```
project_root/
│
├─ accounts/               # User management app
│  ├─ templates            # PostIdea, Hashtag, AnalysisResult models
│  ├─ models.py            # CustomUser model
│  ├─ forms.py              # Registration and profile forms
│  └─ views.py             # Views for user management
│
├─ contentai/                   # Main app
│  ├─ templates            # PostIdea, Hashtag, AnalysisResult models
│  ├─ models.py            # PostIdea, Hashtag, AnalysisResult models
│  ├─ views.py             # Views for content generation and analysis
│
├─ static/                 # CSS, JS, and images
├─ n8n-workflow/           # n8n workflow files for AI Agent
├─ manage.py
└─ requirements.txt
```

---

## Installation

### Prerequisites

* Python 3.10
* Django 5.2
* MySQL
* Node.js and npm (for n8n, if running locally)

### Local Setup

```bash
git clone https://github.com/Esmat434/CaptivAI.git
cd CaptivAI
```

### Database Configuration

Edit `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or mysql
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'db',
        'PORT': '3306',
    }
}
```

```bash
docker-compose build
docker-compose up -d
```

### Run Server

Access the app: `http://127.0.0.1:8080`

---

## Connecting n8n AI Agent

1. Install or deploy n8n (locally or on a server/Render).
2. Import the `n8n` workflow files.
3. Set webhook URLs in Django `dashboard.html` template in contentai app.

---

## Example Usage

1. User enters a topic: `"Digital Marketing"`.
2. Output:

* **Caption:** `"How to double your sales with digital marketing strategies?"`
* **Hashtags:** `#Marketing #Digital #SocialMedia`
* **Image Prompt:** `"Person with laptop and growth chart in a modern background"`
* **Engagement Score:** `87/100`

---

## Future Enhancements

* Auto-posting to Instagram and LinkedIn
* Trending hashtag analysis via web scraping
* Scheduled posting with cron jobs
* SaaS version with monthly subscriptions

---

## License

MIT License © 2025
