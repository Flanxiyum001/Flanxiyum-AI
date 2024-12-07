import datetime
import webbrowser

def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {current_time}"
    elif "open" in command:
        if "google" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Google"
        else:
            return "I can only open Google for now."
    elif "how are you" in command:
        return "I am doing well, thank you for asking!"
    elif "exit" in command or "stop" in command:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."
