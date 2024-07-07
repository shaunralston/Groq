import os
import time
import groq

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = groq.Groq()

def test_groq_speed(prompt, model, num_runs=5):
    total_time = 0
    
    print(f"\nTesting model: {model}")
    print(f"Prompt: {prompt}\n")
    
    for i in range(num_runs):
        start_time = time.time()
        
        try:
            # Make a request to the Groq API
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            end_time = time.time()
            run_time = end_time - start_time
            total_time += run_time
            
            print(f"Run {i+1}: {run_time:.2f} seconds")
            print(f"Response: {completion.choices[0].message.content}\n")
        except groq.error.NotFoundError as e:
            print(f"Error: {e}")
            print("The specified model may not exist or you may not have access to it.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
    
    avg_time = total_time / num_runs
    print(f"Average time over {num_runs} runs: {avg_time:.2f} seconds")

def select_model():
    models = [
        "gemma2-9b-it",
        "gemma-7b-it",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]
    
    print("Available models:")
    for i, model in enumerate(models, 1):
        print(f"{i}. {model}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the model you want to test: "))
            if 1 <= choice <= len(models):
                return models[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_num_runs():
    while True:
        try:
            num_runs = int(input("Enter the number of runs to perform (default is 5): ") or "5")
            if num_runs > 0:
                return num_runs
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    model = select_model()
    num_runs = get_num_runs()
    prompt = "Explain the concept of quantum computing in one sentence."
    test_groq_speed(prompt, model, num_runs)