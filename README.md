# Movie Expert Chatbot

## Overview
The Movie Expert Chatbot leverages the OpenAI GPT-4 model, integrated with LangChain to provide an interactive chat interface in the Mac Terminal. It's designed to retrieve and deliver detailed information about movies from a Neo4J database. The bot handles queries about film titles, directors, actors, and taglines, offering an engaging and informative experience for movie enthusiasts.

## Prerequisites
- macOS (or a Unix-like environment)
- Python 3.6 or higher
- Neo4J Database
- An OpenAI API key

## Setup Instructions

### Install Dependencies
Before running the chatbot, you must install necessary Python dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Neo4J Database Setup
Ensure your Neo4J database is up and running. Adjust the connection settings in the graph.py file to match your database credentials.

## OpenAI API Key Configuration
To use the GPT-4 model, you need to set your OpenAI API key in your environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

## Running the Chatbot
```bash
python3 movies-neo4j.py
```
## Features
- GPT-4 Model: Utilizes the latest GPT-4 model from OpenAI for understanding and generating human-like text.
- LangChain Integration: Enhances the chatbot's capabilities with advanced AI conversational frameworks.
- Neo4J Database Connectivity: Directly queries a Neo4J database for accurate and up-to-date movie information.
- Interactive CLI: Simple and easy-to-use command line interface for querying movie data.

## Usage
Ask questions about movie details directly in the Mac Terminal. Example queries include:

"Tell me about Inception."
"Who directed The Godfather?"
"Who starred in Pulp Fiction?"
To exit the chatbot, type exit, goodbye, or bye.

## Feedback
After exiting, you will be prompted to provide feedback on your session. This helps improve the bot's performance and user experience.

