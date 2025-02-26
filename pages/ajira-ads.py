# import streamlit as st
# import streamlit.components.v1 as components

# # st.title("Welcome to AjiraLink Chatbot")

# # Embed the Dialogflow Messenger HTML code
# dialogflow_html = """
#     <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
#     <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>

#     <df-messenger
#         project-id="cool-kit-451607-u3"
#         agent-id="99a930b8-3d5b-4b8d-ad13-9b722a7fd36a"
#         language-code="en"
#         max-query-length="-1">
#         <df-messenger-chat-bubble chat-title="AjiraLink"></df-messenger-chat-bubble>
#     </df-messenger>

#     <style>
#         df-messenger {
#             z-index: 999;
#             position: fixed;
#             --df-messenger-font-color: #000;
#             --df-messenger-font-family: 'Google Sans', sans-serif;
#             --df-messenger-chat-background: #f3f6fc;
#             --df-messenger-message-user-background: #d3e3fd;
#             --df-messenger-message-bot-background: #fff;
#             bottom: 5px;
#             right: 5px;
#         }
#     </style>
# """

# # Display chatbot using Streamlit's components
# components.html(dialogflow_html, height=480, width=800)

# # st.write("Chat with **AjiraLink AI** for assistance!")
