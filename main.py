import os
from src.orchestrator import run_pipeline

def print_banner():
    print("="*50)
    print("🤖 Autonomous ML-Ops Agent Initialized")
    print("="*50)

def main():
    print_banner()
    print("[System] Ready to accept ReAct workflows.\n")
    
    user_prompt = input("Enter your ML task (e.g., 'Train YOLO on Roboflow dataset'): ")
    
    if not user_prompt.strip():
        print("[Error] Task cannot be empty. Exiting.")
        return

    print(f"\n[System] Routing to Orchestrator...")
    
    # Core engine ko call kar rahe hain
    result = run_pipeline(user_prompt)
    
    print(f"\n[System] Execution Finished: {result}")

if __name__ == "__main__":
    main()