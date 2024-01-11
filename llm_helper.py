from langchain.llms import GooglePalm
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector 
from langchain_experimental.sql import SQLDatabaseChain

from db_helper import get_db_object
from few_shorts_learning import few_shots
from prompt_engineering import get_few_short_prompt 

import os
from dotenv import load_dotenv
load_dotenv() # take environment variables from .env


def get_few_short_learning_db_chain():

    #create database connection
    db = get_db_object()
    #print(db.table_info)

    # create llm object
    llm  = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"],  temperature=0.2)

    # create huggingface embedding object
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    # Cereating block of texts from the few_Shorts list
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    # Store the embeddings in Chroma DB 
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
    # Retrieve the the top most Semantically close example from the vector store
    example_selector= SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

    # Getting the final few short promt
    few_shot_prompt = get_few_short_prompt(example_selector)

    # creating the Database chain object with the few short learnings
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

    return chain


chain = get_few_short_learning_db_chain()
chain.run("How much is the price of the inventory for all small size t-shirts?")