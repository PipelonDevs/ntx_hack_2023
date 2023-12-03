# ntx_hack_2023

# Bore No More - Project README

## Overview

**Bore No More** is an innovative project developed for the [Hackathon Name] hackathon. Focused on creating a dynamic boredom classifier adaptable to various applications, our example integrates it with a simple game. Leveraging scikit-learn (SKLEARN), MNE (Martinos Center for Biomedical Imaging), and Unicorn Hybrid Black EEG band, we aim to revolutionize user experiences. The project includes datasets, Jupyter notebooks for testing, and a Tetris game.

### Team Members

- Tomasz Koralewski
- Paweł Dzikiewicz
- Adam Pawłowski

### Project Structure

```
/project-root
|-- Datasets              # Directory for datasets
|-- MNE                   # MNE library related files
|-- jupyter-tests         # Jupyter notebook testing files
|-- SKLEARN               # Scikit-learn related files
|-- tetris                # Tetris game source code
|   |-- tetris_boring     # Tetris version for boring states
|   |-- tetris_immersive  # Tetris version for immersive states
|-- .gitignore            # Git ignore file
|-- __init__.py           # Initialization file
|-- main.py               # Main project execution file
|-- README.md             # Project README file
```

### EEG Data Collection

We utilized the Unicorn Hybrid Black EEG band for data collection. The gathered datasets are stored in the `Datasets` directory for analysis and training the boredom classifier.


### Boredom Classifier

The boredom classifier, implemented in the SKLEARN directory, uses scikit-learn to analyze EEG data and assess the user's boredom level dynamically.

### Tetris Game

The `tetris` directory contains the source code for two Tetris game versions:
- `tetris_boring`: A Tetris version designed for boring states.
- `tetris_immersive`: A Tetris version tailored for immersive states.

### References

Our project draws inspiration from the following scientific works:

- Neural correlates of flow, boredom, and anxiety in gaming: An
electroencephalogram study (https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=8812&context=masters_theses)
- Classification of EEG signals in gaming using machine learning (https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=8831&context=masters_theses)
- Application of Artificial Intelligence Techniques for Brain–Computer Interface in Mental Fatigue Detection: A Systematic Review (https://scholarsmine.mst.edu/cgi/viewcontent.cgi?article=8831&context=masters_theses)



### Future Improvements

- Explore additional EEG features for improved classification.
- Enhance Tetris game integration based on real-time EEG analysis.
- Expand the project to support various applications.

### Acknowledgments

We extend our gratitude to NTXHackathon for organizing this event and providing us with the opportunity to develop and present **Bore No More**.
