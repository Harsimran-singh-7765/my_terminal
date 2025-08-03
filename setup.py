from setuptools import setup, find_packages

setup(
    name="myterminal",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'myterminal=myterminal.__main__:main'
        ]
    },
)
