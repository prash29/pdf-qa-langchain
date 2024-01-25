import gradio as gr
import os


## Gradio App
def create_gr_app():
    with gr.Blocks(title = "ChatPDF-GPT",
                   theme="default") as app:
        
        # Gradio Block
        with gr.Column():
            with gr.Row():
                with gr.Column(scale = 0.75):
                    api_key = gr.Textbox(
                        placeholder="Enter your OpenAI API Key",
                        show_label=False,
                        interactive=True,
                        container=False
                    )
            
                with gr.Column(scale = 0.2):
                    change_api_key = gr.Button("Update API Key")
            
            with gr.Row():
                chatbot = gr.Chatbot(value=[], elem_id='chatbot',height=700)
                show_img = gr.Image(label = 'PDF Preview', tool='select', height=700)
        
        with gr.Row():
            with gr.Column(scale=0.6):
                text_input = gr.Textbox(
                    show_label = False,
                    placeholder='Type in your question here!',
                    container=False
                )
            
            with gr.Column(scale=0.2):
                submit_button = gr.Button('Send')
            
            with gr.Column(scale = 0.2):
                upload_button = gr.UploadButton("Upload your PDF", file_types=[".pdf"])
        
        return app, api_key, change_api_key, chatbot, show_img, text_input, submit_button, upload_button

if __name__ == '__main__':
    app, api_key, change_api_key, chatbot, show_img, text_input, submit_button, upload_button = create_gr_app()
    app.queue()
    app.launch()

            