#!/usr/bin/env python3
"""
Final Cross-Reference Timeline Visualization
Creates a clean timeline showing cross-references between book sections
Author: GitHub Copilot
Date: September 2025
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pdfplumber
import re

def load_cross_references():
    """Load cross-reference data from CSV file"""
    references = []
    with open('xref_with_pages.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                from_page = int(row['From Page'])
                to_page_str = row['To Page'].strip()
                if to_page_str and to_page_str != '':
                    to_page = int(to_page_str)
                    if abs(from_page - to_page) > 3:  # Only significant references
                        references.append({
                            'from_page': from_page, 'to_page': to_page,
                            'from_section': row['From Section'], 'to_section': row['To Section']
                        })
            except (ValueError, KeyError):
                continue
    return references

def extract_main_chapters():
    """Define main chapter locations manually for clean visualization"""
    return {
        26: "1. Introduction", 29: "2. Fundamentals of Probability", 
        44: "3. Fundamentals of Machine Learning", 56: "4. Fundamentals of Networks",
        70: "5. Univariate Probabilities", 102: "6. Multivariate Probabilities",
        122: "7. Entropies", 136: "8. Dependence", 164: "9. Stochastic Processes",
        190: "10. Causation", 206: "11. Networks as Representations",
        224: "12. Probabilistic Modeling", 244: "13. Nonparametric Estimation",
        264: "14. Parametric Estimation", 290: "15. Estimation of Multivariate",
        324: "16. Time Series", 352: "17. Construction of Networks",
        370: "18. Assessing Goodness", 414: "19. Conclusions"
    }

def create_final_timeline():
    """Generate the final clean cross-reference timeline"""
    print("Loading cross-references...")
    references = load_cross_references()
    chapters = extract_main_chapters()
    
    print(f"References: {len(references)}, Chapters: {len(chapters)}")
    
    # Separate forward and backward references
    forward_refs = [ref for ref in references if ref['to_page'] > ref['from_page']]
    backward_refs = [ref for ref in references if ref['to_page'] < ref['from_page']]
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(24, 8))
    
    # Get page range
    min_page = min(min(chapters.keys()), min([ref['from_page'] for ref in references]))
    max_page = max(max(chapters.keys()), max([ref['to_page'] for ref in references]))
    
    # Set up plot
    ax.set_xlim(min_page - 20, max_page + 20)
    ax.set_ylim(-1.4, 1.4)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    
    # Draw main timeline
    ax.axhline(y=0, color='black', linewidth=3, alpha=0.8)
    
    # Add chapter markers
    for page, title in chapters.items():
        ax.axvline(x=page, color='red', linestyle='-', alpha=0.7, linewidth=2)
        ax.text(page, -1.25, title, rotation=45, ha='right', va='top', 
               fontsize=14, fontweight='bold', color='darkred')
    
    # Draw forward references (top)
    arrow_color = 'steelblue'
    for ref in forward_refs:
        distance = abs(ref['to_page'] - ref['from_page'])
        curve_height = min(0.25 + distance/500, 0.8)
        
        x_points = np.linspace(ref['from_page'], ref['to_page'], 30)
        y_points = [curve_height * 4 * t * (1 - t) for t in 
                   [(x - ref['from_page']) / (ref['to_page'] - ref['from_page']) for x in x_points]]
        
        ax.plot(x_points, y_points, color=arrow_color, alpha=0.3, linewidth=2)
        arrow = patches.FancyArrowPatch(
            (x_points[-2], y_points[-2]), (x_points[-1], y_points[-1]),
            arrowstyle='->', mutation_scale=15, color=arrow_color, alpha=0.6
        )
        ax.add_patch(arrow)
    
    # Draw backward references (bottom)
    for ref in backward_refs:
        distance = abs(ref['to_page'] - ref['from_page'])
        curve_height = min(0.25 + distance/500, 0.8)
        
        x_points = np.linspace(ref['from_page'], ref['to_page'], 30)
        y_points = [-curve_height * 4 * t * (1 - t) for t in 
                   [(x - ref['from_page']) / (ref['to_page'] - ref['from_page']) for x in x_points]]
        
        ax.plot(x_points, y_points, color=arrow_color, alpha=0.3, linewidth=2)
        arrow = patches.FancyArrowPatch(
            (x_points[-2], y_points[-2]), (x_points[-1], y_points[-1]),
            arrowstyle='->', mutation_scale=15, color=arrow_color, alpha=0.6
        )
        ax.add_patch(arrow)
    
    plt.tight_layout()
    plt.savefig('final_cross_reference_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('final_cross_reference_timeline.pdf', bbox_inches='tight', facecolor='white')
    
    print("Final timeline saved as 'final_cross_reference_timeline.png' and '.pdf'")
    print(f"Forward references: {len(forward_refs)}, Backward references: {len(backward_refs)}")

if __name__ == "__main__":
    create_final_timeline()
