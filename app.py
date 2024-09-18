# Import necessary libraries
import os
import streamlit as st

from langchain_groq import ChatGroq
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
load_dotenv()

# Step 1: Environment and API Setup
def setup_environment():
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Langgraph_Chatbot"

# Step 2: Initialize LLM
def initialize_llm():
    groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure the Groq API key is set
    return ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Step 3: Define State Class and Build Graph
class State(TypedDict):

    messages: Annotated[list, add_messages]

def build_graph(llm):
    graph_builder = StateGraph(State)
    
    def chatbot(state: State):
        return {"messages": llm.invoke(state['messages'])}

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder.compile()

# Step 4: Streamlit Chatbot Interface
def chatbot_ui(graph):
    st.title("AI-Powered Chatbot with Langgraph and Powered by Gemma2-9b-It")

    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # User Input without clearing the input
    user_input = st.text_input("You: ", key="input_text")

    st.sidebar.markdown("<h3 style='font-size: 32px;'>App Details</h3>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<h3 style='color: #2ca02c;font-size: 20px;'>App Created by: Parthebhan Pari</h3>", unsafe_allow_html=True)
    
    st.sidebar.markdown("""
                        
        
                        
        **Framework:** Langgraph

        **Model:** Gemma2-9b-It

        **Overview:**
        The AI-Powered Chatbot utilizes the Langgraph framework for dynamic conversational capabilities and the Gemma2-9b-It model for generating sophisticated and contextually relevant responses.

        **Key Features:**
        - **Interactive Conversations:** Engage with the chatbot for various queries and tasks.
        - **Real-time Responses:** Instant and context-aware replies from the AI.
        - **Customizable Integration:** Built with flexibility for modifications and enhancements.

        **How It Works:**
        1. **Input:** Type your message into the input field.
        2. **Processing:** The chatbot uses the Gemma2-9b-It model to process and understand the input.
        3. **Response:** Receive a generated response based on the input context.

        
        **Contact:**
        For questions or feedback, please reach out to me.

        **Configuration:**
        - **API Key:** Configured through environment variables for security.
        - **Project:** Langgraph_Chatbot
        """, unsafe_allow_html=True)

    

    if st.button("Send") and user_input:
        # Add user's message to the session state
        st.session_state['messages'].append(("user", user_input))
        
        # Process the conversation through the graph
        for event in graph.stream({'messages': st.session_state['messages']}):
            for value in event.values():
                response_message = value['messages'].content
                st.session_state['messages'].append(("assistant", response_message))
                st.write(f"Assistant: {response_message}")

# Main Streamlit App
def main():
    setup_environment()
    llm = initialize_llm()
    graph = build_graph(llm)

    # Display chatbot interface
    chatbot_ui(graph)

# Streamlit execution point
if __name__ == "__main__":
    main()
