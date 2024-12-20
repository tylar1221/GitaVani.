
---

# GitaVani - The Voice of the Gita 🌟  

GitaVani is an AI-powered chatbot designed to share the timeless wisdom of the *Bhagavad Gita*. It provides personalized spiritual guidance, motivational insights, and context-specific advice, all inspired by Krishna's teachings.

---

## 🌟 Features  
- **Interactive Chat**: Users can share their challenges and receive wisdom from the *Bhagavad Gita*.  
- **Contextual Responses**: Answers tailored to users' queries with relevant verses and their explanations.  
- **Past Conversations**: Easily revisit previous chats through the sidebar.  
- **Streamlit Interface**: Simple and elegant web app for a seamless user experience.  
- **Gemini AI Integration**: Powered by Google's generative AI model for insightful conversations.  
- **Persistent Chat History**: Save and retrieve past chats with Joblib for continuity.

---

## 🛠️ Tech Stack  
- **Frontend**: [Streamlit](https://streamlit.io/) for creating an intuitive web interface.  
- **Backend**: Python with the Google Gemini API for conversational AI.  
- **Database**: Local storage using Joblib to manage past chats and history.  
- **Environment Management**: dotenv for secure API key handling.  

---

## 🚀 Getting Started  

### Prerequisites  
1. Python 3.7 or above.  
2. Google Gemini API Key.  
3. Required Python libraries:  
   - `streamlit`  
   - `google-generativeai`  
   - `joblib`  
   - `python-dotenv`  

### Installation  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/your-username/gita-chatbot.git  
   cd gita-chatbot  
   ```  

2. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Set Up Environment Variables**  
   Create a `.env` file in the project directory with:  
   ```env  
   GOOGLE_API_KEY=your_google_api_key  
   ```  

4. **Run the Application**  
   ```bash  
   streamlit run app.py  
   ```  

5. **Access the Chatbot**  
   Open your browser and go to `http://localhost:8501`.

---

## 📖 How It Works  

1. **Pre-Prompt Setup**  
   The chatbot is pre-configured to emulate the teachings of Lord Krishna. It interprets queries and provides insights rooted in the *Bhagavad Gita*.  

2. **Chat Interface**  
   - Enter your query in the input box.  
   - View AI-generated responses, complete with Sanskrit verses, translations, and explanations.  
   - Chat history is saved for reference.  

3. **Past Chats**  
   Access past conversations via the sidebar for a seamless experience.  

---


## Upcoming Features

### 1. Text-to-Speech (TTS)
- Hear responses in a divine voice for an immersive experience.  
- Enhances accessibility for visually impaired users.

### 2. Speech-to-Text (STT)
- Interact using voice commands for hands-free use.  
- Ideal for users with physical disabilities.

### 3. Multilingual Support
- Chat in your preferred language with dynamic translations.  
- Expands accessibility to regional language speakers.

### 4. Personalized Insights
- Tailored responses based on user preferences and challenges.  
- Saves preferences for a customized experience.

### 5. UI Enhancements
- Audio playback controls, dark mode, and font adjustments.  
- Interactive widgets for Sanskrit verses and explanations.

These features will make **GitaVani** more accessible, intuitive, and engaging for all users.

---  

