# Google Cloud Summit Website

This is a Flask-based website for a 1-day technical conference.

## Features
- Displays schedule with 8 technical talks.
- Search functionality by Title, Speaker, or Category.
- Responsive design with a modern, glassmorphism aesthetic.
- Includes dummy data for quick setup.

## Setup Instructions

1.  **Prerequisites**:
    - Python 3.x installed.
    - Flask installed (`pip install flask`).

2.  **Installation**:
    - Clone or download this repository.
    - Navigate to the project directory: `cd "Pagina Web"`

3.  **Run the Application**:
    -   **Option 1 (Recommended for Windows)**: Double-click `run_website.bat`.
    -   **Option 2 (Command Line)**:
        ```bash
        py app.py
        ```
        *(If `py` doesn't work, try `python app.py` or `python3 app.py`)*

4.  **Access the Website**:
    - Open your browser and go to `http://127.0.0.1:5000/`.

## Making Changes

-   **Data**: Edit `data.py` to modify talks, speakers, or event info.
-   **Styles**: Edit `static/css/style.css` for visual changes.
-   **Templates**: Edit `templates/index.html` for layout changes.

## License
MIT License
