# 🏢 The Best Company — Team Showcase App

A Streamlit web app to showcase your company's team and allow visitors to contact you directly.

## Features

- 🏠 Home page with company overview, stats, and team profiles
- 📬 Contact form with topic selection and email delivery
- 🔒 Secure credential management via environment variables

## Project Structure

```
Applcation2/
├── HOME.py               # Main app entry point
├── pages/
│   └── contact us.py     # Contact form page
├── send_email.py         # Email utility
├── data.csv              # Team member data
├── topics.csv            # Contact form topics
├── images/               # Team member photos
├── .env.example          # Environment variable template
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Install dependencies
```bash
pip install streamlit pandas python-dotenv
```

### 3. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` and fill in your Gmail credentials:
```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
RECEIVER_EMAIL=receiver_email@gmail.com
```
> ⚠️ Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your regular password.

### 4. Run the app
```bash
streamlit run HOME.py
```

## Author

**Bheem Sagar** — IIIT Kalyani
