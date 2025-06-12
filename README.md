# 🫖 ChaiOrDjango

A full-featured Django-powered tweet-style app with Tailwind CSS, search functionality, user authentication, and glowing UI design. Built for learning, experimenting, and shipping real web projects.

---

## 🚀 Features

- 🧵 Tweet-style content system with descriptions
- 🔐 User signup, login, logout
- 🔍 Search tweets by description
- 🎨 Tailwind CSS dark UI with glowing aesthetic
- 🔄 Live reload with `django-browser-reload`

---


## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ChaiOrDjango.git
cd ChaiOrDjango

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate    # On Windows use: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the server
python manage.py runserver
```
---
📝 Usage
Access the app at: http://localhost:8000/

Log in or sign up to create tweets

Use the search bar to find tweets by their description

Use the navbar to navigate between Tweet, Search, Profile (coming soon)

---
🧪 Example Search
Try accessing:
```bash
http://localhost:8000/search/?q=hello
```
You'll get all tweets containing "hello" in the description.
---
🛠 Tech Stack
Backend: Django 5.2

Frontend: Tailwind CSS

Database: SQLite (default)

Styling & Reload: Tailwind + django-browser-reload
---

📦 Dependencies

pip install -r requirements.txt

To generate your own:

pip freeze > requirements.txt


🙌 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

📜 License
MIT — free to use, improve, remix.

🔥 Author
Made with 💻 & ☕ by @moksh-codedeveloper
