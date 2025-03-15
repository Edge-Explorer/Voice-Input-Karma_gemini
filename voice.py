import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate

print("Voice assistant activated. Say 'stop' to exit.")

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)  # Better noise adjustment
            print("Listening...")

            # Listen for user input with a timeout
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)

            try:
                text = recognizer.recognize_google(audio).lower()
                print("You said:", text)

                # Stop the program if user says "stop"
                if text == "stop":
                    print("Stopping program...")
                    engine.say("Goodbye!")
                    engine.runAndWait()
                    break

                # Voice feedback
                engine.say(f"You said {text}")
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Couldn't understand. Try again.")
                continue  # Go back to listening

            except sr.RequestError:
                print("Network error. Check your internet connection.")
                break  # Exit if API is unreachable

    except sr.WaitTimeoutError:
        print("No speech detected. Try again.")
        continue  # Keeps listening if no sound is detected

    except KeyboardInterrupt:
        print("\nExiting program...")
        break  # Gracefully exit on Ctrl+C

print("Program terminated.")
