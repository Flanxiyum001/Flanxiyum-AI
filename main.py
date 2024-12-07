import sqlite3
import subprocess
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
from transformers import pipeline
import random
import time

# SQLite Database Setup
db_path = "flanxiyum.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table to store user queries and AI responses (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_query TEXT,
    ai_response TEXT
)
''')
conn.commit()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Set up Speech Recognition
r = sr.Recognizer()

# Setup Hugging Face model for question-answering
nlp = pipeline("question-answering")

# Function to speak to the user
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            print(f"User said: {user_input}")
            return user_input.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the service.")
            return ""

# Function to store interactions in the SQLite database
def store_interaction(user_query, ai_response):
    cursor.execute("INSERT INTO interactions (user_query, ai_response) VALUES (?, ?)", (user_query, ai_response))
    conn.commit()

# Function to open apps by name
def open_app(app_name):
    app_paths = {
        "discord": r"C:\Users\pouru\AppData\Local\Discord\app-1.0.9014\Discord.exe",
        "spotify": r"C:\Users\pouru\AppData\Roaming\Spotify\Spotify.exe",
    }
    app_name = app_name.lower()
    
    # Check if app name is in the predefined dictionary
    if app_name in app_paths:
        try:
            subprocess.Popen([app_paths[app_name]])
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Sorry, I could not open {app_name}. Error: {str(e)}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")

# Function to handle different commands
def handle_command(command):
    if "open" in command:
        app_name = command.split("open")[-1].strip()
        open_app(app_name)
        store_interaction(command, f"Opening {app_name}")
    elif "play" in command:
        # Example: play music or a specific song
        song_name = command.split("play")[-1].strip()
        speak(f"Playing {song_name} on Spotify.")
        webbrowser.open(f"https://open.spotify.com/search/{song_name}")
        store_interaction(command, f"Playing {song_name} on Spotify")
    elif "search" in command:
        query = command.split("search")[-1].strip()
        search_query(query)
        store_interaction(command, f"Searching for {query}")
    else:
        # Answer questions using Hugging Face's pre-trained model
        context = "The quick brown fox jumps over the lazy dog."  # Placeholder context
        result = nlp({'question': command, 'context': context})
        answer = result['answer']
        speak(answer)
        store_interaction(command, answer)

# Function to perform a web search
def search_query(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Here are the search results for {query}.")

# Main Loop for Voice Commands
while True:
    print("How can I assist you?")
    speak("How can I assist you?")
    
    user_input = listen()
    
    if user_input:
        handle_command(user_input)
    
    # Optionally, add a delay to avoid continuous listening
    time.sleep(2)
