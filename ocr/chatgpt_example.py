#!/usr/bin/env python3
"""
Complete ChatGPT Integration Example for Human Design Analysis

This script shows how to integrate ChatGPT into your Human Design OCR system
to get personalized, detailed gate analysis like the user's ChatGPT example.
"""

import os
from bodygraph_ocr import BodyGraphOCR

def main():
    """Main example demonstrating ChatGPT integration"""
    
    print("🤖 Human Design ChatGPT Integration Example")
    print("=" * 60)
    print()
    
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OpenAI API key not found!")
        print()
        print("To use ChatGPT integration:")
        print("1. Get an API key from: https://platform.openai.com/api-keys")
        print("2. Set it as an environment variable:")
        print("   export OPENAI_API_KEY='your_api_key_here'")
        print()
        print("3. Or create a .env file with:")
        print("   OPENAI_API_KEY=your_api_key_here")
        print()
        print("For now, showing fallback system...")
        print()
        
        # Test without ChatGPT
        test_fallback_system()
        return
    
    # Test with ChatGPT
    test_chatgpt_system()

def test_chatgpt_system():
    """Test the full ChatGPT integration"""
    
    print("✅ OpenAI API key found!")
    print("Initializing ChatGPT integration...")
    print()
    
    try:
        # Initialize OCR with ChatGPT
        ocr = BodyGraphOCR(enable_chatgpt=True)
        
        print("🎯 Testing Gate 5 Analysis (Your Example)")
        print("=" * 50)
        
        # This replicates the user's ChatGPT query
        print("Query: 'my gate 5 is black (Personal) of the sacral center, can you explain what it means'")
        print()
        
        # Get ChatGPT analysis
        analysis = ocr.fetch_gate_web_info(5, 'Conscious Only (Black)')
        print(analysis)
        
        print("\n" + "=" * 50)
        print("🎯 Testing Different Activation Types")
        print("=" * 50)
        
        # Test different activation types
        activation_types = [
            ('Conscious Only (Black)', 'Personality/Conscious'),
            ('Unconscious Only (Red)', 'Design/Unconscious'),
            ('Both Conscious and Unconscious', 'Both Conscious & Unconscious')
        ]
        
        for activation_type, description in activation_types:
            print(f"\n📋 {description}:")
            print("-" * 30)
            analysis = ocr.fetch_gate_web_info(5, activation_type)
            print(analysis[:300] + "..." if len(analysis) > 300 else analysis)
        
        print("\n" + "=" * 50)
        print("🎯 Testing Other Gates")
        print("=" * 50)
        
        # Test other common gates
        test_gates = [
            (12, 'Conscious Only (Black)', 'Throat'),
            (22, 'Unconscious Only (Red)', 'Solar Plexus'),
            (36, 'Both Conscious and Unconscious', 'Solar Plexus')
        ]
        
        for gate_num, activation_type, center in test_gates:
            print(f"\n📋 Gate {gate_num} ({center} Center):")
            print("-" * 30)
            analysis = ocr.fetch_gate_web_info(gate_num, activation_type)
            print(analysis[:200] + "..." if len(analysis) > 200 else analysis)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nFalling back to built-in system...")
        test_fallback_system()

def test_fallback_system():
    """Test the fallback system without ChatGPT"""
    
    print("🔄 Testing Fallback System (No ChatGPT)")
    print("=" * 50)
    
    try:
        # Initialize OCR without ChatGPT
        ocr = BodyGraphOCR(enable_chatgpt=False)
        
        print("✅ Fallback system initialized!")
        print()
        
        # Test Gate 5 analysis
        print("📋 Gate 5 (Conscious/Black) Analysis:")
        print("-" * 30)
        analysis = ocr.fetch_gate_web_info(5, 'Conscious Only (Black)')
        print(analysis)
        
        print("\n📋 Gate 5 (Unconscious/Red) Analysis:")
        print("-" * 30)
        analysis = ocr.fetch_gate_web_info(5, 'Unconscious Only (Red)')
        print(analysis)
        
    except Exception as e:
        print(f"❌ Error: {e}")

def show_integration_code():
    """Show how to integrate ChatGPT into your own code"""
    
    print("\n" + "=" * 60)
    print("💻 How to Integrate ChatGPT into Your Code")
    print("=" * 60)
    print()
    
    code_example = '''
# 1. Set up your environment
import os
from bodygraph_ocr import BodyGraphOCR

# 2. Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your_api_key_here'

# 3. Initialize OCR with ChatGPT
ocr = BodyGraphOCR(enable_chatgpt=True)

# 4. Get ChatGPT analysis for any gate
analysis = ocr.fetch_gate_web_info(
    gate_num=5,
    activation_type='Conscious Only (Black)'
)

print(analysis)

# 5. Use in your Human Design reports
def generate_personalized_report(image_path):
    result = ocr.process_bodygraph(image_path)
    
    for gate_desc in result['gate_descriptions']:
        chatgpt_analysis = ocr.fetch_gate_web_info(
            gate_desc['gate'],
            gate_desc['activation_type']
        )
        print(f"Gate {gate_desc['gate']}: {chatgpt_analysis}")
'''
    
    print(code_example)

if __name__ == "__main__":
    main()
    show_integration_code()
