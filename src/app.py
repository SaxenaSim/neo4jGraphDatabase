import gradio as gr
from textToCypherQuery import TextToCypher
from log import Logger

logger = Logger.getlogger()
text_to_cypher = TextToCypher()


# Function to process the input and return the result using TextToCypher class
def process_text_to_cypher(user_input):
    global text_to_cypher
    text_to_cypher_output = text_to_cypher.run(user_input)
    logger.info(f"id of text to cypher class is {text_to_cypher}")
    logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    return text_to_cypher_output

def respond(message,history):
    response = process_text_to_cypher(message)
    logger.info(f":::::::my response:::::{response}")
    history.append((message,response))
    return history,history

# Create the Gradio chatbot interface
def chatbot_interface():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(label="Cypher Query Chatbot")
        user_input = gr.Textbox(label="Enter your query")
        submit_button = gr.Button("Submit")

        state = gr.State([])

        submit_button.click(fn=respond, inputs=[user_input,state], outputs=[chatbot,state])

    return demo

# Launch the Gradio chatbot interface
demo = chatbot_interface()
demo.launch()
