# Intro: What this project means to me.

I did this project as my very first datathon project in my first year and It served as a foundation for my start in development.

## Project Summary

- This is a Python Flask web application designed to process and record student transcripts.
- Users can upload a transcript (PDF or other supported file types) and then interactively record grades for several school years.
- The app tracks compulsory and optional subjects, organizes data by year, and stores session data on the filesystem.
- The UI uses Flask templates (found in the templates/ folder).
- Static files (like CSS) are in static/Styles.
- Uploaded transcripts are saved in the uploads/ folder.
- There’s custom logic for file extension extraction and session management.

## Main Features

- **Transcript Upload:** Users can upload a transcript document.
- **Grade Recording:** The app guides users through entering grades for various subjects by year, covering compulsory and elective subjects.
- **Session Management:** Uses Flask session to keep track of progress and data.
- **Simple Web UI:** All interaction is via a browser.
- **File Handling:** Cleans up old uploads before saving new ones.

## Technologies Used

- Python 3.x
- Flask
- flask-session

---


# datathonfinal

A Flask web application for uploading and recording school transcripts and grades across multiple academic years. This project demonstrates end-to-end handling of file uploads, session-based user flows, and data collection via a simple, interactive web interface.

## Features

- **Transcript Upload:** Upload a transcript file (PDF or supported formats).
- **Grade Entry:** Enter subject grades for each academic year, covering both compulsory and elective subjects.
- **Session Persistence:** Progress and data are stored securely through server-side sessions.
- **Clean File Handling:** Uploaded files are managed and cleaned up automatically.
- **Browser-based UI:** Easy to use, with clear prompts for each step.

## Technologies Used

- **Python 3**
- **Flask** (web framework)
- **flask-session** (session management)
- HTML templates (Jinja2), static CSS (in `static/Styles`)

## Project Structure

```
.
├── app.py                  # Main Flask application
├── templates/              # HTML templates
├── static/Styles/          # CSS and static assets
├── uploads/                # Uploaded transcript files
├── flask_session/          # Server-side session data
├── functions.py            # (Assumed) utility functions
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gitau189/datathonfinal.git
   cd datathonfinal
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask-session
   ```

### Running the Application

```bash
# Activate your virtual environment if not already active
flask run
```

- Open the generated URL in your browser.
- Follow on-screen instructions to upload a transcript and enter grades.

## Customization

- Modify `app.py` to change subjects or grading logic.
- Edit templates in the `templates/` directory for UI changes.

## License

This project is for educational and demonstration purposes.

---
