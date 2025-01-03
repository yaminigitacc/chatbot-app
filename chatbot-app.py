# import libraries

import streamlit as st
from  nltk.chat.util import Chat ,reflections

background_image_url = "https://raw.githubusercontent.com/yaminigitacc/chatbot-app/main/chatbots.jpg"


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: top right;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# let's form pairs of patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["prakash created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['our customer service will reach you']
    ],
 ]   

# Streamlit UI setup
st.markdown(
    """
    <h1 style="background-color: #DCF8C6; color: black; text-align: center; margin-bottom: 20px;">Chatbot - The Clever Programmer</h1>
    """, 
    unsafe_allow_html=True
    
)
# #DCF8C6,#F0FFF0;
st.markdown("""
            <p style="font-size: 20px; background-color: white; color: black; text-align: center;">Hello! I am your chatbot assistant. You can type 'quit' to end the conversation</p>
            """,
             unsafe_allow_html=True
            )
#st.write("Hello! I am your chatbot assistant. You can type 'quit' to end the conversation.")

if "history" not in st.session_state:
    st.session_state.history = []
    
st.markdown(
    """
    <style>
    .stTextInput label {
        color: black;  
        font-family: 'Arial', sans-serif;  
        font-size: 18px;  
        font-weight: bold; 
        background-color: white;
        width: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# handle user input
user_input = st.text_input("You:", key="user_input")

# initialze chat with pairs and reflections
chat = Chat(pairs, reflections)

# function of bot response from user input
def get_bot_response(user_input):
    response = chat.respond(user_input)
    return response

if user_input:
    # Store user input in chat history
    st.session_state.history.append({"role": "user", "message": user_input})

    # Get bot response
    bot_response = get_bot_response(user_input)

    # Store bot response in chat history
    st.session_state.history.append({"role": "bot", "message": bot_response})


for chat_message in st.session_state.history:
    if chat_message["role"] == "user":
        st.markdown(f'<div style="text-align:right; background-color:#DCF8C6; border-radius:10px; padding:10px; max-width:100%; margin:10px 0;">{chat_message["message"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="text-align:left; background-color:#ECECEC; border-radius:10px; padding:10px; max-width:100%; margin:10px 0;">{chat_message["message"]}</div>', unsafe_allow_html=True)

# Option to quit the chat
if user_input == "quit":
    st.session_state.history.clear()
    st.write("Chat has ended. Thank you for chatting!")


