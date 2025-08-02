'''
🤖 Simple Rule-Based ChatBot with Sentiment Analysis
    This is a basic Python chatbot built using rule-based pattern matching and sentiment analysis with the TextBlob library. 
    The bot can handle greetings, common questions, and uses sentiment to guide its responses when it doesn't recognize the input.

📋 Features:
    1.Responds to common greetings (like "hello", "good morning", etc.)
    2.Answers simple identity questions (like "what is your name?")
    3.Recognizes and replies to thanks or goodbyes
    4.Uses TextBlob to detect sentiment (positive/negative/neutral)
    5.Logs all conversations with timestamps to a chat_log.txt file
    6.Uses pattern matching with regular expressions (re) for keyword detection

🛠️ How it Works:
1.Input Cleaning:
    User input is cleaned (punctuation removed, converted to lowercase) for easier matching.

2.Pattern Matching:
    The bot checks if the input matches any known greeting or question pattern using regular expressions.

3.Sentiment Analysis:
    If no match is found, the bot uses TextBlob to analyze the sentiment:
    If positive → Gives a friendly default message
    If negative → Offers help or asks for rephrasing
    Otherwise → Chooses a fallback message

4.Logging:
    Every exchange (user input and bot response) is saved in chat_log.txt with a timestamp.

5.Exit Command:
    Type exit or quit to end the chat.

'''

from textblob import TextBlob
from datetime import datetime
import re
import string

class ChatBot:
    def __init__(self):
        """Initialize the chatbot with greeting patterns and responses"""
        self.greeting_patterns = [
            ('hello|hi|hey|greetings', ['Hello! How can I help you today?', 'Hi there!']),
            ('good morning', ['Good morning! How can I assist you?']),
            ('good afternoon', ['Good afternoon! What can I do for you?']),
            ('good evening', ['Good evening! How may I help you?']),
            ('how are you|how\'s it going', ['I\'m doing well, thank you!', 'All systems operational!']),
        ]
        
        self.qa_patterns = [
            ('what is your name|who are you', ['I\'m your AI assistant.', 'You can call me ChatBot.']),
            ('bye|goodbye|see you', ['Goodbye! Have a great day!', 'Farewell! Come back soon.']),
            ('thank you|thanks', ['You\'re welcome!', 'Happy to help!']),
        ]
        
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more.",
            "I'm still learning. Could you ask me something else?",
            "I didn't catch that. What else can I help with?"
        ]
        
        # Conversation log
        self.conversation_log = []
    
    def clean_input(self, text):
        """Clean and normalize user input"""
        text = text.lower().strip()
        text = re.sub(f'[{string.punctuation}]', '', text)
        return text
    
    def get_time_based_greeting(self):
        """Return appropriate greeting based on time of day"""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning!"
        elif 12 <= hour < 17:
            return "Good afternoon!"
        else:
            return "Good evening!"
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of user input"""
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    
    def find_response(self, user_input):
        """Find the most appropriate response based on user input"""
        cleaned_input = self.clean_input(user_input)
        
        # Check greeting patterns first
        for pattern, responses in self.greeting_patterns:
            if re.search(pattern, cleaned_input):
                return responses[0]
        
        # Check QA patterns
        for pattern, responses in self.qa_patterns:
            if re.search(pattern, cleaned_input):
                return responses[0]
        
        # If no pattern matches, use sentiment to guide default response
        sentiment = self.analyze_sentiment(user_input)
        if sentiment > 0.3:
            return "You sound positive! " + self.default_responses[1]
        elif sentiment < -0.3:
            return "I sense some frustration. " + self.default_responses[0]
        
        # Fallback to random default response
        return self.default_responses[len(cleaned_input) % len(self.default_responses)]
    
    def log_conversation(self, user_input, bot_response):
        """Log the conversation to memory and file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} - User: {user_input}\n{timestamp} - Bot: {bot_response}\n"
        self.conversation_log.append(entry)
        
        # Write to file
        with open("chat_log.txt", "a") as f:
            f.write(entry)
    
    def start_chat(self):
        """Main chat loop"""
        time_greeting = self.get_time_based_greeting()
        print(f"{time_greeting} I'm your AI assistant. Type 'exit' or 'quit' to end our conversation.")
        
        while True:
            user_input = input("User: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Bot: Goodbye! Have a great day!")
                self.log_conversation(user_input, "Goodbye! Have a great day!")
                break
                
            if not user_input:
                print("Bot: I didn't hear anything. Could you say that again?")
                continue
                
            response = self.find_response(user_input)
            print(f"Bot: {response}")
            self.log_conversation(user_input, response)

if __name__ == "__main__":
    bot = ChatBot()
    bot.start_chat()