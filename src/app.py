import gradio as gr
from textToCypherQuery import TextToCypher
from log import Logger

# Initialize logger and TextToCypher instance
logger = Logger.getlogger()
text_to_cypher = TextToCypher()

# Function to process the input and return the result using TextToCypher class
def process_text_to_cypher(user_input):
    global text_to_cypher
    try:
        text_to_cypher_output = text_to_cypher.run(user_input)
        logger.info(f"id of text to cypher class is {text_to_cypher}")
        logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    except Exception as e:
        logger.info(f":::error in process_text_to_cypher::::{e}")
    return text_to_cypher_output


def simple_interface():
    # Function to respond to user input
    def respond(message,history):
        try:
            logger.info(f":::::::::Received message::::::::::::::: {message}")
            logger.info(f"::::::::::::Current history::::::::::::: {history}")    
            response = process_text_to_cypher(message)
            logger.info(f":::::::my response:::::{response}")

            # Append the new message-response pair to the global history
            history.append((message, response))
            logger.info(f":::::::::::::::Updated history::::::::::: {history}")
        except Exception as e:
            logger.info(f":::::error in respond:::::::{e}")
        return history, history

    # Create the Gradio chatbot interface
    try:
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot(label="Cypher Query Chatbot",avatar_images=('https://static.vecteezy.com/system/resources/thumbnails/005/129/844/small_2x/profile-user-icon-isolated-on-white-background-eps10-free-vector.jpg','https://www.techopedia.com/wp-content/uploads/2023/03/6e13a6b3-28b6-454a-bef3-92d3d5529007.jpeg'))
            user_input = gr.Textbox(label="Enter your query")
            submit_button = gr.Button("Submit")
            
            state = gr.State([])

            # Ensure the correct function and input-output mappings
            submit_button.click(fn=respond, inputs=[user_input,state], outputs=[chatbot, state])
    except Exception as e:
        logger.info(f":::error in blocks:::::{e}")
    return demo

# Launch the Gradio chatbot interface
demo = simple_interface()
demo.launch()







































