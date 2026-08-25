import os
import sys
import gzip
import subprocess
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
from safetensors.torch import load_file

def harvest_genomes():
    print("✅ Genomes are already downloaded and formatted! Skipping harvest.")

def initialize_ai():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    base_model_name = "InstaDeepAI/nucleotide-transformer-v2-50m-multi-species"
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    model = AutoModelForMaskedLM.from_pretrained(base_model_name, trust_remote_code=True)
    
    model.load_state_dict(load_file("./mushroom_ai_expert/model.safetensors"))
    model.eval()
    model.to(device)
    return tokenizer, model, device

def scan_custom_dna(tokenizer, model, device):
    print("Please paste your raw DNA sequence below (press Enter, type 'SCAN', and press Enter again to start):")
    
    user_input_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'SCAN':
            break
        user_input_lines.append(line)
        
    raw_dna = "".join(user_input_lines).replace("\n", "").replace(" ", "").upper()
    clean_dna = "".join([char for char in raw_dna if char in "ATCG"])
    
    if len(clean_dna) < 10: return

    ERROR_THRESHOLD = 0.10
    WINDOW_SIZE = 64 
    
    inputs = tokenizer(clean_dna, return_tensors="pt", truncation=False)
    input_ids = inputs["input_ids"][0].tolist()
    total_tokens = len(input_ids)
    
    anomalies = []
    
    for i in range(1, total_tokens - 1):
        if i % 10 == 0 or i == total_tokens - 2:
            percent = (i / (total_tokens - 2)) * 100
            sys.stdout.write(f"\rScanning... [{percent:.1f}%]")
            sys.stdout.flush()

        start_idx = max(1, i - (WINDOW_SIZE // 2))
        end_idx = min(total_tokens - 1, i + (WINDOW_SIZE // 2))
        window_tokens = input_ids[start_idx:end_idx]
        local_target_idx = i - start_idx 
        true_token = window_tokens[local_target_idx]
        
        masked_tokens = window_tokens.copy()
        masked_tokens[local_target_idx] = tokenizer.mask_token_id
        tensor_inputs = torch.tensor([masked_tokens]).to(device)
        
        with torch.no_grad():
            outputs = model(tensor_inputs)
            logits = outputs.logits[0, local_target_idx, :]
            probabilities = torch.nn.functional.softmax(logits, dim=-1)
            true_token_prob = probabilities[true_token].item()
            
            if true_token_prob < ERROR_THRESHOLD:
                top_predicted_token = torch.argmax(probabilities).item()
                anomalies.append({
                    "position": i,
                    "original_dna": tokenizer.decode([true_token]).replace(" ", ""),
                    "ai_suggestion": tokenizer.decode([top_predicted_token]).replace(" ", ""),
                    "confidence": true_token_prob
                })

    print("\n\n📊 FINAL SYNTAX REPORT")
    if len(anomalies) == 0:
        print("✅ SUCCESS! 0 Syntax Errors Found.")
    else:
        print(f"⚠️ FOUND {len(anomalies)} POTENTIAL ANOMALIES\n")
        for error in anomalies[:15]:
            print(f"Junction Token {error['position']}: '{error['original_dna']}' (Natural Prob: {error['confidence']*100:.1f}%)")
        if len(anomalies) > 15: print(f"...and {len(anomalies) - 15} more warnings expected in synthetic parts.")

if __name__ == "__main__":
    harvest_genomes()
    ai_tokenizer, ai_model, compute_device = initialize_ai()
    scan_custom_dna(ai_tokenizer, ai_model, compute_device)
