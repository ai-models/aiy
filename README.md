AIY - Ask question from bash shell and get tailored documentation response 
========================================
![image](https://user-images.githubusercontent.com/654993/216212025-5e9e6725-b042-4010-8f4d-649706565b80.png)

AIY is a command line tool that uses OpenAI's language model to provide a documentation-like experience to users. With Aiy, users can get answers to their technical questions and receive step-by-step guidance to complete tasks.

If your organization appreciates this project or is looking for someone to help with your systems and infrastructure, please reach out to me at [LinkedIn](https://www.linkedin.com/in/riddiough/).


<details>
  <summary>Get API Key from OpenAI</summary>

1.  Get your OpenAI API Key:
2.  Go to OpenAI's website ([https://openai.com/api/login](https://openai.com/api/login))
3.  Sign up or log in to your account
4.  Go to the API Key section ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
5.  Create a new secret key
6.  Copy the API key
7.  When running Aiy the first time, you will be prompted for your key
  
</details>

Install on Debian based systems (Debain, Mint, Ubuntu)
-------------------

#### 1. Install our official public software signing key

```
wget -O- https://ppa.aimodels.org/aiy/visioninit.gpg | gpg --dearmor > visioninit.gpg
cat visioninit.gpg | sudo tee -a /usr/share/keyrings/visioninit.gpg > /dev/null
```

#### 2. Add our repository to your list of repositories

```
echo 'deb [signed-by=/usr/share/keyrings/visioninit.gpg] https://ppa.aimodels.org/aiy ./' |\
  sudo tee -a /etc/apt/sources.list.d/aimodels.list
```
  
#### 3. Update your package database and install signal

```sudo apt update && sudo apt install aiy```

( Anyone who might be able to help me get this set up with a snap or flatpack? I've been working on trying to set up these workflows )

Quick Start
-----------

1. Clone repository `git clone https://github.com/visioninit/aiy.git'
2. Change directory `cd aiy`
3. Install dependencies `pip install -r requirements.txt`
4. Run `python aiy` and enter OpenAI key as prompted to complete setup
5. Prompt with `python aiy` or `python aiy "how do I..."` 

Python Requirements
------------

*   Python 3
*   OpenAI API Key
*   Rich library (install via `pip install rich`)
*   dotenv library (install via `pip install python-dotenv`)

Usage
-----

To use AIY, simply run the script and provide a prompt that describes the task you want to complete or the question you want to ask.

For example:

`python aiy.py "How to install and run a web server on Ubuntu?"`

If you have added the script to your path, you can run it from anywhere:

`aiy "How to install and run a web server on Ubuntu?"`

![image](https://user-images.githubusercontent.com/654993/216211945-068bb6a6-b937-44ae-a09c-b75aa8f4d9d6.png)
![image](https://user-images.githubusercontent.com/654993/216211997-167f131f-023b-4b90-8f06-fc7a0e377f6b.png)

Options
-------

* If you wish, you can override automated settings by use of .env file
* You can set the OpenAI model to use by setting the `OPENAI_MODEL` environment variable in your .env file.
* You can disable the notice that is displayed at the end of the response by setting the `OPENAI_DISABLE_NOTICE` environment variable in your .env file.

Contributing
------------

If you'd like to contribute to AIY, feel free to create a pull request or open an issue. All contributions are welcome!
