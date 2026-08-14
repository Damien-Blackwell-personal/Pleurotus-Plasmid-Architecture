# 12 august 2026
#
#
{please read}  this documentation uses open source ai and dependencies, i respect that i may not be able to list all of the 'moving parts' that make this work....
#
#
# ex: this research is into fungal genomics and contributes to personal synthetic fungal plasmid designing.
#
#
#
#
## ex: 1st piece of code, (installs dependencies)
#
#
#
### ///pip install torch transformers datasets multimolecule ncbi-genome-download
#
#
#
## ex: I will be using the pre-trained DNABERT-2 as my base GLM and training it to learn the DNA syntax of Pluerotus Ostreatus and of Nionothopanus Nambi.
#
#
#
#
# ex: installed dependencies...
#
#
#
Defaulting to user installation because normal site-packages is not writeable
Collecting torch
  Downloading torch-2.8.0-cp39-none-macosx_11_0_arm64.whl.metadata (30 kB)
Collecting transformers
  Downloading transformers-4.57.6-py3-none-any.whl.metadata (43 kB)
Collecting datasets
  Downloading datasets-4.5.0-py3-none-any.whl.metadata (19 kB)
Collecting multimolecule
  Downloading multimolecule-0.0.8-py3-none-any.whl.metadata (44 kB)
Requirement already satisfied: filelock in ./Library/Python/3.9/lib/python/site-packages (from torch) (3.19.1)
Requirement already satisfied: typing-extensions>=4.10.0 in ./Library/Python/3.9/lib/python/site-packages (from torch) (4.15.0)
Requirement already satisfied: sympy>=1.13.3 in ./Library/Python/3.9/lib/python/site-packages (from torch) (1.14.0)
Collecting networkx (from torch)
  Downloading networkx-3.2.1-py3-none-any.whl.metadata (5.2 kB)
Requirement already satisfied: jinja2 in ./Library/Python/3.9/lib/python/site-packages (from torch) (3.1.6)
Requirement already satisfied: fsspec in ./Library/Python/3.9/lib/python/site-packages (from torch) (2025.10.0)
Collecting huggingface-hub<1.0,>=0.34.0 (from transformers)
  Downloading huggingface_hub-0.36.2-py3-none-any.whl.metadata (15 kB)
Requirement already satisfied: numpy>=1.17 in ./Library/Python/3.9/lib/python/site-packages (from transformers) (2.0.2)
Requirement already satisfied: packaging>=20.0 in ./Library/Python/3.9/lib/python/site-packages (from transformers) (25.0)
Requirement already satisfied: pyyaml>=5.1 in ./Library/Python/3.9/lib/python/site-packages (from transformers) (6.0.3)
Collecting regex!=2019.12.17 (from transformers)
  Downloading regex-2026.1.15-cp39-cp39-macosx_11_0_arm64.whl.metadata (40 kB)
Requirement already satisfied: requests in ./Library/Python/3.9/lib/python/site-packages (from transformers) (2.32.5)
Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in ./Library/Python/3.9/lib/python/site-packages (from transformers) (0.22.2)
Collecting safetensors>=0.4.3 (from transformers)
  Downloading safetensors-0.7.0-cp38-abi3-macosx_11_0_arm64.whl.metadata (4.1 kB)
Requirement already satisfied: tqdm>=4.27 in ./Library/Python/3.9/lib/python/site-packages (from transformers) (4.67.1)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in ./Library/Python/3.9/lib/python/site-packages (from huggingface-hub<1.0,>=0.34.0->transformers) (1.2.0)
Requirement already satisfied: pyarrow>=21.0.0 in ./Library/Python/3.9/lib/python/site-packages (from datasets) (21.0.0)
Collecting dill<0.4.1,>=0.3.0 (from datasets)
  Downloading dill-0.4.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: pandas in ./Library/Python/3.9/lib/python/site-packages (from datasets) (2.3.3)
Requirement already satisfied: httpx<1.0.0 in ./Library/Python/3.9/lib/python/site-packages (from datasets) (0.28.1)
Collecting xxhash (from datasets)
  Downloading xxhash-3.8.1-cp39-cp39-macosx_11_0_arm64.whl.metadata (15 kB)
