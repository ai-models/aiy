AIY - Command Line Assistant with OpenAI
========================================

AIY is a simple command line tool that uses OpenAI's language model to provide a documentation-like experience to users. With AIY, users can get answers to their technical questions and receive step-by-step guidance to complete tasks.

Disclaimer: This is not an official OpenAI product, and is not endorsed by OpenAI. It's a personal project that I created to learn more about OpenAI's language model.

If your organization appreciates this project or is looking for someone to help with your systems and infrastructure, please reach out to me at [LinkedIn](https://www.linkedin.com/in/riddiough/).

Requirements
------------

*   Python 3
*   OpenAI API Key
*   Rich library (install via `pip install rich`)
*   dotenv library (install via `pip install python-dotenv`)

Quick Start
-----------
# Setup
1. Clone repository `git clone https://github.com/visioninit.aiy.git'
2. Change directory `cd aiy`
3. Install dependencies `pipenv install` (or `pip install -r requirements.txt`)
4. Configure and rename .env `mv .env.default .env` (env is not required)

Configuration
---------------

1.  Get your OpenAI API Key:
2.  Go to OpenAI's website ([https://openai.com/api/login](https://openai.com/api/login))
3.  Sign up or log in to your account
4.  Go to the API Key section ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
5.  Create a new secret key
6.  Copy the API key
7.  Set your OpenAI API Key in your .env file

Usage
-----

To use AIY, simply run the script and provide a prompt that describes the task you want to complete or the question you want to ask.

For example:

`python aiy.py "How to install and run a web server on Ubuntu?"`

If you have added the script to your path, you can run it from anywhere:

`aiy "How to install and run a web server on Ubuntu?"`

Options
-------

* You can set the OpenAI model to use by setting the `OPENAI_MODEL` environment variable in your .env file.

* You can disable the notice that is displayed at the end of the response by setting the `OPENAI_DISABLE_NOTICE` environment variable in your .env file.


Contributing
------------

If you'd like to contribute to AIY, feel free to create a pull request or open an issue. All contributions are welcome!
