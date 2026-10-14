from textblob import TextBlob

print('Welcome to the Emotion Detector!')
name = input("Enter your name: ").strip() or 'Mystery Agent'
print(f"Hello, Agent {name}, nice to meet you.")

print('Type reset, history or exit.')

history = []

while True:
    text = input("\n Enter a sentence to analyze: ")

    if not text:
        print("Please enter a sentence.")
        continue
    if text.lower() == "exit":
        print(f"Goodbye agent {name}!")
        break
    if text.lower() == "reset":
        history.clear()
        print("History cleared.")
        continue
    if text.lower() == "history":
        for i, (polarity, emotion, text) in enumerate(history,1):
            print(f"{i}. {text}, Polarity: {polarity:.2f}, Emotion: {emotion}")
        if history == []:
            print("History is empty.")
        continue

    polarity = TextBlob(text).sentiment.polarity
    emotion = ("Positive" if polarity> 0.25 else
               "Negative" if polarity< -0.25 else
               "Neutral")
    print(f"{text}, Polarity: {polarity:.2f}, Emotion: {emotion}")
    history.append((polarity, emotion, text))

    