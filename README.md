# News AI Assistant

A Flask-based web application that uses OpenAI's GPT-4 to provide AI and technology news summaries and answer questions about the latest developments in the field.

## Features

- 🔍 Search for latest AI and technology news
- 🤖 AI-powered news summaries
- 💬 Interactive chat interface
- ⚙️ Easy API key configuration
- 📱 Responsive design

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/news-ai.git
cd news-ai
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. If you haven't configured your API key yet, go to the Settings page and enter your OpenAI API key

4. Start asking questions about AI and technology news!

## Project Structure

```
news-ai/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── forms/
│   │   ├── __init__.py
│   │   └── forms.py
│   └── utils/
│       ├── __init__.py
│       └── openai_utils.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── setup.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── .env
├── main.py
├── requirements.txt
└── README.md
```

## API Endpoints

- `GET /`: Home page with chat interface
- `GET/POST /setup`: API key configuration page
- `POST /search_news`: Search for news based on user query
- `POST /ask_question`: Ask questions about specific news topics

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-4 API
- Flask for the web framework
- Bootstrap for the UI components 