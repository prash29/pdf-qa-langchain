import gradio as gr
import os
from gradio_app import create_gr_app
from utils import setAPIKey, enable_set_api, add_text_input, generate_response, render_file

demo, api_key, change_api_key, chatbot, show_img, txt, submit_btn, btn = create_gr_app()

# Set up event handlers
with demo:
    # Event handler for submitting the OpenAI API key
    api_key.submit(setAPIKey, inputs=[api_key], outputs=[api_key])

    # Event handler for changing the API key
    change_api_key.click(enable_set_api, outputs=[api_key])

    # Event handler for uploading a PDF
    btn.upload(render_file, inputs=[btn], outputs=[show_img])

    # Event handler for submitting text and generating response
    submit_btn.click(add_text_input, inputs=[chatbot, txt], outputs=[chatbot], queue=False).\
        success(generate_response, inputs=[chatbot, txt, btn], outputs=[chatbot,txt]).\
        success(render_file, inputs=[btn], outputs=[show_img])

if __name__ == "__main__":
    demo.launch()
