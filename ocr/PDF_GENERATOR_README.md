# 📄 Human Design PDF Report Generator

This module generates comprehensive PDF reports for Human Design body graph images, including ChatGPT-powered analysis for gates and channels.

## ✨ Features

- **Professional PDF Layout**: Clean, well-designed reports with proper formatting
- **Body Graph Image**: Original chart displayed on the first page
- **Planetary Information Table**: Complete planetary positions with Design (Red) and Personality (Black) columns
- **Active Channels Analysis**: Detailed channel descriptions with ChatGPT insights
- **Detailed Gates Analysis**: Comprehensive gate analysis with ChatGPT-powered insights
- **Summary Section**: Overview of chart patterns and key insights
- **ChatGPT Integration**: Professional-quality analysis matching Human Design consultations

## 🚀 Quick Start

### Basic Usage

```python
from generate_pdf_report import HumanDesignPDFGenerator

# Generate PDF report
generator = HumanDesignPDFGenerator(enable_chatgpt=True)
output_path = generator.generate_pdf_report("body-graphs/IMG_1974.PNG")
```

### Command Line Usage

```bash
# Generate report for specific image
python3 generate_pdf_universal.py body-graphs/IMG_1974.PNG

# Generate with custom output name
python3 generate_pdf_universal.py body-graphs/IMG_1975.PNG my_report.pdf
```

## 📋 PDF Report Structure

### Page 1: Title Page
- Report title and subtitle
- Original body graph image (6x6 inches)
- Generation date and chart name

### Page 2: Planetary Information Table
```
Planet       | Design (Red) | Personality (Black)
-------------|--------------|--------------------
Sun          | 36.4         | 12.2
Earth        | 6.4          | 11.2
Moon         | 29.2         | 5.5
...
```

### Page 3: Active Channels Analysis
- Channel name and number
- Connected centers
- Basic description
- ChatGPT analysis (if available)

### Page 4+: Detailed Gates Analysis
- Gate activation summary table
- Individual gate analysis with:
  - Gate name and center
  - Activation type (Conscious/Unconscious/Both)
  - ChatGPT analysis with practical guidance

### Final Page: Summary
- Chart statistics
- Key insights and patterns
- Practical guidance

## 🎨 PDF Styling

The PDF uses professional styling with:
- **Colors**: Dark blue headings, dark green subheadings
- **Fonts**: Helvetica family with proper sizing
- **Layout**: Clean tables with alternating row colors
- **Spacing**: Proper margins and spacing for readability

## 🔧 Configuration

### Enable/Disable ChatGPT

```python
# With ChatGPT analysis (default)
generator = HumanDesignPDFGenerator(enable_chatgpt=True)

# Without ChatGPT (fallback only)
generator = HumanDesignPDFGenerator(enable_chatgpt=False)
```

### Custom Output Path

```python
# Auto-generated name
output_path = generator.generate_pdf_report("body-graphs/IMG_1974.PNG")

# Custom name
output_path = generator.generate_pdf_report("body-graphs/IMG_1974.PNG", "custom_report.pdf")
```

## 📊 Example Output

The generated PDF includes:

1. **Title Page**: Professional header with body graph image
2. **Planetary Table**: Clean table with all 13 planetary positions
3. **Channel Analysis**: Detailed analysis of active channels
4. **Gate Analysis**: Comprehensive analysis of all active gates
5. **Summary**: Key insights and patterns

## 🛠️ Dependencies

Required packages:
- `reportlab`: PDF generation
- `pillow`: Image handling
- `openai`: ChatGPT integration (optional)
- `python-dotenv`: Environment variable handling

Install with:
```bash
pip install reportlab pillow openai python-dotenv
```

## 📈 Performance

- **File Size**: Typically 500KB - 2MB depending on content
- **Generation Time**: 30-60 seconds with ChatGPT analysis
- **Pages**: 5-15 pages depending on number of active gates/channels

## 🔍 Troubleshooting

### Common Issues

**"Image not found"**
- Check the image path is correct
- Ensure the image file exists and is readable

**"ChatGPT analysis unavailable"**
- Check your OpenAI API key is set
- Verify you have sufficient API credits
- Check internet connection

**"PDF generation failed"**
- Ensure reportlab is installed correctly
- Check disk space for output file
- Verify write permissions in output directory

### Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)

generator = HumanDesignPDFGenerator(enable_chatgpt=True)
# This will show detailed error messages
```

## 🎯 Use Cases

1. **Professional Consultations**: Generate client reports
2. **Personal Analysis**: Create detailed self-analysis reports
3. **Research**: Document chart patterns and insights
4. **Education**: Teaching materials for Human Design courses
5. **Archiving**: Save analysis results for future reference

## 📝 Customization

### Custom Styles

You can modify the PDF styling by editing the `setup_custom_styles()` method:

```python
# Customize colors
self.styles.add(ParagraphStyle(
    name='CustomTitle',
    fontSize=24,
    textColor=colors.darkblue  # Change color
))
```

### Custom Content

Add custom sections by extending the generator class:

```python
class CustomPDFGenerator(HumanDesignPDFGenerator):
    def create_custom_section(self, result):
        # Add your custom content
        pass
```

## 🚀 Future Enhancements

- [ ] Multiple chart comparison reports
- [ ] Interactive PDF elements
- [ ] Custom branding and logos
- [ ] Multiple language support
- [ ] Chart overlay annotations
- [ ] Export to other formats (HTML, Word)

## 📄 License

This PDF generator is part of the Human Design OCR system and follows the same license terms.
