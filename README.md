
# Quiz App

A web application that generates quizzes based on user-provided topics locally using gemma:2b LLM , allowing users to test their knowledge and view their scores instantly.

## Features

- Generate quizzes based on user-defined topics.
- Display dynamically generated questions with answer options.
- Submit answers and calculate scores automatically.
- Configure the number of questions through the code.

## Tech Stack

- Python
- Flask
- HTML and CSS
- SQLite

## Project Structure

```text
QUIZ-APP/
├── app.py
├── database.py
├── generate_quiz.py
├── quiz.db
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── quiz.html
│   └── result.html
└── README.md
```

## Setup and Execution

1. Clone the repository:

   ```bash
   git clone https://github.com/Harsa-2004/Quiz-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Quiz-App
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open the local URL displayed in the terminal.

## Usage

Enter a topic, generate the quiz, select answers for the questions, and submit to view your final score.

## Author

Harsa Vardhini

GitHub: [Harsa-2004](https://github.com/Harsa-2004)
