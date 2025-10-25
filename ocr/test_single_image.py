#!/usr/bin/env python3
"""
Script to test OCR on a single image
Usage: python3 test_single_image.py path/to/image.PNG
"""

import sys
import os
from bodygraph_ocr import BodyGraphOCR

def test_single_image(image_path):
    """Test OCR on a single image"""
    
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found")
        return
    
    print(f"Testing OCR on: {image_path}")
    print("="*60)
    
    # Initialize OCR
    ocr = BodyGraphOCR()
    
    # Process the image
    result = ocr.process_bodygraph(image_path)
    
    # Display results
    print("EXTRACTED PLANETARY NUMBERS:")
    print("-" * 40)
    
    planetary_order = [
        "Sun", "Earth", "Moon", "North Node", "South Node", 
        "Mercury", "Venus", "Mars", "Jupiter", "Saturn", 
        "Uranus", "Neptune", "Pluto"
    ]
    
    # Get planetary info
    planetary_info = result.get('planetary_info', {})
    red_numbers = planetary_info.get('red_numbers_clean', [])
    black_numbers = planetary_info.get('black_numbers_clean', [])
    
    print(f"{'Planet':<12} {'Red (Personality)':<18} {'Black (Design)':<18}")
    print("-" * 50)
    
    for i, planet in enumerate(planetary_order):
        red = red_numbers[i] if i < len(red_numbers) else "N/A"
        black = black_numbers[i] if i < len(black_numbers) else "N/A"
        print(f"{planet:<12} {red:<18} {black:<18}")
    
    print("\n" + "="*60)
    print("CENTER DEFINITION ANALYSIS:")
    print("="*60)
    
    # Analyze center definitions
    center_analysis = ocr.analyze_center_definitions(red_numbers, black_numbers)
    
    # Get conscious/unconscious gate summary
    gate_summary = ocr.summarize_conscious_unconscious_gates(red_numbers, black_numbers)
    
    print(f"CONSCIOUS ONLY GATES: {sorted(gate_summary['conscious_only'])}")
    print(f"UNCONSCIOUS ONLY GATES: {sorted(gate_summary['unconscious_only'])}")
    print(f"BOTH CONSCIOUS & UNCONSCIOUS: {sorted(gate_summary['both_conscious_unconscious'])}")
    
    print(f"\nDefined Channels ({len(center_analysis['defined_channels'])}):")
    for channel in center_analysis['defined_channels']:
        print(f"  Channel {channel['channel']}: {channel['name']}")
        print(f"    Connects: {channel['centers'][0]} ↔ {channel['centers'][1]}")
        print(f"    Description: {channel['description']}")
        print(f"    Gates: {channel['gates']}")
    
    print(f"\nDefined Centers: {center_analysis['defined_centers']}")
    print(f"Total Defined Centers: {len(center_analysis['defined_centers'])}")
    
    print("\n" + "="*60)
    print("SUMMARY:")
    print(f"Red numbers extracted: {len(red_numbers)}")
    print(f"Black numbers extracted: {len(black_numbers)}")
    print(f"Total extractions: {len(red_numbers) + len(black_numbers)}")
    print(f"Activated gates: {len(center_analysis['activated_gates'])}")
    print(f"Defined channels: {len(center_analysis['defined_channels'])}")
    print(f"Defined centers: {len(center_analysis['defined_centers'])}")
    
    # Check if annotation file exists
    annotation_file = image_path.replace('.PNG', '.txt').replace('.png', '.txt')
    if os.path.exists(annotation_file):
        print(f"\nAnnotation file found: {annotation_file}")
        print("Run 'python3 generate_final_results.py' for accuracy analysis")
    else:
        print(f"\nNo annotation file found: {annotation_file}")
        print("Create annotation file to check accuracy")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 test_single_image.py path/to/image.PNG")
        print("Example: python3 test_single_image.py body-graphs/IMG_1999.PNG")
        sys.exit(1)
    
    image_path = sys.argv[1]
    test_single_image(image_path)
