from textblob import TextBlob
import colorama 
from colorama import Style, Fore 

print(f'{Fore.CYAN} Welcome to the Emotion Detector!{Style.RESET_ALL}')
name = input("Enter your name: ").strip() or 'Mystery Agent'
print(f"{Fore.GREEN}Hello, Agent {name}, nice to meet you.{Style.RESET_ALL}")

print(f'{Fore.YELLOW}Type reset, history or exit.{Style.RESET_ALL}')

history = []

while True:
    text = input(f"\n{Fore.CYAN} Enter a sentence to analyze: {Style.RESET_ALL}")

    if not text:
        print(f"{Fore.RED}Please enter a sentence.{Style.RESET_ALL}")
        continue
    if text.lower() == "exit":
        print(f"{Fore.MAGENTA}Goodbye agent {name}!{Style.RESET_ALL}")
        break
    if text.lower() == "reset":
        history.clear()
        print(f"{Fore.GREEN}History cleared.{Style.RESET_ALL}")
        continue
    if text.lower() == "history":
        for i, (polarity, emotion, text) in enumerate(history,1):
            color = Fore.GREEN if emotion == "Positive" else Fore.RED if emotion == "Negative" else Fore.YELLOW
            print(f"{color}{i}. {text}, Polarity: {polarity:.2f}, Emotion: {emotion}{Style.RESET_ALL}")
        if history == []:
            print(f"{Fore.YELLOW}History is empty.{Style.RESET_ALL}")
        continue

    polarity = TextBlob(text).sentiment.polarity
    emotion = ("Positive" if polarity> 0.25 else
               "Negative" if polarity< -0.25 else
               "Neutral")
    color = Fore.GREEN if emotion == "Positive" else Fore.RED if emotion == "Negative" else Fore.YELLOW
    print(f"{color}{text}, Polarity: {polarity:.2f}, Emotion: {emotion}{Style.RESET_ALL}")
    history.append((polarity, emotion, text))