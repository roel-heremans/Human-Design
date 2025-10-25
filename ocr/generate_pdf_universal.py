#!/usr/bin/env python3
"""
Human Design PDF Report Generator - Universal Script

This script can generate PDF reports for any Human Design body graph image.
Usage: python3 generate_pdf_universal.py <image_path> [output_path]
"""

import sys
import os
from generate_pdf_report import HumanDesignPDFGenerator

def main():
    """Main function to generate PDF report for any image"""
    
    if len(sys.argv) < 2:
        print("Usage: python3 generate_pdf_universal.py <image_path> [output_path]")
        print()
        print("Examples:")
        print("  python3 generate_pdf_universal.py body-graphs/IMG_1974.PNG")
        print("  python3 generate_pdf_universal.py body-graphs/IMG_1975.PNG custom_report.pdf")
        return
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return
    
    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  No OpenAI API key found - generating report without ChatGPT analysis")
        enable_chatgpt = False
    else:
        print("✅ OpenAI API key found - including ChatGPT analysis")
        enable_chatgpt = True
    
    # Generate PDF report
    generator = HumanDesignPDFGenerator(enable_chatgpt=enable_chatgpt)
    
    try:
        output_file = generator.generate_pdf_report(image_path, output_path)
        
        print(f"\n🎉 PDF report generated successfully!")
        print(f"📄 File: {output_file}")
        print(f"📊 Size: {os.path.getsize(output_file) / 1024:.1f} KB")
        
        # Show file location
        full_path = os.path.abspath(output_file)
        print(f"📍 Full path: {full_path}")
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")

if __name__ == "__main__":
    main()
