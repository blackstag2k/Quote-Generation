# Quotes Generation with Gemini API through LangChain

This project is about generating quotes from topics in a CSV file using **LangChain** and **Google GenAI**

## Workflow

CSV - Prompt Template for LangChain - Google GenAI - Output in the CSV

## Steps to Run the Code

1. Cloning the repository:

git clone https://github.com/blackstag2k/Prompt-Engineering-Projects.git

2. Installing the Dependencies for the project:

* dependencies listed in the requirements.txt

pip install -r requirements.txt 

* If script isn't saved or generated in the 'PATH', then use the command below in Command Window

pip -m install -r requirements.txt

* Example:

** python -m pip install langchain,
** python -m pip install pandas,
** python -m pip install google-generativeai

3. Add your API Key 

* Google AI API, Open AI API, etc. generated from any platform. Google Genai key is used here.

export GOOGLE_API_KEY="YOUR_KEY"

4. Run

python main.py

**Input and Output**

Input CSV:
| topic |
|-------|
| Self Development |
| Time Management |

Output CSV:
| topic | quote |
|-------|--------|
| Self Development | "Self-development is the art of listening to the whispers of your soul." |
| Time Management | "Time is a sculptor's clay awaiting your deliberate touch." |

## Tools Used

LangChain
Google AI API (Gemini)
Pandas
Python 3.14

## Lessons to be Learned

- Connecting LangChain template prompt to Google Gen AI through API key
- Using the Pandas DataFrame as a worksheet to save the particulars of the prompt
- Executing the code through a virtual environment (.venv) like VS Code.


* Documented during the Prompt Engineering Course for automation through *Zapier* and *LangChain*


