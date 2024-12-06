# Blogify

**Blogify** is a simple and customizable blogging platform built with Django. It allows users to create, edit, and manage blog posts, organize them into categories, and interact with readers through comments.

## Features
- Create, edit, and publish blog posts.
- Organize posts into categories.
- User authentication for posting comments.
- Admin panel for managing posts and categories.
- Comment system for readers to interact with posts.
- Responsive design for a seamless experience on mobile and desktop.

## Installation

Follow these steps to get the project up and running:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/blogify.git
```
### 2. Install dependencies
```bash
cd blogify
pip install -r requirements.txt
```

###3. Set up the database
```bash
python manage.py migrate
```

### 4. Create a superuser to access the admin panel
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Open your browser and go to:
```bash
http://127.0.0.1:8000
```






