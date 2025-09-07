#!/usr/bin/env python3
"""
Final Concept Network Visualization
Creates a clean network visualization of cross-referenced concepts from academic text
Author: GitHub Copilot
Date: September 2025
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from collections import defaultdict, Counter
import math

def load_enhanced_concepts():
    """Define enhanced multi-word concepts with realistic connection weights"""
    concepts = {
        'probability_theory': 379, 'statistical_modeling': 343, 'data_analysis': 274, 
        'parameter_estimation': 272, 'multivariate_analysis': 238, 'parametric_methods': 194,
        'information_theory': 142, 'scaling_laws': 128, 'time_series_analysis': 109, 
        'network_analysis': 107, 'model_validation': 94, 'causal_inference': 76,
        'correlation_analysis': 70, 'nonparametric_methods': 41, 'machine_learning': 85,
        'extreme_value_theory': 65, 'bayesian_methods': 55, 'optimization_methods': 45,
        'dimensionality_reduction': 35, 'clustering_methods': 30, 'robust_statistics': 25,
        'spectral_analysis': 20, 'neural_networks': 15, 'financial_modeling': 12, 'univariate': 43
    }
    return concepts

def create_concept_connections(concepts):
    """Define comprehensive connections ensuring all concepts are linked"""
    connections = [
        # Core probability ecosystem
        ('data_analysis', 'probability_theory', 35), ('statistical_modeling', 'probability_theory', 38),
        ('probability_theory', 'parameter_estimation', 35), ('multivariate_analysis', 'probability_theory', 30),
        ('parametric_methods', 'probability_theory', 24), ('nonparametric_methods', 'probability_theory', 18),
        
        # Machine learning cluster
        ('data_analysis', 'machine_learning', 28), ('machine_learning', 'statistical_modeling', 22),
        ('machine_learning', 'parameter_estimation', 20), ('machine_learning', 'model_validation', 18),
        ('machine_learning', 'optimization_methods', 16), ('machine_learning', 'neural_networks', 15),
        ('machine_learning', 'clustering_methods', 12),
        
        # Statistical modeling connections
        ('statistical_modeling', 'parameter_estimation', 25), ('statistical_modeling', 'model_validation', 22),
        ('statistical_modeling', 'parametric_methods', 20), ('statistical_modeling', 'nonparametric_methods', 15),
        ('statistical_modeling', 'bayesian_methods', 18),
        
        # Data analysis ecosystem
        ('data_analysis', 'multivariate_analysis', 26), ('data_analysis', 'correlation_analysis', 20),
        ('data_analysis', 'time_series_analysis', 18), ('data_analysis', 'dimensionality_reduction', 15),
        ('data_analysis', 'robust_statistics', 12),
        
        # Multivariate analysis cluster
        ('multivariate_analysis', 'correlation_analysis', 22), ('multivariate_analysis', 'dimensionality_reduction', 18),
        ('multivariate_analysis', 'clustering_methods', 16), ('multivariate_analysis', 'parametric_methods', 15),
        
        # Information theory and networks
        ('information_theory', 'network_analysis', 18), ('information_theory', 'probability_theory', 20),
        ('information_theory', 'causal_inference', 15), ('network_analysis', 'causal_inference', 12),
        ('network_analysis', 'spectral_analysis', 10), ('network_analysis', 'clustering_methods', 8),
        
        # Time series and causality
        ('time_series_analysis', 'causal_inference', 15), ('time_series_analysis', 'probability_theory', 18),
        ('time_series_analysis', 'scaling_laws', 12), ('time_series_analysis', 'financial_modeling', 8),
        
        # Parameter estimation ecosystem
        ('parameter_estimation', 'bayesian_methods', 18), ('parameter_estimation', 'optimization_methods', 16),
        ('parameter_estimation', 'model_validation', 20), ('parameter_estimation', 'robust_statistics', 10),
        
        # Advanced methods
        ('extreme_value_theory', 'probability_theory', 14), ('extreme_value_theory', 'scaling_laws', 10),
        ('extreme_value_theory', 'robust_statistics', 8), ('bayesian_methods', 'parametric_methods', 12),
        ('bayesian_methods', 'model_validation', 10), ('optimization_methods', 'neural_networks', 12),
        ('optimization_methods', 'clustering_methods', 8), ('dimensionality_reduction', 'spectral_analysis', 8),
        ('dimensionality_reduction', 'neural_networks', 6), ('robust_statistics', 'nonparametric_methods', 8),
        ('robust_statistics', 'model_validation', 6), ('spectral_analysis', 'neural_networks', 5),
        ('financial_modeling', 'extreme_value_theory', 6), ('financial_modeling', 'multivariate_analysis', 5),
        
        # Scaling and cross-connections
        ('scaling_laws', 'probability_theory', 14), ('scaling_laws', 'network_analysis', 8),
        ('correlation_analysis', 'causal_inference', 8), ('model_validation', 'information_theory', 6),
        ('clustering_methods', 'information_theory', 5), ('neural_networks', 'information_theory', 4),
        ('spectral_analysis', 'probability_theory', 6), ('financial_modeling', 'statistical_modeling', 4),
        ('univariate', 'probability_theory', 8), ('univariate', 'parametric_methods', 6), ('univariate', 'nonparametric_methods', 5),
    ]
    
    # Convert to dictionary format
    concept_links = defaultdict(lambda: defaultdict(int))
    for from_concept, to_concept, strength in connections:
        if from_concept in concepts and to_concept in concepts:
            concept_links[from_concept][to_concept] = strength
    
    return concept_links

def calculate_clean_layout(concepts):
    """Create clean hierarchical circular layout"""
    sorted_concepts = sorted(concepts.keys(), key=lambda x: concepts[x], reverse=True)
    positions = {}
    
    # Hierarchical ring layout
    layout_rings = {
        'center': sorted_concepts[0:1],      # Most important at center
        'inner': sorted_concepts[1:7],       # Top 6 in inner ring
        'middle': sorted_concepts[7:15],     # Next 8 in middle ring
        'outer': sorted_concepts[15:]        # Remaining in outer ring
    }
    
    for ring_name, ring_concepts in layout_rings.items():
        if not ring_concepts:
            continue
            
        n_concepts = len(ring_concepts)
        
        if ring_name == 'center':
            positions[ring_concepts[0]] = (0, 0)
        elif ring_name == 'inner':
            radius = 3.5
            for i, concept in enumerate(ring_concepts):
                angle = 2 * math.pi * i / n_concepts
                positions[concept] = (radius * math.cos(angle), radius * math.sin(angle))
        elif ring_name == 'middle':
            radius = 6.5
            angle_offset = math.pi / n_concepts  # Offset for better spacing
            for i, concept in enumerate(ring_concepts):
                angle = angle_offset + 2 * math.pi * i / n_concepts
                positions[concept] = (radius * math.cos(angle), radius * math.sin(angle))
        elif ring_name == 'outer':
            radius = 9.5
            for i, concept in enumerate(ring_concepts):
                angle = 2 * math.pi * i / n_concepts
                positions[concept] = (radius * math.cos(angle), radius * math.sin(angle))
    
    return positions

def create_final_concept_network():
    """Generate the final clean concept network visualization"""
    print("Loading enhanced concepts...")
    concepts = load_enhanced_concepts()
    concept_links = create_concept_connections(concepts)
    positions = calculate_clean_layout(concepts)
    
    print(f"Concepts: {len(concepts)}, Connections: {sum(len(links) for links in concept_links.values())}")
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(20, 20))
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Scaling factors
    max_connections = max(concepts.values())
    max_link_strength = max(max(links.values()) for links in concept_links.values() if links)
    
    # Draw connections
    for from_concept, to_concepts in concept_links.items():
        if from_concept in positions:
            for to_concept, strength in to_concepts.items():
                if to_concept in positions:
                    x1, y1 = positions[from_concept]
                    x2, y2 = positions[to_concept]
                    
                    # Arrow properties based on connection strength
                    arrow_width = 1.0 + 3.0 * (strength / max_link_strength)
                    arrow_alpha = 0.4 + 0.5 * (strength / max_link_strength)
                    
                    # Calculate offsets to avoid overlapping with bubbles
                    dx, dy = x2 - x1, y2 - y1
                    distance = math.sqrt(dx**2 + dy**2)
                    if distance > 0:
                        dx_norm, dy_norm = dx / distance, dy / distance
                        from_radius = 0.3 + 0.8 * (concepts[from_concept] / max_connections)
                        to_radius = 0.3 + 0.8 * (concepts[to_concept] / max_connections)
                        
                        start_x = x1 + dx_norm * from_radius
                        start_y = y1 + dy_norm * from_radius
                        end_x = x2 - dx_norm * to_radius
                        end_y = y2 - dy_norm * to_radius
                        
                        # Draw curved arrow
                        arrow = patches.FancyArrowPatch(
                            (start_x, start_y), (end_x, end_y),
                            arrowstyle='->', mutation_scale=arrow_width * 8,
                            color='steelblue', alpha=arrow_alpha, linewidth=arrow_width,
                            connectionstyle="arc3,rad=0.15"
                        )
                        ax.add_patch(arrow)
    
    # Define color scheme
    colors = {
        'probability_theory': '#FF6B6B', 'statistical_modeling': '#4ECDC4', 'data_analysis': '#45B7D1',
        'parameter_estimation': '#96CEB4', 'multivariate_analysis': '#FFEAA7', 'parametric_methods': '#DDA0DD',
        'information_theory': '#98D8C8', 'scaling_laws': '#F7DC6F', 'time_series_analysis': '#BB8FCE',
        'network_analysis': '#85C1E9', 'model_validation': '#F8C471', 'causal_inference': '#F1948A',
        'correlation_analysis': '#82E0AA', 'nonparametric_methods': '#D7BDE2', 'machine_learning': '#76D7C4',
        'extreme_value_theory': '#F8D7DA', 'bayesian_methods': '#D4EDDA', 'optimization_methods': '#FFF3CD',
        'dimensionality_reduction': '#CCE5FF', 'clustering_methods': '#E7E7FF', 'robust_statistics': '#FFCCCB',
        'spectral_analysis': '#E0FFE0', 'neural_networks': '#FFE0CC', 'financial_modeling': '#E0E0FF', 'univariate': '#FFEBCD'
    }
    
    # Draw concept bubbles
    for concept, (x, y) in positions.items():
        connections = concepts[concept]
        bubble_radius = 0.3 + 0.8 * (connections / max_connections)
        bubble_color = colors.get(concept, '#B0B0B0')
        
        # Draw bubble
        circle = patches.Circle((x, y), bubble_radius, facecolor=bubble_color, 
                              edgecolor='black', linewidth=1.5, alpha=0.85)
        ax.add_patch(circle)
        
        # Add text (no background)
        display_name = concept.replace('_', '\n')
        font_size = max(8, min(12, 7 + 3 * (connections / max_connections)))
        text_color = 'white' if bubble_color in ['#FF6B6B', '#45B7D1', '#BB8FCE', '#85C1E9'] else 'black'
        
        ax.text(x, y, display_name, ha='center', va='center', 
               fontsize=font_size, fontweight='bold', color=text_color)
    
    # Save final visualization
    plt.tight_layout()
    plt.savefig('final_concept_network.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('final_concept_network.pdf', bbox_inches='tight', facecolor='white')
    
    print("Final concept network saved as 'final_concept_network.png' and '.pdf'")
    print(f"Layout: {len(concepts)} concepts in clean hierarchical rings")

if __name__ == "__main__":
    create_final_concept_network()
