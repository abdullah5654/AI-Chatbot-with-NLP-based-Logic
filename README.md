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
