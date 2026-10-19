import subprocess
import os

WORKSPACE_DIR = "workspace"

def execute_script(script_content, filename="generated_script.py"):
    print("[Sandbox] Preparing to execute AI generated code...")
    
    # Workspace folder ensure karna
    if not os.path.exists(WORKSPACE_DIR):
        os.makedirs(WORKSPACE_DIR)
        
    filepath = os.path.join(WORKSPACE_DIR, filename)
    
    # AI ka code file mein save karna
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(script_content)
        
    # Subprocess ke zariye code run karna
    try:
        print(f"[Sandbox] Running {filepath}...\n")
        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True,
            timeout=60  # 60 seconds max execution time
        )
        
        # Agar code successfully chal gaya
        if result.returncode == 0:
            print("[Sandbox] Execution Successful!")
            return {"status": "success", "output": result.stdout, "error": None}
        
        # Agar code mein error aaya (yeh self-healing ke liye zaroori hai)
        else:
            print("[Sandbox] Execution Failed! Error caught.")
            return {"status": "error", "output": result.stdout, "error": result.stderr}
            
    except Exception as e:
        return {"status": "error", "output": "", "error": str(e)}