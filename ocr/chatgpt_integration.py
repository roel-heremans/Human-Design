#!/usr/bin/env python3
"""
ChatGPT Integration for Human Design Analysis

This module provides ChatGPT-powered analysis for Human Design gates,
channels, and other chart elements with personalized insights.
"""

import os
import openai
from dotenv import load_dotenv
from typing import Dict, Optional
import json

# Load environment variables
load_dotenv()

class HumanDesignChatGPT:
    """ChatGPT integration for Human Design analysis"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize ChatGPT client"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it directly.")
        
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def analyze_gate(self, gate_num: int, center: str, activation_type: str, 
                    gate_name: str = None, gate_description: str = None) -> str:
        """
        Get ChatGPT analysis for a specific gate
        
        Args:
            gate_num: Gate number (1-64)
            center: Center name (e.g., 'Sacral', 'Solar Plexus')
            activation_type: 'Conscious Only (Black)', 'Unconscious Only (Red)', or 'Both Conscious and Unconscious'
            gate_name: Optional gate name
            gate_description: Optional gate description
            
        Returns:
            ChatGPT analysis string
        """
        
        # Create the prompt based on the user's example
        prompt = self._create_gate_prompt(gate_num, center, activation_type, gate_name, gate_description)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": """You are a Human Design expert with deep knowledge of the system created by Ra Uru Hu. 
                        You provide detailed, personalized insights about gates, channels, and centers. 
                        You explain concepts clearly and practically, helping people understand how their design influences their daily life."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"ChatGPT analysis failed: {str(e)}"
    
    def analyze_channel(self, channel_num: str, channel_name: str, centers: list, 
                       gates: list, description: str = None) -> str:
        """
        Get ChatGPT analysis for a specific channel
        
        Args:
            channel_num: Channel number (e.g., '5-15')
            channel_name: Channel name
            centers: List of connected centers
            gates: List of gates in the channel
            description: Optional channel description
            
        Returns:
            ChatGPT analysis string
        """
        
        prompt = f"""My channel {channel_num} ({channel_name}) connects {centers[0]} ↔ {centers[1]} centers through gates {gates[0]} and {gates[1]}. 
        
        Can you explain what this channel means for me in practical terms? 
        
        Please include:
        - What this channel brings to my life
        - How I can work with this energy
        - What challenges or gifts this channel provides
        - How this affects my relationships and daily life
        
        Make it personal and practical, like you're explaining it to a friend."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": """You are a Human Design expert. Provide detailed, practical insights about channels, 
                        explaining how they influence daily life, relationships, and personal growth."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=1200,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"ChatGPT channel analysis failed: {str(e)}"
    
    def _create_gate_prompt(self, gate_num: int, center: str, activation_type: str, 
                          gate_name: str = None, gate_description: str = None) -> str:
        """Create a personalized prompt for gate analysis"""
        
        # Determine color and consciousness level
        if "Conscious" in activation_type and "Unconscious" not in activation_type:
            color_desc = "black (Personality/Conscious)"
            consciousness_desc = "conscious — something you're aware of expressing in your daily life"
        elif "Unconscious" in activation_type and "Conscious" not in activation_type:
            color_desc = "red (Design/Unconscious)"
            consciousness_desc = "unconscious — something that operates below your awareness"
        else:
            color_desc = "both black and red (Conscious & Unconscious)"
            consciousness_desc = "both conscious and unconscious — you're aware of it and it also operates automatically"
        
        gate_name_str = f" ({gate_name})" if gate_name else ""
        gate_desc_str = f"\n\nGate Description: {gate_description}" if gate_description else ""
        
        prompt = f"""My gate {gate_num}{gate_name_str} is {color_desc} of the {center} center. Can you explain what this means?

Please break this down clearly and gently, like the example below:

⚙️ Gate {gate_num} — {gate_name or f'The Gate of [Gate Name]'}

Location: {center} Center

🔲 Because it's {color_desc.split('(')[0].strip()}

You know this about yourself (or others see this about you).
Others may even see you as someone who:

[Specific traits and behaviors]

You can often sense when [relevant situations], and you intuitively [how you respond].

Your [gate energy] becomes a model for others — showing how [positive impact].

🧭 Practical Guidance

[Specific actionable advice]

Honor your [specific needs]. You thrive when you [specific behaviors].

Avoid [specific pitfalls] — your [strength] is your strength.

[More specific guidance]

🌙 Shadow → Gift perspective
Level | Expression
Shadow | [Shadow expression]
Gift | [Gift expression]  
Siddhi | [Siddhi expression]

In short:
Gate {gate_num} in the {center} Center gives you [specific energy]. Because it's {consciousness_desc}, [specific awareness description]. When you follow your own [specific guidance], life feels [positive outcome]; when you resist it, [specific challenge] arises.{gate_desc_str}

Would you like me to show how this Gate {gate_num} energy interacts with your Type and Strategy so you can see how to use your [specific energy] correctly in decision-making?"""
        
        return prompt

def test_chatgpt_integration():
    """Test the ChatGPT integration with Gate 5 example"""
    
    # You'll need to set your OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Please set your OPENAI_API_KEY environment variable")
        print("You can get an API key from: https://platform.openai.com/api-keys")
        return
    
    try:
        chatgpt = HumanDesignChatGPT(api_key)
        
        print("=== Testing ChatGPT Integration ===")
        print()
        
        # Test Gate 5 analysis (like the user's example)
        print("Gate 5 Analysis:")
        result = chatgpt.analyze_gate(
            gate_num=5,
            center="Sacral",
            activation_type="Conscious Only (Black)",
            gate_name="Fixed Rhythms",
            gate_description="Gate 5 brings fixed rhythms and waiting. This gate provides natural timing and rhythm, knowing when to act and when to wait."
        )
        print(result)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_chatgpt_integration()
