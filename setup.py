from setuptools import setup, find_packages

setup(
    name='aiy',
    version='0.2.0',
    description='Ask question from bash shell and get tailored documentation response',
    author='VisionInit',
    author_email='contact@aimodels.org',
    url='https://github.com/visioninit/aiy',
    packages=find_packages(),
    install_requires=[
        'openai==0.26.4',
        'appdirs==1.4.4',
        'rich==13.3.1',
    ],
    entry_points={
        'console_scripts': [
            'aiy=aiy.aiy:main',
        ],
    },
)
