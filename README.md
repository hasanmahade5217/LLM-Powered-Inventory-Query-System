# LLM Powered Inventory Query System: Talk to a MySQL Database


In this Large Language Model (LLM) project, leveraging the capabilities of Google Palm model and Langchain library, I  aim to create a system that seamlessly interacts with a MySQL database. The user interface enables natural language inquiries, where users ask questions, and the system responds by transforming those questions into SQL queries. This, in turn, facilitates the retrieval of information from the MySQL database. 

This project is tailored for AtliQ Tees, a T-shirt store managing inventory, sales, and discount data within a MySQL Database. Using this system, store managers can effortlessly seek information by articulating questions in everyday language, allowing for efficient and intuitive database interaction.


## Sample Questions
  - How many total t shirts are left in total in stock?
  - How many t-shirts do we have left for Nike in XS size and white color?
  - How much is the total price of the inventory for all S-size t-shirts?
  - How much sales amount will be generated if we sell all small size adidas shirts today after discounts?

## Project Structure

- main.py: The main Streamlit application script.
- llm_helper.py: This has the langchain framework code
- db_helper.py: This has the MySQL database connection code
- prompt_engineering: This file handles the promt cretion for the LLM
- requirements.txt: A list of required Python packages for the project.
- few_shots.py: Contains few shot prompts
- .env: Configuration file for storing your Google API key.


## Technology Used:
1. LLM MODEL: Google PaLM
2. Language: Python
3. Framework: Langchain 
4. Embeddings: Hugging Face Embeddings
5. Vector Database: ChromaDB
6. UI: Streamlit 
7. Environment: Conda Virtual Environment
8. Version Control: Git (GitHub)
9. Standard Practices


## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/hasanmahade5217/LLM-Powered-Inventory-Query-System.git
```
2. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
3. Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY = "USE YOUR OWN GOOGLE API KEY"
```
4. For database setup, run database/db_creation_atliq_t_shirts.sql in your MySQL workbench

## Usage

1. Run the Streamlit app using the following:

```bash
streamlit run main.py
```

2. The web app will open in your browser where you can ask questions