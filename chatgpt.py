import os

import streamlit as st
from revChatGPT.V1 import Chatbot
from streamlit_chat import message

# Set up chatbot : https://chat.openai.com/api/auth/session
config = {
    "Authorization": "<leave this as whatever - it will get replaced>",
    "access_token": os.environ.get("CHATGPT_ACCESS_TOKEN"),
}
# Initialize chatbot
chatbot = Chatbot(config, conversation_id=None)

# Define functions
def update_history(prompt):
    response = ''
    for data in chatbot.ask(prompt):
        response = data["message"]
    print(response)
    return response 

def generate_response(prompt, history):
    history = history or []
    s = ' '.join(sum(history, ()))
    print(s)
    output = update_history(f'{s} {prompt}')
    history.append(output)
    return history, history

def main():
    # Set up Streamlit app
    st.set_page_config(
        page_title="Streamlit Chat - Demo",
        page_icon=":robot:"
    )
    st.header("ChatGPT Clone")

    history_input = []

    # Initialize session state
    st.session_state.setdefault('generated', [])
    st.session_state.setdefault('past', [])

    # Get user input
    user_input = st.text_input("You: ", key="input")

    # Generate and display responses
    if user_input:
        output = generate_response(user_input, history_input)
        history_input.append([user_input, output])
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output[0])
        
    # Display past messages
    for i, (gen, past) in enumerate(zip(reversed(st.session_state.generated), reversed(st.session_state.past))): 
        message(gen, key=str(i))
        message(past, is_user=True, key=f'{i}_user')

if __name__ == '__main__':
    main()