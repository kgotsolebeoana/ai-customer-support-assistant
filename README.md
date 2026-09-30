AI Customer Support Assistant
A simple AI-powered customer support web application built with Python and Flask.

Features
Simple web interface

Users can submit questions

Questions are sent to an AI model

AI-generated responses are displayed on the page

Basic input validation

Error handling

API credentials stored using environment variables

Technologies Used
Python

Flask

HTML

CSS

OpenAI API

python-dotenv

How It Works
The user enters a question.

Flask receives the request.

The application sends the question to the AI model.

The AI generates a response.

The response is displayed in the web interface.

Installation
Clone the repository:

git clone https://github.com/YOUR-USERNAME/ai-customer-support-assistant.git

Go into the project directory:

cd ai-customer-support-assistant

Create a virtual environment:

python -m venv .venv

Activate the virtual environment.

Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here

Run the application:

python app.py

Open the local address shown by Flask in your browser.

Security
API keys are stored in environment variables and are excluded from Git using .gitignore.

Future Improvements
Possible improvements include:

Conversation history

User authentication

Database storage

Customer-specific knowledge

Better error handling

Deployment to a cloud platform

Automated tests

Author
Kgotso Lebeoana