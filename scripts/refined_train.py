import os
import sys
import gzip
import subprocess
import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForMaskedLM, DataCollatorForLanguageModeling, get_cosine_schedule_with_warmup
from datasets import load_dataset
from tqdm import tqdm

# PHASE 1: DATA VERIFICATION
output_file = "mushroom_genomes_massive.txt"
if not os.path.exists(output_file):
    print(f"⚠️ Training corpus '{output_file}' not found! Please run the massive harvester script first.")
    sys.exit(1)

# PHASE 2: INITIALIZING AI ARCHITECTURE
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "InstaDeepAI/nucleotide-transformer-v2-50m-multi-species"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForMaskedLM.from_pretrained(model_name, trust_remote_code=True)
model.to(device)

dataset = load_dataset("text", data_files={"train": output_file})
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=256)

tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)
train_dataloader = DataLoader(tokenized_datasets["train"], shuffle=True, batch_size=4, collate_fn=data_collator)

# PHASE 3: ADVANCED OPTIMIZATION MATH
optimizer = AdamW(model.parameters(), lr=5e-6, weight_decay=0.01)
num_training_steps = 50000 
lr_scheduler = get_cosine_schedule_with_warmup(optimizer=optimizer, num_warmup_steps=2000, num_training_steps=num_training_steps)

# PHASE 4: THE REFINED INFINITE LOOP
accumulation_steps = 16 
model.train()
epoch = 1
try:
    while True:
        progress_bar = tqdm(train_dataloader, desc=f"Epoch {epoch}", leave=True)
        for step, batch in enumerate(progress_bar):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss / accumulation_steps
            loss.backward()

            if (step + 1) % accumulation_steps == 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()
                lr_scheduler.step()
                optimizer.zero_grad()
            
            predictions = torch.argmax(outputs.logits, dim=-1)
            labels = batch["labels"]
            mask = labels != -100
            correct = (predictions[mask] == labels[mask]).sum().item()
            total = mask.sum().item()
            accuracy = (correct / total) * 100 if total > 0 else 0.0
            
            progress_bar.set_postfix({"Loss": f"{outputs.loss.item():.4f}", "Accuracy": f"{accuracy:.1f}%"})
        epoch += 1
except KeyboardInterrupt:
    print("\n\n🛑 TRAINING HALTED BY USER")

# PHASE 5: SAVE THE EXPERT AI
model.save_pretrained("./mushroom_ai_expert")
tokenizer.save_pretrained("./mushroom_ai_expert")
