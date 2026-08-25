# Pleurotus Plasmid Architecture: Biological Logic Gates

###  Project Overview
This repository contains the computational framework and architectural modeling for a synthetic plasmid designed for the basidiomycete fungus *Pleurotus ostreatus* (Oyster Mushroom). 

The primary objective of this project is to engineer a highly efficient bioluminescent pathway utilizing structural logic gates. By optimizing the plasmid backbone and promoter regions, this design theoretically yields a higher photon output during the fruiting body stage compared to wild-type bioluminescent species.

###  System Architecture

* **The Selection Marker (URA3):** The plasmid backbone integrates the `URA3` gene (orotidine 5'-phosphate decarboxylase). By transforming this plasmid into a uracil-deficient (auxotrophic) *P. ostreatus* host, the `URA3` marker acts as a biological filter. Only successful transformants will survive on uracil-dropout media, ensuring long-term stability and selection of the glowing mycelium.
* **Biological Logic Gates:** The transcription of the bioluminescent gene cassette is governed by specific promoter logic, ensuring expression is localized and amplified specifically during the formation of the fruiting body, rather than expending cellular energy during vegetative mycelial growth.
* **Genomic Integration Pipeline:** The structural design process utilized AI-assisted genomic database analysis to identify optimal restriction sites and promoter sequences compatible with basidiomycete expression systems.

### 📁 Repository Structure
* `/src` - Python logic gate simulations and plasmid syntax checkers.
* `/docs` - Research logs and genomic database training data.
* `project_progress.md` - Chronological development and debugging log.

*Note: This project is a computational proof-of-concept for synthetic biology workflows.*