Collecting multiprocess<0.70.19 (from datasets)
  Downloading multiprocess-0.70.18-py39-none-any.whl.metadata (7.5 kB)
Requirement already satisfied: aiohttp!=4.0.0a0,!=4.0.0a1 in ./Library/Python/3.9/lib/python/site-packages (from fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (3.13.3)
Requirement already satisfied: anyio in ./Library/Python/3.9/lib/python/site-packages (from httpx<1.0.0->datasets) (4.12.1)
Requirement already satisfied: certifi in ./Library/Python/3.9/lib/python/site-packages (from httpx<1.0.0->datasets) (2026.1.4)
Requirement already satisfied: httpcore==1.* in ./Library/Python/3.9/lib/python/site-packages (from httpx<1.0.0->datasets) (1.0.9)
Requirement already satisfied: idna in ./Library/Python/3.9/lib/python/site-packages (from httpx<1.0.0->datasets) (3.11)
Requirement already satisfied: h11>=0.16 in ./Library/Python/3.9/lib/python/site-packages (from httpcore==1.*->httpx<1.0.0->datasets) (0.16.0)
Collecting accelerate (from multimolecule)
  Downloading accelerate-1.10.1-py3-none-any.whl.metadata (19 kB)
Collecting chanfig>=0.0.105 (from multimolecule)
  Downloading chanfig-0.0.117-py3-none-any.whl.metadata (14 kB)
Collecting danling>=0.3.11 (from danling[torch]>=0.3.11->multimolecule)
  Downloading danling-0.4.0-py3-none-any.whl.metadata (4.2 kB)
Collecting strenum (from multimolecule)
  Downloading StrEnum-0.4.15-py3-none-any.whl.metadata (5.3 kB)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (2.6.1)
Requirement already satisfied: aiosignal>=1.4.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.4.0)
Requirement already satisfied: async-timeout<6.0,>=4.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (5.0.1)
Requirement already satisfied: attrs>=17.3.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (25.4.0)
Requirement already satisfied: frozenlist>=1.1.1 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.8.0)
Requirement already satisfied: multidict<7.0,>=4.5 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (6.7.0)
Requirement already satisfied: propcache>=0.2.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (0.4.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in ./Library/Python/3.9/lib/python/site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2025.10.0,>=2023.1.0->datasets) (1.22.0)
Collecting lazy-imports (from chanfig>=0.0.105->multimolecule)
  Downloading lazy_imports-1.1.0-py3-none-any.whl.metadata (11 kB)
Collecting tomli (from chanfig>=0.0.105->multimolecule)
  Downloading tomli-2.4.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: gitpython in ./Library/Python/3.9/lib/python/site-packages (from danling>=0.3.11->danling[torch]>=0.3.11->multimolecule) (3.1.50)
Collecting torchdata (from danling>=0.3.11->danling[torch]>=0.3.11->multimolecule)
  Downloading torchdata-0.11.0-py3-none-any.whl.metadata (6.3 kB)
Collecting torchmetrics (from danling[torch]>=0.3.11->multimolecule)
  Downloading torchmetrics-1.8.2-py3-none-any.whl.metadata (22 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in ./Library/Python/3.9/lib/python/site-packages (from requests->transformers) (3.4.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./Library/Python/3.9/lib/python/site-packages (from requests->transformers) (2.6.3)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./Library/Python/3.9/lib/python/site-packages (from sympy>=1.13.3->torch) (1.3.0)
Collecting psutil (from accelerate->multimolecule)
  Downloading psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)
Requirement already satisfied: exceptiongroup>=1.0.2 in ./Library/Python/3.9/lib/python/site-packages (from anyio->httpx<1.0.0->datasets) (1.3.1)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./Library/Python/3.9/lib/python/site-packages (from gitpython->danling>=0.3.11->danling[torch]>=0.3.11->multimolecule) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in ./Library/Python/3.9/lib/python/site-packages (from gitdb<5,>=4.0.1->gitpython->danling>=0.3.11->danling[torch]>=0.3.11->multimolecule) (5.0.3)
Requirement already satisfied: MarkupSafe>=2.0 in ./Library/Python/3.9/lib/python/site-packages (from jinja2->torch) (3.0.3)
Requirement already satisfied: python-dateutil>=2.8.2 in ./Library/Python/3.9/lib/python/site-packages (from pandas->datasets) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./Library/Python/3.9/lib/python/site-packages (from pandas->datasets) (2026.2)
Requirement already satisfied: tzdata>=2022.7 in ./Library/Python/3.9/lib/python/site-packages (from pandas->datasets) (2026.2)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas->datasets) (1.15.0)
Collecting lightning-utilities>=0.8.0 (from torchmetrics->danling[torch]>=0.3.11->multimolecule)
  Downloading lightning_utilities-0.15.2-py3-none-any.whl.metadata (5.7 kB)
