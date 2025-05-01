# Face Recognition Django REST API

A robust backend system for facial recognition and attendance tracking, built with Django REST Framework and Face Recognition algorithms. This project enables real-time face detection, recognition, and attendance logging through RESTful API endpoints.

## 🔍 Features

- Facial detection using Facenet and recognition using DeepFace.
- RESTful API endpoints for seamless integration.
- Attendance tracking with timestamp logging.
- Modular and scalable architecture.
- Deployment-ready with AWS Elastic Beanstalk configurations.

## 📁 Project Structure


```bash
Face-Recognition-Django-REST-API/
├── api/                   # Core API logic
├── face/                  # Face recognition modules
├── face_attendance/       # Attendance tracking app
├── db_path/               # Database files
├── images/                # Sample images
├── .ebextensions/         # AWS Elastic Beanstalk configs
├── .github/workflows/     # GitHub Actions workflows
├── .vscode/               # VSCode settings
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── run.sh                 # Startup script
├── db.sqlite3             # SQLite database
├── backend_API.md         # API documentation
├── Face recognition part.txt  # Implementation notes
├── *.jpeg                 # Sample images
└── collage.jpg            # Image collage
```


## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lokie-codes/Face-Recognition-Django-REST-API.git
   cd Face-Recognition-Django-REST-API
   ```


2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```


5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```


   Access the API at `http://127.0.0.1:8000/`

## 📡 API Endpoints

The API endpoints are documented in detail in the [backend_API.md](backend_API.md) file. Below is a summary of the primary endpoints:

- **POST `/api/face-detect/`**: Detect faces in an uploaded image.
- **POST `/api/face-encode/`**: Generate and store facial encodings.
- **POST `/api/face-recognize/`**: Recognize faces in an uploaded image.
- **GET `/api/attendance/`**: Retrieve attendance records.
- **POST `/api/attendance/`**: Log attendance for recognized individuals.
  
Each endpoint expects specific parameters and returns JSON responses. Refer to the [backend_API.md](backend_API.md) for request and response examples.

## 🖼️ Sample Images

The `images/` directory contains sample images used for testing the face recognition functionalities.

## 🛠️ Deployment

This project includes configurations for deploying to AWS Elastic Beanstalk:

- `.ebextensions/` directory contains environment configurations.
- `run.sh` script is used to start the application on the server.

To deploy: 

1. Install the [AWS Elastic Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html).

2. Initialize your EB application:

   ```bash
   eb init -p python-3.7 face-recognition-api
   ```


3. Create an environment and deploy:
   
   ```bash
   eb create face-recognition-env
   eb deploy
   ```


## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For any inquiries or support, please contact [lokesh.sinduluri@gmail.com](mailto:lokesh.sinduluri@gmail.com).
