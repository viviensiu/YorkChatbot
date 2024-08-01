## Project Goal
* Build and deploy a chatbot that advises users on travelling in York.
* Since it's a personal and non-commercial project, aim for lowest cost possible by leveraging on open-source resources without compromising on chatbot performance.

## Project Methodology
Agile

## System Design
Modular programs:
* Web-scrapping class
* Web-scrapping interface
* Data ingestion into Vector DB
* Embedding class
* LLM class
* Chatbot interface

## Project Timeline
7 July 2024 - 31 August 2024

## Sprints
* Priority : Must-have, good-to-have
* Sprint Task: Description of task
* Timeline: Sprint timeline for task

| Priority | Sprint Task | Timeline |
|----------|-------------|----------|
| Must-have| A Vector database that stores web-scraped data on York travel info.| 8 Jul - 14 Jul|
| Must-have| A basic RAG chatbot using information scraped from a website | 8 Jul - 14 Jul|
| Must-have| Deploy the basic RAG chatbot on HuggingFace Spaces for demo | 15 Jul - 21 Jul|
| Good-to-have| RAG pipeline using dlt Python package to inject new York travel info into the vector DB | N/A|
| Good-to-have| Host the RAG chatbot on Cloud | N/A|

### Task: Web-scraping
* <b>Goal</b>: Scrape VisitYork pages for context.
* **Notes**:
The Google Tag Manager pagination made it impossible to scrape and retrieve all links for all pages, since page numbers are not shown in url. To mitigate this, a Streamlit app was create to allow manual web-scraping by url input into JSON files.

### Task: Vector Database
* <b>Goal</b>: 
    - Store web-scraping data in persistent Vector DB.
    - Vector search to retrieve context based on user query.
* [RAG Stack with PyMongo, OpenAI, LlamaIndex, MongoDB](https://www.mongodb.com/developer/products/atlas/rag-with-polm-stack-llamaindex-openai-mongodb/)
* [RAG with MongoDB Atlas Vector Search, LangChain, and OpenAI on Gradio](https://www.mongodb.com/developer/products/atlas/rag-atlas-vector-search-langchain-openai/#setting-up-the-environment)
* [Code example on MongoDB Atlas Vector Search](https://github.com/mongodb-developer/atlas-vector-search-rag/blob/main/load_data.py)

### Task: LLM
* <b>Goal</b>: Respond to user query based on context

### Task: Chatbot UI
* <b>Goal</b>: Accepts user query and respond to it using RAG.
* References:
    * [Build a simple chatbot GUI with streaming](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)
    * [How to display conversation on opposite sides](https://discuss.streamlit.io/t/how-to-display-user-and-assistant-chat-on-opposite-sides-when-streaming-like-a-conversation/60336/7)

## References
* [Agile 101: How to do a Basic Agile Project](https://www.youtube.com/watch?v=6PqmHhJFXp4)
