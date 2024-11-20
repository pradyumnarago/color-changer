# Color Changer 🎨

A simple web application that allows users to change the background color of a webpage and logs the colors in a backend system.

---

## Features

- **Frontend**: Built with React.js to provide an interactive user interface.
- **Backend**: Developed using Flask for managing color logs.
- **Data Storage**: Colors are saved to a JSON file (`colors.json`).
- **Live Preview**: Changes the background color instantly based on user input.
- **Persistence**: Maintains a log of all submitted colors.

---

## Project Structure

```plaintext
color-changer/
├── frontend/       # React.js frontend
│   ├── src/        # React components
│   ├── public/     # Static assets
│   └── package.json # Frontend dependencies
├── backend/        # Flask backend
│   ├── app.py      # Backend logic
│   ├── colors.json # Logs of submitted colors
└── README.md       # Project documentation

Installation
Prerequisites
Node.js and npm installed for the frontend.
Python 3.x and pip installed for the backend.
Steps to Run Locally

1. Clone the Repository
bash
Copy code
git clone "https://github.com/pradyumnarago/color-changer.git"
cd color-changer

2. Start the Backend
Navigate to the backend directory:
bash
Copy code
cd backend

Install the required Python dependencies:
bash
Copy code
pip install flask flask-cors

Run the Flask server:
bash
Copy code
python app.py

3. Start the Frontend
Navigate to the frontend directory:
bash
Copy code
cd frontend

Install the frontend dependencies:
bash
Copy code
npm install

Start the React development server:
bash
Copy code
npm start

Usage
Enter a color name (e.g., blue, red, or a hex code like #FF5733) in the input field.
Submit the color to change the webpage background.
Check the backend log (colors.json) for the list of submitted colors.

Technologies Used
Frontend
React.js
Axios (for API requests)
Backend
Flask
Flask-CORS
