
#  Pleurotus Plasmid Architecture: Biological Logic Gates

**Lead Researcher/Engineer:** Damien Blackwell (Age 13, UK)

Note: This project is a computational proof-of-concept for synthetic biology workflows.

###  Project Overview
This repository contains the computational framework and architectural modeling for a synthetic plasmid designed for the basidiomycete fungus *Pleurotus ostreatus* (Oyster Mushroom). 

The primary objective of this project is to engineer a highly efficient bioluminescent pathway utilizing structural logic gates. By optimizing the plasmid backbone and promoter regions, this design theoretically yields a higher photon output during the fruiting body stage compared to wild-type bioluminescent species.

### ⚙️ System Architecture
* **The Selection Marker (URA3):** The plasmid backbone integrates the `URA3` gene (orotidine 5'-phosphate decarboxylase). By transforming this plasmid into a uracil-deficient (auxotrophic) *P. ostreatus* host, the `URA3` marker acts as a biological filter. Only successful transformants will survive on uracil-dropout media.
* **Biological Logic Gates:** The transcription of the bioluminescent gene cassette is governed by specific promoter logic, ensuring expression is localized specifically during the formation of the fruiting body.
* **Genomic Integration Pipeline:** The structural design process utilized a custom-trained Genomic Language Model (GLM) to predict the natural occurrence of engineered DNA sequences and detect human-engineered anomalies.

### 📁 Repository Structure
* `/scripts` - Python logic gate simulations, AI training loops, and syntax checkers.
* `/data` - Raw plasmid sequences and FASTA files.
* `/assets` - Visual proof, Benchling maps, and terminal outputs.
* `project_progress.md` - Chronological development and debugging log.

###  How to Run This Project

*Note: The terminal interface and environment for this project were built using **Python 3.9**.*

```bash
# 1. Install Dependencies
pip install -r requirements.txt
pip install einops "urllib3<2"

# 2. Train the AI (Optional)
python3 scripts/refined_train.py

# 3. Run the Syntax Scanner
python3 scripts/bioscanner_pipeline.py
