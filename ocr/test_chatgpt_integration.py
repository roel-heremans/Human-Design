#!/usr/bin/env python3
"""
Test ChatGPT Integration for Human Design Analysis

This script demonstrates how to use ChatGPT for personalized Human Design gate analysis.
"""

import os
from bodygraph_ocr import BodyGraphOCR

def test_chatgpt_gate_analysis():
    """Test ChatGPT analysis for Gate 5 (like the user's example)"""
    
    print("=== Testing ChatGPT Integration for Gate 5 ===")
    print()
    
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OpenAI API key not found!")
        print("Please set your OPENAI_API_KEY environment variable")
        print("You can get an API key from: https://platform.openai.com/api-keys")
        print()
        print("To set it:")
        print("export OPENAI_API_KEY='your_api_key_here'")
        print()
        print("Or create a .env file with:")
        print("OPENAI_API_KEY=your_api_key_here")
        return
    
    try:
        # Initialize OCR with ChatGPT enabled
        print("Initializing OCR with ChatGPT integration...")
        ocr = BodyGraphOCR(enable_chatgpt=True)
        
        print("✅ OCR initialized successfully!")
        print()
        
        # Test Gate 5 analysis (Conscious/Black)
        print("🔍 Analyzing Gate 5 (Conscious/Black) - Fixed Rhythms...")
        print("=" * 60)
        
        result = ocr.fetch_gate_web_info(5, 'Conscious Only (Black)')
        print(result)
        
        print("\n" + "=" * 60)
        print("🔍 Analyzing Gate 5 (Unconscious/Red) - Fixed Rhythms...")
        print("=" * 60)
        
        result = ocr.fetch_gate_web_info(5, 'Unconscious Only (Red)')
        print(result)
        
        print("\n" + "=" * 60)
        print("🔍 Analyzing Gate 5 (Both) - Fixed Rhythms...")
        print("=" * 60)
        
        result = ocr.fetch_gate_web_info(5, 'Both Conscious and Unconscious')
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nThis might be due to:")
        print("1. Invalid API key")
        print("2. Network connection issues")
        print("3. OpenAI API rate limits")
        print("4. Missing dependencies")

def test_without_chatgpt():
    """Test the fallback system without ChatGPT"""
    
    print("=== Testing Fallback System (No ChatGPT) ===")
    print()
    
    try:
        # Initialize OCR without ChatGPT
        ocr = BodyGraphOCR(enable_chatgpt=False)
        
        print("✅ OCR initialized with fallback system!")
        print()
        
        # Test Gate 5 analysis
        print("🔍 Analyzing Gate 5 (Conscious/Black) - Fixed Rhythms...")
        print("=" * 60)
        
        result = ocr.fetch_gate_web_info(5, 'Conscious Only (Black)')
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Human Design ChatGPT Integration Test")
    print("=" * 50)
    print()
    
    # Test with ChatGPT if API key available
    test_chatgpt_gate_analysis()
    
    print("\n" + "=" * 50)
    print()
    
    # Test fallback system
    test_without_chatgpt()
