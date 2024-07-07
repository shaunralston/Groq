import os
import time
import groq
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = groq.Groq()

def print_header(text):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{text}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * len(text)}")

def print_model_name(model):
    print(f"\n{Fore.GREEN}{Style.BRIGHT}Testing model: {model}")

def print_result(run, time, response):
    print(f"{Fore.YELLOW}Run {run}: {time:.2f} seconds")
    print(f"{Fore.WHITE}Response: {response}")

def print_average(model, avg_time):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Average time for {model}: {avg_time:.2f} seconds")

def print_winner(winner, time):
    print(f"\n{Fore.RED}{Style.BRIGHT}🏆 The winner is: {winner} 🏆")
    print(f"{Fore.RED}{Style.BRIGHT}Fastest average time: {time:.2f} seconds")

def test_groq_speed(prompt, model, num_runs):
    total_time = 0
    
    print_model_name(model)
    
    for i in range(num_runs):
        start_time = time.time()
        
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            
            print_result(i+1, run_time, completion.choices[0].message.content)
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}")
            return None
    
    avg_time = total_time / num_runs
    print_average(model, avg_time)
    return avg_time

def main():
    models = [
        "gemma2-9b-it",
        "gemma-7b-it",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]
    
    print_header("Welcome to the Groq API Speed Test!")
    
    while True:
        try:
            num_runs = int(input(f"{Fore.CYAN}Enter the number of runs to perform for each model: "))
            if num_runs > 0:
                break
            else:
                print(f"{Fore.RED}Please enter a positive number.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.")
    
    prompt = "Explain the concept of quantum computing in one sentence."
    
    print_header(f"Testing all models with {num_runs} runs each")
    print(f"{Fore.WHITE}Prompt: {prompt}")
    
    results = {}
    for model in models:
        avg_time = test_groq_speed(prompt, model, num_runs)
        if avg_time is not None:
            results[model] = avg_time
    
    if results:
        winner = min(results, key=results.get)
        print_winner(winner, results[winner])
    else:
        print(f"{Fore.RED}No successful tests were completed.")

if __name__ == "__main__":
    main()