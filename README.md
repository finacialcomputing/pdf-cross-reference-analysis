# PDF Cross-Reference Analysis System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive Python system for analyzing cross-references in academic PDFs and creating visual mappings between sections and concepts. This project demonstrates  text processing, data visualization.

## 🎯 Project Overview

This system extracts and analyzes cross-references from academic PDFs (use case: Data-Driven Modeling, Cambridge 2025) and creates two complementary visualizations:

1. **📈 Timeline Visualization**: Interactive timeline showing cross-references as curved arrows
2. **🕸️ Concept Network**: Hierarchical network displaying relationships between key financial/mathematical concepts

## 🚀 Features

- **Automated PDF Processing**: Extracts text and identifies section structures
- **Intelligent Cross-Reference Detection**: Uses advanced regex patterns to find references
- **Dual Visualization System**: Timeline and network representations
- **Professional Output**: High-quality PNG and PDF exports
- **Data Export**: Comprehensive CSV files for further analysis
- **Clean Architecture**: Well-documented, modular Python code

## 📊 Analysis Results for the book Probabilistic Data-Driven Modeling (https://www.cambridge.org/core/books/probabilistic-datadriven-modeling/BA499CC1F0904618A7914C6CBAB03A26)

- **279 cross-references** identified and mapped
- **162 forward references** vs **117 backward references**
- **25 key concepts** with **66 interconnections**
- **19 main chapters** analyzed
- Clean hierarchical layout with proportional sizing

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pdf-cross-reference-analysis.git
cd pdf-cross-reference-analysis

# Install required packages
pip install pdfplumber matplotlib numpy
```

## 📁 Project Structure

```
├── final_timeline_visualization.py    # Timeline visualization generator
├── final_concept_network.py          # Concept network visualization
├── enhanced_concept_network.py       # Alternative network implementation
├── xref_with_pages.csv              # Cross-reference data (279 entries)
├── concept_mapping.csv              # Concept relationships
├── final_cross_reference_timeline.png # Timeline output
├── final_concept_network.png        # Network output
└── README.md                        # This file
```

## 🎮 Usage

### Generate Timeline Visualization
```bash
python final_timeline_visualization.py
```
Creates a timeline showing cross-references as curved arrows above (forward) and below (backward) the page sequence.

### Generate Concept Network
```bash
python final_concept_network.py
```
Creates a hierarchical network showing relationships between key concepts like "data modeling", "probability", "multivariate analysis", etc.

## 📈 Visualizations

### Timeline Visualization
- **Forward arrows** (top): References pointing to later sections
- **Backward arrows** (bottom): References pointing to earlier sections
- **Transparency**: Proportional to reference frequency
- **Chapter markers**: Key section indicators

### Concept Network
- **Node size**: Proportional to concept frequency
- **Edge thickness**: Proportional to connection strength
- **Hierarchical layout**: Organized in concentric rings
- **Color coding**: Semantic grouping of related concepts

## 🔧 Technical Details

### Dependencies
- `pdfplumber`: PDF text extraction
- `matplotlib`: Visualization and plotting
- `numpy`: Numerical computations
- `csv`: Data handling

### Key Algorithms
- **Text Processing**: Section detection and reference extraction
- **Layout Algorithm**: Hierarchical circular positioning
- **Visualization**: Curved arrow generation with transparency
- **Network Analysis**: Connection strength calculation

## 📊 Data Format

### Cross-Reference Data (`xref_with_pages.csv`)
```csv
from_section,to_section,from_page,to_page,reference_text
1.1,2.3,15,45,"see Section 2.3"
```

### Concept Mapping (`concept_mapping.csv`)
```csv
concept1,concept2,connection_strength
data modeling,probability,0.8
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Academic literature analysis techniques
- Python visualization community
- Financial modeling research methods

## 📧 Contact

For questions or collaboration opportunities, please open an issue or contact through GitHub.

---
*This project demonstrates advanced Python techniques for academic text analysis and data visualization in financial computing contexts.*