Requirement already satisfied: setuptools in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from lightning-utilities>=0.8.0->torchmetrics->danling[torch]>=0.3.11->multimolecule) (58.0.4)
Downloading torch-2.8.0-cp39-none-macosx_11_0_arm64.whl (73.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.6/73.6 MB 4.0 MB/s  0:00:18
Downloading transformers-4.57.6-py3-none-any.whl (12.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.0/12.0 MB 2.7 MB/s  0:00:04
Downloading huggingface_hub-0.36.2-py3-none-any.whl (566 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 566.4/566.4 kB 6.1 MB/s  0:00:00
Downloading datasets-4.5.0-py3-none-any.whl (515 kB)
Downloading dill-0.4.0-py3-none-any.whl (119 kB)
Downloading multiprocess-0.70.18-py39-none-any.whl (133 kB)
Downloading multimolecule-0.0.8-py3-none-any.whl (487 kB)
Downloading chanfig-0.0.117-py3-none-any.whl (63 kB)
Downloading danling-0.4.0-py3-none-any.whl (429 kB)
Downloading regex-2026.1.15-cp39-cp39-macosx_11_0_arm64.whl (288 kB)
Downloading safetensors-0.7.0-cp38-abi3-macosx_11_0_arm64.whl (447 kB)
Downloading accelerate-1.10.1-py3-none-any.whl (374 kB)
Downloading lazy_imports-1.1.0-py3-none-any.whl (18 kB)
Downloading networkx-3.2.1-py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 3.3 MB/s  0:00:00
Downloading psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl (129 kB)
Downloading StrEnum-0.4.15-py3-none-any.whl (8.9 kB)
Downloading tomli-2.4.1-py3-none-any.whl (14 kB)
Downloading torchdata-0.11.0-py3-none-any.whl (61 kB)
Downloading torchmetrics-1.8.2-py3-none-any.whl (983 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 983.2/983.2 kB 1.2 MB/s  0:00:00
Downloading lightning_utilities-0.15.2-py3-none-any.whl (29 kB)
Downloading xxhash-3.8.1-cp39-cp39-macosx_11_0_arm64.whl (32 kB)
Installing collected packages: strenum, xxhash, tomli, safetensors, regex, psutil, networkx, lightning-utilities, lazy-imports, dill, torch, multiprocess, huggingface-hub, chanfig, torchmetrics, torchdata, accelerate, transformers, danling, datasets, multimolecule
   ━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━━━━━ 10/21 [torch]  WARNING: The scripts torchfrtrace and torchrun are installed in '/Users/classified/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: huggingface-hub
    Found existing installation: huggingface_hub 1.3.4
    Uninstalling huggingface_hub-1.3.4:
      Successfully uninstalled huggingface_hub-1.3.4
   ━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━━━━━ 12/21 [huggingface-hub]  WARNING: The scripts hf, huggingface-cli and tiny-agents are installed in '/Users/classified/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━ 16/21 [accelerate]  WARNING: The scripts accelerate, accelerate-config, accelerate-estimate-memory, accelerate-launch and accelerate-merge-weights are installed in '/Users/damo/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━ 17/21 [transformers]  WARNING: The scripts transformers and transformers-cli are installed in '/Users/damo/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━ 19/21 [datasets]  WARNING: The script datasets-cli is installed in '/Users/classified/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed accelerate-1.10.1 chanfig-0.0.117 danling-0.4.0 datasets-4.5.0 dill-0.4.0 huggingface-hub-0.36.2 lazy-imports-1.1.0 lightning-utilities-0.15.2 multimolecule-0.0.8 multiprocess-0.70.18 networkx-3.2.1 psutil-7.2.2 regex-2026.1.15 safetensors-0.7.0 strenum-0.4.15 tomli-2.4.1 torch-2.8.0 torchdata-0.11.0 torchmetrics-1.8.2 transformers-4.57.6 xxhash-3.8.1

 ## ex: so that successfully ran in my terminal and installed the necessary libraries and dependencies in order to continue.

 # ex: credit where credit is due to my coding assistant gemini and to the repositories used to achieve the genomic data from the 2 mushroom species 
 #
///nano bioscanner_pipeline.py
#
## ex: The following python script sets up the environment and allows the ai to read and train upon the inputted data
#
#
///import os
import sys
import gzip
import subprocess
import torch
import multimolecule # Required to load DNABERT-2 architecture
from transformers import AutoTokenizer, AutoModelForMaskedLM

# ==========================================
# PHASE 1: AUTOMATED DATA HARVESTER
# ==========================================
def harvest_genomes():
    print("\n" + "="*50)
    print("🌍 PHASE 1: FETCHING REFERENCE GENOMES FROM NCBI")
    print("="*50)
    
    # Run the NCBI downloader tool for our specific fungi in FASTA format
    download_cmd = [
        "ncbi-genome-download", 
        "--genera", "Pleurotus ostreatus,Neonothopanus nambi", 
        "--formats", "fasta", 
        "fungi"
    ]
    
    try:
        print("Connecting to NCBI FTP servers... (This may take a moment)")
        subprocess.run(download_cmd, check=True)
        print("✅ Genomes downloaded successfully.")
    except Exception as e:
        print(f"⚠️ NCBI Download failed (you might need to check your internet connection): {e}")
        print("Continuing pipeline without updating local reference files...")

    # Clean and merge the downloaded zipped FASTA files into one text file
    output_file = "mushroom_genomes.txt"
    if os.path.exists("./genbank/fungi") or os.path.exists("./refseq/fungi"):
        print("Extracting and formatting raw DNA...")
        with open(output_file, 'w') as outfile:
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file.endswith(".fna.gz"):
                        filepath = os.path.join(root, file)
                        with gzip.open(filepath, 'rt') as zipped_fasta:
                            for line in zipped_fasta:
                                # Strip headers so only pure A,T,C,G remains
                                if not line.startswith(">"):
                                    outfile.write(line.strip())
        print(f"✅ Formatted training corpus saved as '{output_file}'.")
    else:
        print("No new genomes found to format.")

# ==========================================
# PHASE 2: AI INITIALIZATION
# ==========================================
def initialize_ai():
    print("\n" + "="*50)
    print("🧠 PHASE 2: INITIALIZING GENOMIC AI")
    print("="*50)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Hardware allocated: {device.type.upper()}")
    print("Loading DNABERT-2 Model...")
    
    # We load the base model here for immediate scanning. 
    # (If you run the 3-hour fine-tuning process later, you would point this to your local folder)
    model_name = "multimolecule/dnabert2"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForMaskedLM.from_pretrained(model_name, trust_remote_code=True)
    model.eval()
    model.to(device)
    
    print("✅ AI loaded and ready.")
    return tokenizer, model, device

# ==========================================
# PHASE 3: INTERACTIVE SEQUENCE SCANNER
# ==========================================
def scan_custom_dna(tokenizer, model, device):
    print("\n" + "="*50)
    print("🧬 PHASE 3: PLASMID SYNTAX SCANNER")
    print("="*50)
    
    # The interactive terminal prompt!
    print("Please paste your raw DNA sequence below (press Enter, type 'SCAN', and press Enter again to start):")
    
    user_input_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'SCAN':
            break
        user_input_lines.append(line)
        
    # Clean the pasted input (removes accidental FASTA headers, spaces, and numbers)
    raw_dna = "".join(user_input_lines).replace("\n", "").replace(" ", "").upper()
    # Filter out anything that isn't a standard nucleotide
    clean_dna = "".join([char for char in raw_dna if char in "ATCG"])
    
    if len(clean_dna) < 10:
        print("\n⚠️ Error: DNA sequence is too short or invalid.")
        return

    print(f"\nProcessing {len(clean_dna)} base pairs...")
    
    # Scanning parameters
    ERROR_THRESHOLD = 0.10
    WINDOW_SIZE = 64 
    
    inputs = tokenizer(clean_dna, return_tensors="pt", truncation=False)
    input_ids = inputs["input_ids"][0].tolist()
    total_tokens = len(input_ids)
    
    anomalies = []
    print("Initializing sliding window analysis...")
    
    for i in range(1, total_tokens - 1):
        # Progress tracker
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

    # The Final Report
    print("\n\n" + "="*50)
    print("📊 FINAL SYNTAX REPORT")
    print("="*50)

    if len(anomalies) == 0:
        print("✅ SUCCESS! 0 Syntax Errors Found.")
        print("Your synthetic construct matches natural biological patterns flawlessly.")
    else:
        print(f"⚠️ FOUND {len(anomalies)} POTENTIAL ANOMALIES\n")
        for error in anomalies:
            print(f"Junction Token {error['position']}:")
            print(f"  - You designed: '{error['original_dna']}' (Natural Probability: {error['confidence']*100:.1f}%)")
            print(f"  - AI suggests:  '{error['ai_suggestion']}'")
            print("-" * 35)

# ==========================================
# EXECUTE PIPELINE
# ==========================================
if __name__ == "__main__":
    harvest_genomes()
    ai_tokenizer, ai_model, compute_device = initialize_ai()
    scan_custom_dna(ai_tokenizer, ai_model, compute_device)
#
#
# ex: I will be training it upon data from sources at the NCBI database, it is as automated for my specific task as possible and only asks me for the .fasta file of my plasmid.
#
#





#14 august 2026




///cd ~/desktop
#
///python bioscanner_pipeline.py
#
#
#
#
# ex: i got an error...   damo@Nicks-Mac-mini ~ % cd ~/desktopdamo@NicksMacminidesktop%python3bioscanner_pipeline.pyFile"/Users/damo/Desktop/bioscanner_pipeline.py", line 1print("📊 FINALSYNTAXREPORT")IndentationError: unexpected indentdamo@Nicks-Mac-mini desktop % 
#
#
#
#
#ex: i'll try fixing the error by checking the indentation
#
#
#ex: ha haa, i found that luckily id only pasted half of the script into my file! all i have to do is just delete everything in it and paste it all in again!
#
#
#
///python3 bioscanner_pipeline.py
#
#
#
#
#
#ex: when running the entire script i got further errors, i will just use gemini for analysis of what whent wrong and report back later

/Users/classified/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/classified/Desktop/bioscanner_pipeline.py", line 6, in <module>
    import multimolecule
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/multimolecule/__init__.py", line 24, in <module>
    from .data import Dataset, contact_map_to_dot_bracket, dot_bracket_to_contact_map
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/multimolecule/data/__init__.py", line 22, in <module>
    from .dataset import Dataset, SampleDataset
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/multimolecule/data/dataset.py", line 30, in <module>
    import danling as dl
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/danling/__init__.py", line 31, in <module>
    from .runners import (
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/danling/runners/__init__.py", line 45, in <module>
    from .base_runner import BaseRunner
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/danling/runners/base_runner.py", line 44, in <module>
    from .checkpoints import CheckpointManager, FileCheckpointManager
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/danling/runners/checkpoints/__init__.py", line 23, in <module>
    from .torch_ft import FTDataLoaderCheckpointer, TorchFTCheckpointManager
  File "/Users/classified/Library/Python/3.9/lib/python/site-packages/danling/runners/checkpoints/torch_ft.py", line 31, in <module>
    from .torch_distributed import TorchDistributedCheckpointManager, TorchDistributedCheckpointTask, dcp
ImportError: cannot import name 'dcp' from 'danling.runners.checkpoints.torch_distributed' (/Users/damo/Library/Python/3.9/lib/python/site-packages/danling/runners/checkpoints/torch_distributed.py)
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
#
#
#
