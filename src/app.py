import gradio as gr
from textToCypherQuery import TextToCypher
from log import Logger

# Initialize logger and TextToCypher instance
logger = Logger.getlogger()
text_to_cypher = TextToCypher()

# Global variable to maintain conversation history
global_history = []

# Function to process the input and return the result using TextToCypher class
def process_text_to_cypher(user_input):
    global text_to_cypher
    text_to_cypher_output = text_to_cypher.run(user_input)
    logger.info(f"id of text to cypher class is {text_to_cypher}")
    logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
    return text_to_cypher_output

# Function to respond to user input
def respond(message):
    global global_history
    response = process_text_to_cypher(message)
    logger.info(f":::::::my response:::::{response}")

    # Append the new message-response pair to the global history
    global_history.append((message, response))

    return global_history, global_history

# Create the Gradio chatbot interface
def chatbot_interface():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(label="Cypher Query Chatbot",avatar_images=('https://www.techopedia.com/wp-content/uploads/2023/03/6e13a6b3-28b6-454a-bef3-92d3d5529007.jpeg','https://static.vecteezy.com/system/resources/thumbnails/005/129/844/small_2x/profile-user-icon-isolated-on-white-background-eps10-free-vector.jpg'))
        user_input = gr.Textbox(label="Enter your query")
        submit_button = gr.Button("Submit")

        # Ensure the correct function and input-output mappings
        submit_button.click(fn=respond, inputs=[user_input], outputs=[chatbot, gr.State([])])

    return demo

# Launch the Gradio chatbot interface
demo = chatbot_interface()
demo.launch()







































# import gradio as gr
# from textToCypherQuery import TextToCypher
# from log import Logger

# # Initialize logger and TextToCypher instance
# logger = Logger.getlogger()
# text_to_cypher = TextToCypher()

# # Global variable to maintain conversation history
# global_history = []

# # Function to process the input and return the result using TextToCypher class
# def process_text_to_cypher(user_input):
#     global text_to_cypher
#     text_to_cypher_output = text_to_cypher.run(user_input)
#     logger.info(f"id of text to cypher class is {text_to_cypher}")
#     logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
#     return text_to_cypher_output

# # Function to respond to user input
# def respond(message):
#     global global_history
#     response = process_text_to_cypher(message)
#     logger.info(f":::::::my response:::::{response}")
    
#     # Debug print statements to trace history
#     print(f"Received message: {message}")
#     print(f"Generated response: {response}")
#     print(f"Current history before appending: {global_history}")

#     # Append the new message-response pair to the global history
#     global_history.append((message, response))

#     # Print the updated history
#     print(f"Updated history: {global_history}")

#     # Log each element in the history
#     for i, item in enumerate(global_history):
#         logger.info(f":::::::::history element {i}:::::::{item}")
#         print(f":::::::::history element {i}:::::::{item}")

#     # Add icons to messages
#     styled_history = [
#         (f'<div class="user-message"><i class="fa-solid fa-user"></i><span>{m}</span></div>', 
#          f'<div class="bot-message"><i class="fa-brands fa-discord"></i><span>{r}</span></div>') 
#         for m, r in global_history
#     ]

#     # Ensure the correct return value format
#     return styled_history, styled_history

# # Create the Gradio chatbot interface
# def chatbot_interface():
#     with gr.Blocks(css="""
#     .user-message, .bot-message {
#         display: flex;
#         align-items: center;
#     }
#     .user-message .icon, .bot-message .icon {
#         font-size: 20px;
#         margin-right: 10px;
#     }
#     .user-message {
#         justify-content: flex-end;
#     }
#     .bot-message {
#         justify-content: flex-start;
#     }
#     """) as demo:
#         gr.HTML('''
#                 <head>
#                     <script src="https://kit.fontawesome.com/ee138b12bd.js" crossorigin="anonymous"></script>
#                 </head>
#         ''')
#         chatbot = gr.Chatbot(label="Cypher Query Chatbot")
#         user_input = gr.Textbox(label="Enter your query")
#         submit_button = gr.Button("Submit")

#         # Ensure the correct function and input-output mappings
#         submit_button.click(fn=respond, inputs=[user_input], outputs=[chatbot, gr.State([])])

#     return demo

# # Launch the Gradio chatbot interface
# demo = chatbot_interface()
# demo.launch()





























# import gradio as gr
# from textToCypherQuery import TextToCypher
# from log import Logger

# logger = Logger.getlogger()
# text_to_cypher = TextToCypher()
# global_history=[]

# # Function to process the input and return the result using TextToCypher class
# def process_text_to_cypher(user_input):
#     global text_to_cypher
#     text_to_cypher_output = text_to_cypher.run(user_input)
#     logger.info(f"id of text to cypher class is {text_to_cypher}")
#     logger.info(f":::::::::::returning the output:::::::{text_to_cypher_output}")
#     return text_to_cypher_output

# def respond(message):
#     global global_history
#     response = process_text_to_cypher(message)
#     logger.info(f":::::::my response:::::{response}")
    
#     print(f"Received message: {message}")
#     print(f"Generated response: {response}")
#     print(f"Current history before appending: {global_history}")

#     global_history.append((message, response))

#     print(f"Updated history: {global_history}")
#     # history.append((message,response))
#     # for i, item in enumerate(history):
#     #     logger.info(f":::::::::history element {i}:::::::{item}")
#     return global_history,global_history

# # def update_state_display(history):
# #     return gr.update(value=str(history))

# # Create the Gradio chatbot interface
# def chatbot_interface():
#     with gr.Blocks() as demo:
#         chatbot = gr.Chatbot(label="Cypher Query Chatbot")
#         user_input = gr.Textbox(label="Enter your query")
#         submit_button = gr.Button("Submit")
#         # state_display = gr.Markdown(label="Conversation State")


#         #state = gr.State([])
        

#         submit_button.click(fn=respond, inputs=[user_input], outputs=[chatbot,gr.State([])])
#         # submit_button.click(fn=update_state_display, inputs=[state], outputs=[state_display])


#     return demo

# # Launch the Gradio chatbot interface
# demo = chatbot_interface()
# demo.launch()
