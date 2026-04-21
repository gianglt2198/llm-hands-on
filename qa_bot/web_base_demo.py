import gradio as gr

from llm import generate_response

chat_application = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

chat_application.launch(server_name="127.0.0.1", server_port= 7860)