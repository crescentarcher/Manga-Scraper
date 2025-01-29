{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Manga-Scraper\
\
A Python-based manga scraper.\
\
## Installation\
\
### 1. Install Python\
If you don\'92t already have Python installed:\
- Download and install it from [python.org](https://www.python.org/).\
- Verify installation by running:\
  ```sh\
  python3 --version\
  ```\
\
### 2. Set Up a Virtual Environment\
It\'92s recommended to use a virtual environment to manage dependencies.\
- Navigate to the project folder:\
  ```sh\
  cd ~/Documents/Manga/Repo/Manga-Scraper\
  ```\
- Create a virtual environment:\
  ```sh\
  python3 -m venv venv\
  ```\
- Activate the virtual environment:\
  ```sh\
  source venv/bin/activate  # macOS/Linux\
  ```\
\
### 3. Install Dependencies\
Inside the activated virtual environment, install the required packages:\
```sh\
pip install requests numpy\
Pip install requests\
```\
\
### 4. Running the Program\
To run the manga scraper:\
```sh\
python3 manga.py\
```\
\
### 5. Deactivating the Virtual Environment\
When you're done, deactivate the virtual environment:\
```sh\
deactivate\
```\
\
## Additional Notes\
- Ensure `pip` is installed and updated:\
  ```sh\
  python3 -m ensurepip\
  python3 -m pip install --upgrade pip\
  ```\
- If you ever need to install additional dependencies, make sure your virtual environment is activated before running `pip install`.\
- To reactivate the virtual environment later:\
  ```sh\
  source venv/bin/activate\
  ```\
\
}