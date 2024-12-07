import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:  # Automatically uses the default microphone
            print("Adjusting for background noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=10)
            print("Listening... Speak now.")
            audio = recognizer.listen(source, timeout=10)  # Increased timeout to 10 seconds
            print("Audio captured successfully.")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.WaitTimeoutError:
        print("Listening timed out. Please try again.")
    except sr.RequestError as e:
        print(f"Could not connect to the speech recognition service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

listen()
