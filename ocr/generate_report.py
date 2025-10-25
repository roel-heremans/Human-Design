#!/usr/bin/env python3
"""
Generate comprehensive Human Design report from OCR analysis
"""

import sys
from bodygraph_ocr import BodyGraphOCR

def generate_report(image_path):
    """Generate a comprehensive Human Design report"""
    
    print(f"Generating comprehensive Human Design report for: {image_path}")
    print("="*80)
    
    # Initialize OCR
    ocr = BodyGraphOCR()
    
    # Suppress OCR processing output by redirecting stdout temporarily
    import sys
    from io import StringIO
    
    # Save original stdout
    original_stdout = sys.stdout
    
    # Process the body graph (suppress output)
    sys.stdout = StringIO()
    result = ocr.process_bodygraph(image_path)
    sys.stdout = original_stdout
    
    if "error" in result:
        print(f"Error processing image: {result['error']}")
        return
    
    # Extract planetary information
    planetary_info = result.get('planetary_info', {})
    red_numbers = planetary_info.get('red_numbers_clean', [])
    black_numbers = planetary_info.get('black_numbers_clean', [])
    
    # Generate comprehensive report
    report = ocr.generate_comprehensive_report(red_numbers, black_numbers)
    
    # Print planetary information table
    print(f"\n{'='*80}")
    print(f"PLANETARY INFORMATION")
    print(f"{'='*80}")
    
    planetary_info = result.get('planetary_info', {})
    red_numbers = planetary_info.get('red_numbers_clean', [])
    black_numbers = planetary_info.get('black_numbers_clean', [])
    
    # Planetary order
    planets = [
        "Sun", "Earth", "Moon", "North Node", "South Node", 
        "Mercury", "Venus", "Mars", "Jupiter", "Saturn", 
        "Uranus", "Neptune", "Pluto"
    ]
    
    print(f"{'Planet':<12} | {'Design':<8} | {'Personality':<12}")
    print(f"{'-'*12} | {'-'*8} | {'-'*12}")
    
    for i, planet in enumerate(planets):
        if i < len(red_numbers) and i < len(black_numbers):
            design = red_numbers[i] if i < len(red_numbers) else "N/A"  # Red = Design (Unconscious)
            personality = black_numbers[i] if i < len(black_numbers) else "N/A"  # Black = Personality (Conscious)
            print(f"{planet:<12} | {design:<8} | {personality:<12}")
    
    # Print gate summary
    gate_summary = report['gate_summary']
    print(f"\nGATE ACTIVATION SUMMARY:")
    print(f"CONSCIOUS ONLY GATES: {sorted(gate_summary['conscious_only'])}")
    print(f"UNCONSCIOUS ONLY GATES: {sorted(gate_summary['unconscious_only'])}")
    print(f"BOTH CONSCIOUS & UNCONSCIOUS: {sorted(gate_summary['both_conscious_unconscious'])}")
    
    # Print channel descriptions in specific order
    print(f"\n{'='*80}")
    print(f"ACTIVE CHANNELS ANALYSIS")
    print(f"{'='*80}")
    
    # Define the preferred order for channel descriptions
    center_hierarchy = {
        'Root': 1,
        'Spleen': 2, 
        'Sacral': 3,
        'Solar Plexus': 4,
        'G': 5,
        'Heart': 6,
        'Throat': 7,
        'Ajna': 8,
        'Head': 9
    }
    
    def get_channel_priority(channel_desc):
        """Get priority for channel sorting based on center hierarchy"""
        center1, center2 = channel_desc['centers']
        # Use the lower priority center as the primary sort key
        priority1 = center_hierarchy.get(center1, 999)
        priority2 = center_hierarchy.get(center2, 999)
        return min(priority1, priority2)
    
    # Sort channels by priority
    sorted_channels = sorted(report['channel_descriptions'], key=get_channel_priority)
    
    for channel_desc in sorted_channels:
        print(f"\nChannel {channel_desc['channel']}: {channel_desc['name']}")
        print(f"Connects: {channel_desc['centers'][0]} ↔ {channel_desc['centers'][1]}")
        print(f"Description: {channel_desc['description']}")
    
    # Print gate descriptions
    print(f"\n{'='*80}")
    print(f"ACTIVE GATES ANALYSIS")
    print(f"{'='*80}")
    
    for gate_desc in report['gate_descriptions']:
        print(f"\nGate {gate_desc['gate']}: {gate_desc['name']}")
        print(f"Center: {gate_desc['center']}")
        print(f"Activation: {gate_desc['activation_type']}")
        print(f"Description: {gate_desc['description']}")
        print(f"Color Meaning: {gate_desc['color_meaning']}")
        print(f"Web Research: {gate_desc['web_info']}")
    
    print(f"\n{'='*80}")
    print(f"REPORT COMPLETE")
    print(f"{'='*80}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_report.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    generate_report(image_path)
