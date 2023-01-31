AIY - OpenAI Command Line Assistant
===================================

AIY is a simple command line tool that uses OpenAI's language model to provide a documentation-like experience to users. With AIY, users can get answers to their technical questions and receive step-by-step guidance to complete tasks.

Requirements
------------

*   Python 3
*   OpenAI API Key
*   Rich library (install via `pip install rich`)
*   dotenv library (install via `pip install python-dotenv`)

Getting Started
---------------

1.  Clone the repository: `git clone https://github.com/<username>/aiy.git`

2.  Create a virtual environment: `python3 -m venv venv`

3.  Activate the virtual environment: `source venv/bin/activate`

4.  Install the dependencies: `pip install rich python-dotenv`

5.  Get your OpenAI API Key:
6.  Go to OpenAI's website ([https://openai.com/api/login](https://openai.com/api/login))
7.  Sign up or log in to your account
8.  Go to the API Key section ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
9.  Create a new secret key
10.  Copy the API key
11.  Set your OpenAI API Key in your .env file:

12.  Run the tool:

Copy code

`python aiy.py`

Usage
-----

To use AIY, simply run the script and provide a prompt that describes the task you want to complete or the question you want to ask.

For example:


`python aiy.py "How to install and run a web server on Ubuntu 20.04?"`

Options
-------

* You can set the OpenAI model to use by setting the `OPENAI_MODEL` environment variable in your .env file. For example:

`echo "OPENAI_MODEL=text-davinci-002" > .env`
* You can disable the notice that is displayed at the end of the response by setting the `OPENAI_DISABLE_NOTICE` environment variable in your .env file. For example:

`echo "OPENAI_DISABLE_NOTICE=true" > .env`

Contributing
------------

If you'd like to contribute to AIY, feel free to create a pull request or open an issue. All contributions are welcome!
