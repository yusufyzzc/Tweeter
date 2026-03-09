# Tweeter

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-4.2-green?logo=django&logoColor=white)
![Deployed on Railway](https://img.shields.io/badge/deployed%20on-Railway-blueviolet?logo=railway&logoColor=white)
![License](https://img.shields.io/badge/license-open%20source-lightgrey)

A lightweight Twitter-style microblogging web application built with Django. Users can post short messages (tweets), browse a public feed, like/unlike posts and manage their accounts through a full authentication system.



## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [License](#license)



## Features

- **Tweet Feed** -- Browse all tweets in reverse chronological order.
- **Post Tweets** -- Authenticated users can create tweets with a nickname and up to 280 characters of content.
- **Like / Unlike** -- Toggle likes on tweets. Each user can only like a tweet once (enforced at the database level via a unique constraint).
- **User Authentication** -- Sign up, log in, and log out using Django's built-in auth system.
- **Responsive UI** -- Built with Bootstrap 5 and custom CSS for a clean, mobile-friendly experience.



## Tech Stack

| Layer        | Technology                      |
| ------------ | ------------------------------- |
| Backend      | Python 3.11, Django 4.2         |
| Database     | SQLite (default, dev)           |
| Frontend     | Django Templates, Bootstrap 5   |
| Static Files | WhiteNoise                      |
| Deployment   | Gunicorn, Railway               |
| Config       | python-decouple                 |



## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yusufyzzc/Tweeter.git
   cd Tweeter
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```



## Environment Variables

The project uses `python-decouple` to manage configuration. Create a `.env` file in the project root with the following variables:

| Variable     | Description                        | Default                          |
| ------------ | ---------------------------------- | -------------------------------- |
| `SECRET_KEY` | Django secret key                  | Auto-generated insecure default  |
| `DEBUG`      | Enable/disable debug mode          | `False`                          |

Example `.env`:

```
SECRET_KEY=your-production-secret-key
DEBUG=True
```



## Deployment

The project is configured for deployment on Railway (or any platform that supports Gunicorn + Procfile workflows).

Key deployment details:

- **Procfile** declares the web process: `web: gunicorn djangotweet.wsgi --log-file -`
- **runtime.txt** pins the Python version to `3.11.7`.
- **WhiteNoise** serves static files in production without a separate web server.
- **Allowed Hosts** include `*.up.railway.app` by default. Update `settings.py` to add your own domain.



## License

This project is open source and available for educational purposes.
