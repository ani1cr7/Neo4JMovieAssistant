import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Import the graph object from graph.py for Neo4J database interactions
from graph import graph

# Function to get OpenAI API key from environment variable
def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    return api_key

# Initialize the language model with the API key
chat_llm = ChatOpenAI(openai_api_key=get_openai_api_key())

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a movie expert, helping users find information about movies, actors, and directors.",
        ),
        ("system", "{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

# Initialize the chat message history
memory = ChatMessageHistory()

# Function to return the chat memory
def get_memory(session_id):
    return memory

# Function to query Neo4J for movie details based on user input
def query_movies(question):
    # Example query to fetch movie information based on title
    query_result = graph.run("MATCH (m:Movie {title: $title}) RETURN m.title, m.year, m.tagline", title=question).data()
    if query_result:
        return " ".join([f"{key}: {val}" for item in query_result for key, val in item.items()])
    return "No details found for that movie."

# Create the chat chain
chat_chain = prompt | chat_llm | StrOutputParser()

# Wrap the chat chain with message history handling
chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)
# Function to gather user feedback at the end of the session
def get_feedback():
    feedback = input("Was this chat session good or bad? ")
    print(f"Thank you for your feedback: {feedback}")
    
# Function to query Neo4J for movie details based on user input
def query_movies(question):
    print(f"Querying Neo4J for: {question}")  # Print the query intention
    # Example query to fetch movie information based on title
    query_result = graph.run("MATCH (m:Movie {title: $title}) RETURN m.title, m.year, m.tagline", title=question).data()
    if query_result:
        response = " ".join([f"{key}: {val}" for item in query_result for key, val in item.items()])
        print(f"Neo4J response: {response}")  # Print what Neo4J returned
        return response
    print("No details found for that movie in Neo4J.")  # Indicate no results found
    return "No details found for that movie."

# Main loop and other parts of your script remain unchanged

# Test the query_movies function right at the beginning to check database connectivity
test_movie = "Inception"  # Change this to any movie title you expect to be in your database
print("Running initial database test...")
initial_test_result = query_movies(test_movie)
print(f"Initial test query result: {initial_test_result}")


# Main loop to interact with the chatbot
print("What questions can I answer about movies?")


while True:
    try:
        question = input("> ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        # Check if the question is about a specific movie
        if "details about" in question.lower():
            movie_title = question.split("details about")[1].strip()
            response = query_movies(movie_title)
        else:
            response = chat_with_message_history.invoke(
                {
                    "context": "",
                    "question": question,
                },
                config={
                    "configurable": {"session_id": "none"}
                }
            )

        print(response)
        get_feedback()  # Collect feedback even if interrupted
    except KeyboardInterrupt:
        print("\nGoodbye!")
        
        break
    except Exception as e:
        print(f"An error occurred: {e}")
