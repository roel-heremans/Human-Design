#!/usr/bin/env python3
"""
Generate ChatGPT-Enhanced Human Design Report for IMG_1974.PNG

This script processes the body graph image and provides ChatGPT analysis
for each active gate, focusing on Personal (conscious/black) vs Design (unconscious/red) aspects.
"""

import os
import sys
from bodygraph_ocr import BodyGraphOCR

def generate_chatgpt_enhanced_report(image_path):
    """Generate a comprehensive report with ChatGPT analysis for each gate"""
    
    print("🤖 ChatGPT-Enhanced Human Design Report")
    print("=" * 80)
    print(f"Processing: {image_path}")
    print()
    
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OpenAI API key not found!")
        print("Please set your OPENAI_API_KEY environment variable")
        print("You can get an API key from: https://platform.openai.com/api-keys")
        print()
        print("Falling back to basic analysis...")
        ocr = BodyGraphOCR(enable_chatgpt=False)
    else:
        print("✅ OpenAI API key found - using ChatGPT integration")
        ocr = BodyGraphOCR(enable_chatgpt=True)
    
    # Process the body graph
    print("📊 Processing body graph...")
    result = ocr.process_bodygraph(image_path)
    
    # Extract planetary information
    planetary_info = result.get('planetary_info', {})
    red_numbers = planetary_info.get('red_numbers_clean', [])
    black_numbers = planetary_info.get('black_numbers_clean', [])
    
    planets = ['Sun', 'Earth', 'Moon', 'North Node', 'South Node', 'Mercury', 
               'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    
    print("=" * 80)
    print("PLANETARY INFORMATION")
    print("=" * 80)
    print(f"{'Planet':<12} | {'Design (Red)':<12} | {'Personality (Black)':<20}")
    print(f"{'-'*12} | {'-'*12} | {'-'*20}")
    
    for i, planet in enumerate(planets):
        if i < len(red_numbers) and i < len(black_numbers):
            design = red_numbers[i]  # Red = Design (Unconscious)
            personality = black_numbers[i]  # Black = Personality (Conscious)
            print(f"{planet:<12} | {design:<12} | {personality:<20}")
    
    # Extract gate numbers from planetary positions
    red_gates = [int(float(num)) for num in red_numbers]
    black_gates = [int(float(num)) for num in black_numbers]
    
    # Find unique gates and their activation types
    all_gates = list(set(red_gates + black_gates))
    conscious_gates = [gate for gate in all_gates if gate in black_gates and gate not in red_gates]
    unconscious_gates = [gate for gate in all_gates if gate in red_gates and gate not in black_gates]
    both_gates = [gate for gate in all_gates if gate in red_gates and gate in black_gates]
    
    print("\n" + "=" * 80)
    print("GATE ACTIVATION SUMMARY")
    print("=" * 80)
    print(f"PERSONALITY ONLY GATES (Conscious/Black): {sorted(conscious_gates)}")
    print(f"DESIGN ONLY GATES (Unconscious/Red): {sorted(unconscious_gates)}")
    print(f"BOTH PERSONALITY & DESIGN: {sorted(both_gates)}")
    
    print("\n" + "=" * 80)
    print("CHATGPT-ENHANCED GATE ANALYSIS")
    print("=" * 80)
    
    # Analyze each gate with ChatGPT
    for i, gate_num in enumerate(sorted(all_gates), 1):
        # Determine activation type
        if gate_num in both_gates:
            activation_type = "Both Conscious and Unconscious"
        elif gate_num in conscious_gates:
            activation_type = "Conscious Only (Black)"
        else:
            activation_type = "Unconscious Only (Red)"
        
        # Get gate info
        gate_info = ocr.gates.get(gate_num, {})
        gate_name = gate_info.get('name', f'Gate {gate_num}')
        center = ocr.get_center_for_gate(gate_num)
        
        print(f"\n{'='*60}")
        print(f"GATE {gate_num}: {gate_name}")
        print(f"Center: {center}")
        print(f"Activation: {activation_type}")
        print(f"{'='*60}")
        
        # Get ChatGPT analysis
        chatgpt_analysis = ocr.fetch_gate_web_info(gate_num, activation_type)
        print(chatgpt_analysis)
        
        print(f"\n{'='*60}")
        print(f"End of Gate {gate_num} Analysis")
        print(f"{'='*60}")
    
    # Get channel information
    channel_descriptions = result.get('channel_descriptions', [])
    
    print("\n" + "=" * 80)
    print("ACTIVE CHANNELS")
    print("=" * 80)
    
    if channel_descriptions:
        for channel_desc in channel_descriptions:
            print(f"\nChannel {channel_desc['channel']}: {channel_desc['name']}")
            print(f"Connects: {channel_desc['centers'][0]} ↔ {channel_desc['centers'][1]}")
            print(f"Description: {channel_desc['description']}")
    else:
        print("No active channels found")
    
    print("\n" + "=" * 80)
    print("REPORT COMPLETE")
    print("=" * 80)
    print(f"Total Gates Analyzed: {len(all_gates)}")
    print(f"Total Channels Found: {len(channel_descriptions)}")
    
    if api_key:
        print("✅ ChatGPT analysis included")
    else:
        print("⚠️  Basic analysis only (no ChatGPT)")

def main():
    """Main function"""
    image_path = "body-graphs/IMG_1974.PNG"
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        print("Please make sure the image file exists in the body-graphs directory")
        return
    
    generate_chatgpt_enhanced_report(image_path)

if __name__ == "__main__":
    main()
