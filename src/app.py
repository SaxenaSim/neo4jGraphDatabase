import gradio as gr
from textToCypherQuery import TextToCypher
from log import Logger

logger = Logger.getlogger()
text_to_cypher = TextToCypher()
global_history=[]

# Function to process the input and return the result using TextToCypher class
def process_text_to_cypher(user_input):
    global text_to_cypher
    text_to_cypher_output = text_to_cypher.run(user_input)
    logger.info(f"id of text to cypher class is {text_to_cypher}")
    logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    return text_to_cypher_output

def respond(message):
    global global_history
    response = process_text_to_cypher(message)
    logger.info(f":::::::my response:::::{response}")
    
    print(f"Received message: {message}")
    print(f"Generated response: {response}")
    print(f"Current history before appending: {global_history}")

    global_history.append((message, response))

    print(f"Updated history: {global_history}")
    # history.append((message,response))
    # for i, item in enumerate(history):
    #     logger.info(f":::::::::history element {i}:::::::{item}")
    return global_history,global_history

# def update_state_display(history):
#     return gr.update(value=str(history))

# Create the Gradio chatbot interface
def chatbot_interface():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(label="Cypher Query Chatbot")
        user_input = gr.Textbox(label="Enter your query")
        submit_button = gr.Button("Submit")
        # state_display = gr.Markdown(label="Conversation State")


        #state = gr.State([])
        

        submit_button.click(fn=respond, inputs=[user_input], outputs=[chatbot,gr.State([])])
        # submit_button.click(fn=update_state_display, inputs=[state], outputs=[state_display])


    return demo

# Launch the Gradio chatbot interface
demo = chatbot_interface()
demo.launch()
