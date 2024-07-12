# News Portal Project

## Description
This project is a News Portal developed using Django. It allows users to search by tags and categories, add articles, comment, edit, delete, sort by popularity/views, like articles, and more. Users can also add, edit, delete, and see details of blogs. Admin users can perform CRUD operations on articles and manage user comments.

### Features:
- Search by tags and categories
- Add, edit, and delete articles
- Comment on articles
- Sort articles by popularity/views
- Like articles
- Add, edit, delete, and view details of blogs

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SaugatMgr/News-Portal-Project.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd News-Portal-Project
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start using the News Portal:

1. **Create a superuser:**
    - Run the following command and follow the prompts:
        ```bash
        python manage.py createsuperuser
        ```
    - Alternatively, you can sign up and log in from the home page.

2. **Run the server:**
    ```bash
    python manage.py runserver
    ```

3. **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:8000/`.

4. **Admin Panel:**
    - Access the admin panel at `http://127.0.0.1:8000/admin/` to manage articles and comments.
