import gradio as gr
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI

# Define function for clarity and organization
def initialize_models():
    """
    Initializes the ChatOpenAI model using the provided API key.

    Returns:
        ChatOpenAI instance: The initialized ChatOpenAI object.
    """

    return ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key="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"
    )

# Create the ChatOpenAI instance
openai = initialize_models()

def chatbot(user_input):
    """
    Processes user input, formats the prompt, and invokes the ChatOpenAI model.

    Args:
        user_input (str): The user's query.

    Returns:
        str: The ChatOpenAI model's response, formatted as a step-by-step answer.
    """

    # Define the prompt template with clear variable names and formatting
    template = """
    **Question:** {question}

    **Please provide step-by-step instructions:**
    """

    # Create a PromptTemplate object using the defined template
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Format the prompt with the user's input
    formatted_prompt = prompt.format(question=str(user_input))

    # Invoke the ChatOpenAI model and return its content
    return openai.invoke(formatted_prompt).content.strip()  # Remove potential leading/trailing whitespace

# Launch the Gradio interface
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(share=True)
