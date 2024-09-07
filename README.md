# web-AI-locator
# Web Element Locator

Web Element Locator is a Flask-based web application that uses AI vision capabilities to analyze screenshots of web pages and identify specific HTML elements. It provides detailed descriptions of elements without relying on traditional DOM-based locators, making it useful for web scraping, testing, and accessibility analysis.

## Features

- Capture screenshots of web pages automatically
- Analyze web page elements using AI vision
- Provide detailed descriptions of element positions, sizes, and attributes
- Handle various types of web content responsibly
- User-friendly web interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)
- Google Chrome browser (for Selenium WebDriver)
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/web-element-locator.git
   cd web-element-locator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Anthropic API key:
   - Sign up for an account at [Anthropic](https://www.anthropic.com)
   - Obtain your API key
   - Set it as an environment variable:
     ```
     export ANTHROPIC_API_KEY='your_api_key_here'
     ```
     On Windows, use `set` instead of `export`.

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Enter a website URL and the type of element you want to locate (e.g., "button", "div", "a").

4. Click "Analyze Website" and wait for the results.

## Configuration

You can modify the following parameters in `app.py`:

- `MAX_CONTENT_LENGTH`: Maximum allowed file size for uploads
- `ALLOWED_EXTENSIONS`: Allowed file types for uploads
- Screenshot dimensions in the `capture_screenshot` function

## Contributing

Contributions to the Web Element Locator project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project uses the following license: [MIT License](LICENSE).

## Contact

If you want to contact me, you can reach me at `<your_email@example.com>`.

## Acknowledgements

- [Anthropic](https://www.anthropic.com) for providing the AI vision capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Selenium](https://www.selenium.dev/) for web page screenshot capture