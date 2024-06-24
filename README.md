# Cypher Query Chatbot with Gradio, CrewaI, OpenAI, and Neo4j

This project features a chatbot interface built with Gradio that converts user input into Cypher queries using CrewaI and OpenAI, fetches data from a Neo4j database, and displays the results in the UI.

## Features

- **User-friendly Chatbot Interface**: Implemented using Gradio for easy interaction.
- **Cypher Query Conversion**: Uses CrewaI and OpenAI to translate natural language inputs into Cypher queries.
- **Neo4j Database Integration**: Fetches data from a Neo4j database based on generated Cypher queries.
- **Real-time Responses**: Provides immediate feedback and results in the UI.

## Technologies Used

- **Gradio**: For building the interactive chatbot interface.
- **CrewaI**: For handling natural language processing and Cypher query conversion.
- **OpenAI**: For leveraging language model capabilities.
- **Neo4j**: As the database for storing and querying graph data.
- **Python**: Core programming language for the backend.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Neo4j Database
- Required Python packages (listed in `requirements.txt`)

### Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/SaxenaSim/neo4jGraphDatabase/tree/updates

    cd neo4jGraphDatabase
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Neo4j Database**:
    - Ensure your Neo4j database is running.
    - Configure the connection details (URL, username, password) in your project settings.

### Configuration

Configure your API keys and database connection details in a `.env` file or directly in the script as needed:

```env
OPENAI_API_KEY=your_openai_api_key
NEO4J_URI=your_neo4j_uri
NEO4J_USER=your_neo4j_username
NEO4J_PASSWORD=your_neo4j_password
```

## Running the Application

Start the Neo4j Database:

Make sure your Neo4j database is up and running.

Run the Chatbot Interface:

```sh
    python app.py
```

This will start the Gradio interface. Open the provided local URL in your browser to interact with the chatbot.

## Usage

Open the Gradio interface in your browser.
Enter your natural language query in the text input field.
The chatbot will process the input, convert it into a Cypher query, fetch the relevant data from the Neo4j database, and display the results.

## Project Structure

app.py: Main application script to run the Gradio interface and handle backend logic.

requirements.txt: List of required Python packages.

src: Folder which contains all the python scripts having backend logic to fetch data from the database.

data: This contains the sample dataset csv files on which the queries are being run.

README.md: Project documentation.


