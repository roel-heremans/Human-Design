# 🤖 ChatGPT Integration for Human Design Analysis

This module provides ChatGPT-powered analysis for Human Design gates, channels, and other chart elements with personalized insights that match the quality and depth of professional Human Design consultations.

## ✨ Features

- **Personalized Gate Analysis**: Get detailed, personalized insights for each gate based on its activation type (conscious/unconscious/both)
- **Color-Specific Insights**: Understand how black (conscious), red (unconscious), and both activations work differently
- **Professional Quality**: Responses match the depth and style of professional Human Design consultations
- **Fallback System**: Automatically falls back to built-in insights if ChatGPT is unavailable
- **Easy Integration**: Simple API that works with existing OCR system

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install openai python-dotenv
```

### 2. Set Up API Key

Get your OpenAI API key from: https://platform.openai.com/api-keys

**Option A: Environment Variable**
```bash
export OPENAI_API_KEY='your_api_key_here'
```

**Option B: .env File**
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### 3. Basic Usage

```python
from bodygraph_ocr import BodyGraphOCR

# Initialize with ChatGPT integration
ocr = BodyGraphOCR(enable_chatgpt=True)

# Get personalized analysis for any gate
analysis = ocr.fetch_gate_web_info(
    gate_num=5,
    activation_type='Conscious Only (Black)'
)

print(analysis)
```

## 📋 Example Output

When you ask: *"my gate 5 is black (Personal) of the sacral center, can you explain what it means"*

**ChatGPT Response:**
```
⚙️ Gate 5 — Gate 5 - Fixed Rhythms

Location: Sacral Center

🔲 Because it's black (Conscious)

You are aware of your need for routine and predictability. Others may even see you as someone who is dependable, consistent, and loyal.

You can often sense when there is a disruption in your routine, and you intuitively seek to restore stability and predictability.

Your consistent energy becomes a model for others — showing how a steady, predictable rhythm can create an environment of trust and security.

🧭 Practical Guidance

Honor your need for routine. You thrive when you can create a structured and predictable environment for yourself.

Avoid resisting change — your adaptability to maintain your rhythm in the face of change is your strength.

🌙 Shadow → Gift perspective
Level | Expression
Shadow | Resistance to change, inflexibility
Gift | Dependability, creating trust through consistency
Siddhi | Universal rhythm, being in sync with the cosmic flow

In short:
Gate 5 in the Sacral Center gives you a consistent and dependable energy. Because it's conscious — something you're aware of expressing in your daily life, you can use this to create trust and security in your relationships. When you follow your own need for routine, life feels stable and secure; when you resist change, a sense of frustration and inflexibility arises.
```

## 🔧 Advanced Usage

### Analyze Different Activation Types

```python
# Conscious (Black) - You're aware of this energy
conscious_analysis = ocr.fetch_gate_web_info(5, 'Conscious Only (Black)')

# Unconscious (Red) - Others see this more than you do
unconscious_analysis = ocr.fetch_gate_web_info(5, 'Unconscious Only (Red)')

# Both - Powerful, consistent influence
both_analysis = ocr.fetch_gate_web_info(5, 'Both Conscious and Unconscious')
```

### Integrate with Full Reports

```python
def generate_enhanced_report(image_path):
    result = ocr.process_bodygraph(image_path)
    
    print("=== ENHANCED HUMAN DESIGN REPORT ===")
    
    for gate_desc in result['gate_descriptions']:
        print(f"\nGate {gate_desc['gate']}: {gate_desc['name']}")
        
        # Get ChatGPT analysis
        chatgpt_analysis = ocr.fetch_gate_web_info(
            gate_desc['gate'],
            gate_desc['activation_type']
        )
        
        print(chatgpt_analysis)
        print("-" * 50)
```

### Channel Analysis

```python
# Analyze channels with ChatGPT
channel_analysis = ocr.chatgpt.analyze_channel(
    channel_num="5-15",
    channel_name="Channel of Rhythm",
    centers=["Sacral", "Root"],
    gates=[5, 15],
    description="Brings natural rhythm and flow"
)

print(channel_analysis)
```

## 🛠️ Configuration

### Enable/Disable ChatGPT

```python
# With ChatGPT (default)
ocr = BodyGraphOCR(enable_chatgpt=True)

# Without ChatGPT (fallback only)
ocr = BodyGraphOCR(enable_chatgpt=False)
```

### Custom ChatGPT Settings

```python
from chatgpt_integration import HumanDesignChatGPT

# Custom ChatGPT instance
chatgpt = HumanDesignChatGPT(api_key="your_key")

# Use custom model or settings
chatgpt.client.chat.completions.create(
    model="gpt-3.5-turbo",  # or gpt-4
    temperature=0.7,
    max_tokens=1500
)
```

## 📊 Comparison: ChatGPT vs Fallback

| Feature | ChatGPT Integration | Fallback System |
|---------|-------------------|-----------------|
| **Depth** | Professional-level insights | Basic activation info |
| **Personalization** | Highly personalized | Generic descriptions |
| **Practical Guidance** | Detailed, actionable advice | General insights |
| **Shadow/Gift/Siddhi** | Complete perspective | Basic activation type |
| **Cost** | Requires API key | Free |
| **Speed** | ~2-3 seconds per gate | Instant |
| **Reliability** | Depends on API | Always available |

## 🔍 Testing

Run the test script to verify everything works:

```bash
python3 test_chatgpt_integration.py
```

Or run the comprehensive example:

```bash
python3 chatgpt_example.py
```

## 💡 Tips for Best Results

1. **Use GPT-4**: Better quality responses than GPT-3.5
2. **Specific Activation Types**: Always specify conscious/unconscious/both
3. **Include Context**: Provide gate name and center for better analysis
4. **Rate Limiting**: Be mindful of OpenAI API rate limits
5. **Fallback**: Always have fallback system for reliability

## 🚨 Troubleshooting

### Common Issues

**"ChatGPT integration not available"**
- Check your API key is set correctly
- Verify you have internet connection
- Ensure OpenAI API key has sufficient credits

**"Rate limit exceeded"**
- Wait a few minutes before retrying
- Consider upgrading your OpenAI plan
- Use fallback system temporarily

**"Invalid API key"**
- Double-check your API key
- Ensure no extra spaces or characters
- Try regenerating the key

### Debug Mode

```python
import os
os.environ['OPENAI_DEBUG'] = 'true'

# This will show detailed error messages
ocr = BodyGraphOCR(enable_chatgpt=True)
```

## 📈 Future Enhancements

- [ ] Channel analysis integration
- [ ] Type and Strategy analysis
- [ ] Profile line analysis
- [ ] Authority analysis
- [ ] Caching for repeated queries
- [ ] Batch processing for multiple gates

## 🤝 Contributing

Feel free to contribute improvements to the ChatGPT integration:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## 📄 License

This ChatGPT integration is part of the Human Design OCR system and follows the same license terms.
