# Groq API Speed Test One

This Python program allows users to test the response speed of various language models available through the Groq API. Key features include:

1. Interactive model selection from a predefined list of available models.
2. Customizable number of test runs per session.
3. Measures and displays the response time for each run.
4. Calculates and shows the average response time across all runs.
5. Uses a consistent prompt to test different models for comparison.
6. Handles potential errors gracefully, such as invalid model selection or API issues.

The program is designed to help users benchmark the performance of different Groq models, allowing for easy comparison of speed and response quality across various AI language models.

# Groq API Speed Test Two

## Description

This Python program automatically benchmarks and compares the response times of various AI language models available through the Groq API. It's designed to help you assess the performance of different models across multiple runs, providing insights into their speed and efficiency.

## Features

- Automatically tests five Groq API models:
  - gemma2-9b-it
  - gemma-7b-it
  - llama3-70b-8192
  - llama3-8b-8192
  - mixtral-8x7b-32768
- Allows user to specify the number of runs for each model
- Measures and displays response time for each run
- Calculates average response time for each model
- Announces the fastest model at the end of all tests
- Colorful and engaging command-line interface

## Requirements

- Python 3.6 or higher
- `groq` Python library
- `colorama` Python library

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.

2. Install the required libraries:

   ```
   pip3 install groq colorama
   ```

3. Set up your Groq API key:
   - Sign up for a Groq account and obtain your API key
   - In the script, replace `"your_groq_api_key_here"` with your actual Groq API key

## Usage

1. Save the script as `groq_speed_test.py`.

2. Run the script:

   ```
   python3 groq_speed_test.py
   ```

3. When prompted, enter the number of runs you want to perform for each model.

4. The program will automatically test all five models and display the results.

5. At the end of the test, the program will announce the fastest model.

## Output

The program provides a colorful output in the terminal:
- Cyan: Headers and user prompts
- Green: Model names
- Yellow: Individual run times
- White: Model responses
- Magenta: Average times for each model
- Red: Winner announcement

## Note

This program uses a fixed prompt for testing all models. If you want to test with different prompts, you can modify the `prompt` variable in the `main()` function.

## Troubleshooting

If you encounter any issues:
- Ensure your Groq API key is correct and has the necessary permissions
- Check your internet connection
- Verify that you have the latest versions of the `groq` and `colorama` libraries

## License

[Specify your chosen license here]

## Author

[Your Name]

## Acknowledgments

- Groq for providing the API
- Colorama for the colored terminal output

Enjoy racing your AI models! 🏎️💨
