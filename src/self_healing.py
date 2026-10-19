from src.llm_brain import generate_ml_script

def fix_code(original_code, error_message):
    print("\n[Self-Healing] Analyzing the error and fixing the code...")
    
    # Prompt engineering for error correction
    healing_prompt = f"""
    You are an expert ML-Ops AI. The following Python code encountered an error during execution.
    
    Original Code:
    {original_code}
    
    Error Message:
    {error_message}
    
    Analyze the error and provide ONLY the corrected raw python code. 
    Do NOT include markdown formatting (like ```python) or any explanations.
    """
    
    # LLM ko purana code aur error bhej kar naya code mangwana
    fixed_code = generate_ml_script(healing_prompt)
    
    return fixed_code