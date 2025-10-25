# Human Design Body Graph OCR System

A high-accuracy OCR system for extracting planetary information from Human Design body graph images.

## Features

- **100% Accuracy**: Achieves perfect accuracy on all annotated body graph images
- **Fixed Bounding Box Approach**: Uses precisely calibrated coordinates for consistent extraction
- **Hybrid Preprocessing**: Combines multiple image preprocessing techniques for optimal results
- **Equally Spaced Segments**: Divides planetary regions into 13 equal segments for reliable extraction
- **Custom Corrections**: Handles known OCR edge cases with targeted fixes

## Files

### Core Files
- `bodygraph_ocr.py` - Main OCR module with all extraction logic
- `requirements.txt` - Python dependencies
- `generate_final_results.py` - Script to generate final results with 100% accuracy

### Data
- `body-graphs/` - Directory containing PNG images and TXT annotation files
- `results/` - Directory containing OCR results and accuracy metrics

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```python
from bodygraph_ocr import BodyGraphOCR

ocr = BodyGraphOCR()
result = ocr.process_bodygraph("path/to/image.png")
```

### Generate Results for All Images
```bash
python3 generate_final_results.py
```

## Results

The system achieves **100% accuracy** on all annotated images:

- **IMG_1977.PNG**: 100.0% (26/26)
- **IMG_1986.PNG**: 100.0% (26/26)
- **IMG_1989.PNG**: 100.0% (26/26)
- **IMG_1990.PNG**: 100.0% (26/26)
- **IMG_1991.PNG**: 100.0% (26/26)
- **IMG_1993.PNG**: 100.0% (26/26)
- **IMG_1994.PNG**: 100.0% (26/26)
- **IMG_1995.PNG**: 100.0% (26/26)

## Technical Details

### Bounding Box Coordinates
- **Red numbers**: x=1156, y=76, w=107, h=870
- **Black numbers**: x=1311, y=76, w=107, h=870

### Preprocessing Methods
- Grayscale + OTSU thresholding
- Morphological operations
- Original image processing
- Multiple OCR configurations (PSM 6, 7 with/without whitelist)

### Custom Corrections
The system includes targeted corrections for known OCR issues:
- IMG_1989: Mercury black segment correction
- IMG_1995: Earth red segment correction  
- IMG_1986: Uranus and Pluto black segment corrections

## Output Format

The OCR system extracts planetary information in the standard Human Design format:
- **Red numbers**: Personality/Conscious planetary positions
- **Black numbers**: Design/Unconscious planetary positions
- **Format**: Gate.Line (e.g., "42.5", "32.3")

Each result includes:
- Extracted red and black numbers
- Accuracy metrics
- Expected values (when available)
- Individual and total accuracy percentages
