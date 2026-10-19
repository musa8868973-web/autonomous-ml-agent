from src.llm_brain import generate_ml_script

def run_pipeline(user_prompt):
    print(f"[Orchestrator] Planning the workflow for: '{user_prompt}'")
    
    # Step 1: Send the task to the LLM Brain
    generated_code = generate_ml_script(user_prompt)
    
    print("\n" + "="*40)
    print("🧠 GENERATED CODE PREVIEW")
    print("="*40)
    print(generated_code)
    print("="*40 + "\n")
    
    # Sandbox execution will be added here later
    return "Code generated successfully (Execution pending)"