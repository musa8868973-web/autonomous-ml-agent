import os

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

    print(f"\n[Orchestrator] Received task: {user_prompt}")
    print("[Orchestrator] Routing to Groq Brain... (Logic pending)")
    
    # TODO: Pass this prompt to src.orchestrator

if __name__ == "__main__":
    main()