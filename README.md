# **AI-Powered Chatbot with Langgraph and Powered by Gemma2-9b-It**

## **Purpose**

This Streamlit application allows users to interact with a chatbot powered by the Langgraph framework and the Gemma2-9b-It model. It facilitates real-time conversations and dynamic responses through an intuitive web interface.

[![Streamlit App](https://img.shields.io/badge/Streamlit_App_-Langraph_PDF_QA_Chatbot-ff69b4.svg?style=for-the-badge&logo=Streamlit)](https://langgraphaipoweredchatbot-hckfqhgaabazappsukyyrjw.streamlit.app/)





## **Dependencies**

- **Streamlit**: For building interactive web applications.
- **langchain_groq**: Provides access to Groq’s conversational AI models.
- **langgraph**: Framework for managing conversational state and flow.
- **dotenv**: For loading environment variables from a .env file.

## **Main Functions and Workflow**

### **Setup Environment**

The `setup_environment` function configures environment variables, including API keys and project settings, to ensure the chatbot can access necessary resources.

### **Initialize LLM**

The `initialize_llm` function initializes the ChatGroq model using the provided API key and model name. This sets up the conversational AI model used for generating responses.

### **Define State Class and Build Graph**

The `State` class defines the structure of the conversation state. The `build_graph` function constructs a state graph to manage conversational flow, setting up nodes and edges to handle and process user messages.

### **Streamlit Chatbot Interface**

The `chatbot_ui` function sets up the Streamlit interface for the chatbot, including:
- **Title**: Displays the title of the application.
- **Session State**: Initializes and manages the chat history.
- **User Input**: Captures user input and processes it through the conversational model.
- **Sidebar**: Displays application details, including framework, model, and key features.

## **Usage**

1. Users upload PDF files.
2. Clicking "Submit & Process" initiates the processing of the PDF, including text extraction and chunking.
3. Users input questions related to the content, and the AI provides answers based on the processed information.
4. Users can reset the app or save the chat history.

## **Summary**

The application integrates AI and NLP techniques to interact with PDF content through a web interface. It handles text extraction, processing, and question answering, enhancing the usability and accessibility of PDF content through automation and AI capabilities.

## **Author**

This app was created by **`Parthebhan Pari`**.

## **Notes**

- **Model**: Uses Groq’s conversational AI model for generating responses.
- **API Key**: Ensure that the API key for Groq is securely handled and loaded from environment variables.
- **Security**: Ensure that API keys and sensitive data are managed securely.

## **🔗 Connect with Me**

Feel free to connect with me on:

- [![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)
- [![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)
- [![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)
- [![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)
