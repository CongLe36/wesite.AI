# Document Management System

This project is a Document Management System built using Django for the backend and FastAPI for AI-assisted features. It provides functionalities for managing outgoing and incoming documents, AI-assisted note-taking, and automatic metadata extraction from text and images.

## Features

- **Document Management**: Store and manage both outgoing and incoming documents efficiently.
- **AI-Assisted Note-Taking**: Utilize AI to assist in creating notes from documents, summarizing content, and extracting important information.
- **Automatic Metadata Extraction**: Automatically extract metadata from both text documents and images to facilitate better organization and retrieval.

## Project Structure

```
document-management-system
├── backend
│   ├── django_app
│   │   ├── documents
│   │   │   ├── migrations
│   │   │   ├── templates
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── django_app
│   │   │   ├── __init__.py
│   │   │   ├── asgi.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── manage.py
│   │   └── requirements.txt
│   ├── fastapi_app
│   │   ├── ai
│   │   │   ├── __init__.py
│   │   │   ├── metadata_extraction.py
│   │   │   └── note_taking.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── requirements.txt
├── frontend
│   ├── public
│   │   ├── css
│   │   ├── js
│   │   └── index.html
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── webpack.config.js
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd document-management-system
   ```

2. Set up the backend:
   - Navigate to the `backend/django_app` directory.
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```
   - Run migrations:
     ```
     python manage.py migrate
     ```
   - Start the Django server:
     ```
     python manage.py runserver
     ```

3. Set up the FastAPI application:
   - Navigate to the `backend/fastapi_app` directory.
   - Install the required packages:
     ```
     pip install -r requirements.txt
     ```
   - Start the FastAPI server:
     ```
     uvicorn main:app --reload
     ```

4. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required packages:
     ```
     npm install
     ```
   - Start the frontend application:
     ```
     npm start
     ```

## Usage

- Access the Django admin panel to manage documents at `http://127.0.0.1:8000/admin`.
- Use the FastAPI endpoints for AI-assisted features.
- Interact with the frontend application to manage documents and utilize AI features.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.