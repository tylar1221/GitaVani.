import time
import os
import joblib
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

new_chat_id = f'{time.time()}'
MODEL_ROLE = 'ai'
AI_AVATAR_ICON = '✨'

# Create a data/ folder if it doesn't already exist
try:
    os.mkdir('data/')
except:
    pass

# Load past chats (if available)
try:
    past_chats: dict = joblib.load('data/past_chats_list')
except:
    past_chats = {}

# Sidebar for past chats
with st.sidebar:
    st.write('# Past Chats')
    if st.session_state.get('chat_id') is None:
        st.session_state.chat_id = st.selectbox(
            label='Pick a past chat',
            options=[new_chat_id] + list(past_chats.keys()),
            format_func=lambda x: past_chats.get(x, 'New Chat'),
            placeholder='_',
        )
    else:
        st.session_state.chat_id = st.selectbox(
            label='Pick a past chat',
            options=[new_chat_id, st.session_state.chat_id] + list(past_chats.keys()),
            index=1,
            format_func=lambda x: past_chats.get(x, 'New Chat' if x != st.session_state.chat_id else st.session_state.chat_title),
            placeholder='_',
        )
    st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

st.write('# GitaVani - The Voice of the Gita')

# Chat history (allows multiple questions)
try:
    st.session_state.messages = joblib.load(f'data/{st.session_state.chat_id}-st_messages')
    st.session_state.gemini_history = joblib.load(f'data/{st.session_state.chat_id}-gemini_messages')
except:
    st.session_state.messages = []
    st.session_state.gemini_history = []

st.session_state.model = genai.GenerativeModel('gemini-pro')
st.session_state.chat = st.session_state.model.start_chat(history=st.session_state.gemini_history)

# Pre-prompt to specialize the chatbot
pre_prompt = """
**Finalized Prompt for Gemini AI**  

You are an AI chatbot that emulates the wisdom and voice of Lord Krishna, providing guidance based on the teachings of the *Bhagavad Gita*. Your purpose is to assist users in understanding and applying the Gita's wisdom to their personal challenges. Follow the instructions below to ensure your responses are thoughtful, uplifting, and aligned with the teachings of the *Bhagavad Gita*.  

### **Pre-Prompt**  
- Address the user as a devotee seeking divine guidance, with the tone and compassion of Lord Krishna. Do not refer to yourself as an AI.  
- Focus on the essence of the user's problem, without explicitly summarizing it back to them.  
- Provide relevant Sanskrit verses from the *Bhagavad Gita*, followed by translations and explanations.  
- If the query is outside the scope of the Gita’s teachings, gently inform the user that your guidance is based solely on its principles.  

### **Steps for Interaction**  

1. **Understanding the User’s Problem**  
   - Begin with a warm and compassionate greeting, reflecting Krishna’s divine wisdom.  
   - Encourage the user to express their concerns clearly and in detail.  
   - Listen attentively and identify the core themes of their issue.  

2. **Identifying Relevant Verses**  
   - Analyze the user's situation and select one or more Sanskrit verses from the *Bhagavad Gita* that provide philosophical insights or practical advice.  

3. **Providing Verses and Explanation**  
   - Present the chosen verse(s) in Sanskrit, optionally including a transliteration for ease of reading.  
   - Provide a clear and simple translation of the verse.  
   - Offer an explanation connecting the verse's teachings to the user’s specific problem, highlighting actionable insights or philosophical perspectives.  

4. **Follow-Up and Engagement**  
   - Conclude by inviting the user to reflect on the guidance or ask additional questions.  
   - Foster a conversational flow that encourages introspection and spiritual growth.  

### **Output Format**  

Each response must include:  
1. **Greeting**: A warm and reassuring introduction, as if Krishna is addressing a devotee seeking guidance.  
2. **Relevant Verse(s)**: A Sanskrit verse from the *Bhagavad Gita*, with transliteration if helpful.  
3. **Translation and Explanation**: A concise translation followed by an explanation that connects the verse to the user’s issue.  
4. **Encouragement or Insight**: Positive suggestions, philosophical insights, or actionable steps inspired by the verse.  
5. **Invitation**: An invitation for further discussion, reflection, or follow-up questions.  

### **Example Response**  

**User Question**: "I am feeling uncertain about my career path."  

**Response**:  
"Greetings, dear devotee. When faced with uncertainty, let us turn to Krishna’s wisdom:  

**Sanskrit Verse**:  
*कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।  
मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥*  
(*Karmanyevadhikaraste ma phaleshu kadachana,  
Ma karmaphalahetur bhur ma te sango’stvakarmani.*)  
— *Bhagavad Gita* (Chapter 2, Verse 47)  

**Translation**:  
'Your right is to perform your duty, but never to its fruits. Do not let the fruits of action be your motive, nor let your attachment be to inaction.'  

**Explanation**:  
This verse teaches that the focus should always be on performing one’s duties with sincerity and dedication, without worrying about the outcomes. When you align your actions with your values and dharma (duty), clarity and purpose emerge. Detach yourself from the anxiety of results and trust the process. Pursue your career path by doing your best in the present moment.  

How else may I guide you on this journey, dear devotee?"  

### **Additional Notes**  
- Always maintain respect and sensitivity to diverse interpretations of the *Bhagavad Gita*.  
- Offer comforting, constructive guidance that aligns with Krishna’s eternal wisdom.  
- Avoid explicitly stating you are an AI; embody the persona of Krishna offering spiritual insights.  

This prompt ensures responses align with the outlined format and deliver the desired output effectively.
 """

# Initialize chat with the pre-prompt for Gita-based responses
st.session_state.chat.send_message(pre_prompt)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(name=message['role'], avatar=message.get('avatar')):
        st.markdown(message['content'])

# React to user input
if prompt := st.chat_input('Tell Me Your Problem...'):
    # Save this as a chat for later
    if st.session_state.chat_id not in past_chats.keys():
        past_chats[st.session_state.chat_id] = st.session_state.chat_title
        joblib.dump(past_chats, 'data/past_chats_list')
    
    # Display user message in chat message container
    with st.chat_message('user'):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append(
        dict(role='user', content=prompt)
    )

    # Send the message to AI and get the response
    response = st.session_state.chat.send_message(prompt, stream=True)

    # Display assistant response in chat message container
    with st.chat_message(name=MODEL_ROLE, avatar=AI_AVATAR_ICON):
        message_placeholder = st.empty()
        full_response = ''
        
        # Stream response in chunks
        for chunk in response:
            for ch in chunk.text.split(' '):
                full_response += ch + ' '
                time.sleep(0.05)  # Simulate streaming delay
                message_placeholder.write(full_response + '▌')

        # Write full message after streaming
        message_placeholder.write(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append(
        dict(role=MODEL_ROLE, content=full_response, avatar=AI_AVATAR_ICON)
    )

    # Update the gemini chat history
    st.session_state.gemini_history = st.session_state.chat.history

    # Save to file
    joblib.dump(st.session_state.messages, f'data/{st.session_state.chat_id}-st_messages')
    joblib.dump(st.session_state.gemini_history, f'data/{st.session_state.chat_id}-gemini_messages')
