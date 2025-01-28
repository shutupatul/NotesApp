# NotesApp

A simple web application for managing notes, built using FastAPI, MongoDB, and HTML/CSS.

## Features

- Add notes with a title, description, and an "important" flag.
- View all your notes with an indication of whether they are marked as important.
- Data is stored in MongoDB for persistence.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **MongoDB**: A NoSQL database to store notes data.
- **HTML/CSS**: Frontend to create a simple user interface for adding and viewing notes.

## Setup

### Prerequisites

- Python 3.7 or higher
- MongoDB (either locally or via MongoDB Atlas)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/shutupatul/NotesApp.git
   cd NotesApp
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Mac/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your **MongoDB connection**:

   - If you're using MongoDB locally, ensure that MongoDB is running on your machine.
   - If you're using MongoDB Atlas, create a MongoDB cluster and replace the `<password>` in the connection string with your actual password.

   ```bash
   MONGO_URI="mongodb+srv://<username>:<password>@fastapitutorial.lwslm.mongodb.net"
   ```

6. Create a `.env` file to securely store your MongoDB URI (as described in the setup guide).

7. Run the FastAPI app:

   ```bash
   uvicorn index:app --reload
   ```

   The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

### Add a Note

- Navigate to the homepage.
- Fill in the title and description for your note.
- Optionally, mark the note as important by checking the checkbox.
- Submit the form to add the note.

### View Notes

- The "Your Notes" section displays all your notes along with their status (whether they are important or not).

## Project Structure

```
NotesApp/
│
├── index.py            # FastAPI app entry point
├── routes/
│   ├── note.py         # Routes for handling notes
│
├── models/
│   └── note.py         # Pydantic model for validating note data
│
├── schemas/
│   └── note.py         # Schemas to transform and serialize note data
│
├── config/
│   └── db.py           # MongoDB connection setup
│
├── templates/           # HTML templates
│   └── index.html      # Main UI for the notes app
│
├── requirements.txt    # List of dependencies
└── .env                # Environment file for MongoDB URI (ignore this in Git)
```

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
