import gradio as gr
from textToCypherQuery import TextToCypher

# Function to process the input and return the result using TextToCypher class
def process_text_to_cypher(user_input):
    text_to_cypher = TextToCypher(user_input)
    result = text_to_cypher.run()
    return result

# Create the Gradio chatbot interface
def chatbot_interface():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(label="Cypher Query Chatbot")
        user_input = gr.Textbox(label="Enter your query")
        submit_button = gr.Button("Submit")

        def respond(message):
            response = process_text_to_cypher(message)
            return [(message, response)]

        submit_button.click(fn=respond, inputs=user_input, outputs=chatbot, api_name="process_text_to_cypher")

    return demo

# Launch the Gradio chatbot interface
demo = chatbot_interface()
demo.launch()




















# import gradio as gr
# from textToCypherQuery import TextToCypher


# def process_text_to_cypher(user_input):
#     text_to_cypher = TextToCypher(user_input)
#     result = text_to_cypher.run()
#     return result

# # Create the Gradio chatbot interface
# def chatbot_interface():
#     with gr.Blocks() as demo:
#         chatbot = gr.Chatbot(label="Cypher Query Chatbot")
#         user_input = gr.Textbox(label="Enter your query")
#         submit_button = gr.Button("Submit")

#         submit_button.click(fn=process_text_to_cypher, inputs=user_input, outputs=chatbot,api_name="process_test_to_cypher")

#     return demo

# # Launch the Gradio chatbot interface
# demo = chatbot_interface()
# demo.launch()

# text_to_cypher_instance = None

# def process_text_to_cypher(text_input):
#     global text_to_cypher_instance
#     if text_to_cypher_instance is None:
#         text_to_cypher_instance = TextToCypher(text_input)
#     else:
#         text_to_cypher_instance.input = text_input
    
#     result = text_to_cypher_instance.run()
#     return result
#     # text_to_cypher = TextToCypher(text_input)
#     # result = text_to_cypher.run()
#     # return result

# # Create the Gradio interface
# with gr.Blocks() as demo:
#     text_input = gr.Textbox(label="Enter your query")
#     output = gr.Textbox(label="Cypher Query Result")

#     submit_button = gr.Button("Submit")
#     # button = gr.Button("qwe")
#     # button.click(fn=process_text_to_cypher,inputs=text_input,outputs=output,api_name="process_text_to_cypher")    
#     submit_button.click(
#         fn=process_text_to_cypher,
#         inputs=text_input,
#         outputs=output,
#         api_name="process_text_to_cypher"
#     )

# # Launch the Gradio interface
# if __name__ == "__main__":
#     demo.launch()
