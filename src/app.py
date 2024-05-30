import gradio as gr

def greet(name):
    return "Hello, " + name 

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=5,label="Enter your input",placeholder="Enter here"),
    outputs=["text"],
)

demo.launch()
