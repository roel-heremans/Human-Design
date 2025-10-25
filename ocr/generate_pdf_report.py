#!/usr/bin/env python3
"""
Human Design PDF Report Generator

This script generates a comprehensive PDF report including:
- Original body graph image
- Planetary information table
- Active channels analysis with ChatGPT insights
- Detailed gate analysis with ChatGPT insights
- Summary section
"""

import os
import sys
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from bodygraph_ocr import BodyGraphOCR

class HumanDesignPDFGenerator:
    """Generate comprehensive Human Design PDF reports"""
    
    def __init__(self, enable_chatgpt=True):
        """Initialize the PDF generator with OCR and ChatGPT integration"""
        self.ocr = BodyGraphOCR(enable_chatgpt=enable_chatgpt)
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Setup custom paragraph styles for the PDF"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        ))
        
        # Heading style
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.darkblue
        ))
        
        # Subheading style
        self.styles.add(ParagraphStyle(
            name='CustomSubHeading',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=12,
            textColor=colors.darkgreen
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY
        ))
        
        # Gate analysis style
        self.styles.add(ParagraphStyle(
            name='GateAnalysis',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=4,
            leftIndent=20,
            alignment=TA_JUSTIFY
        ))
    
    def generate_pdf_report(self, image_path, output_path=None):
        """Generate a comprehensive PDF report"""
        
        if not output_path:
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            output_path = f"{base_name}_human_design_report.pdf"
        
        print(f"🤖 Generating Human Design PDF Report")
        print(f"📊 Processing: {image_path}")
        print(f"📄 Output: {output_path}")
        print()
        
        # Process the body graph
        print("Processing body graph...")
        result = self.ocr.process_bodygraph(image_path)
        
        # Create PDF document
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        story = []
        
        # Add title page
        story.extend(self.create_title_page(image_path))
        story.append(PageBreak())
        
        # Add planetary information table
        story.extend(self.create_planetary_table(result))
        story.append(PageBreak())
        
        # Add centers analysis
        story.extend(self.create_centers_analysis(result))
        story.append(PageBreak())
        
        # Add active channels analysis
        story.extend(self.create_channels_analysis(result))
        story.append(PageBreak())
        
        # Add detailed gate analysis
        story.extend(self.create_gates_analysis(result))
        story.append(PageBreak())
        
        # Add global summary
        story.extend(self.create_global_summary(result))
        
        # Build PDF
        print("Building PDF...")
        doc.build(story)
        
        print(f"✅ PDF report generated successfully: {output_path}")
        return output_path
    
    def create_title_page(self, image_path):
        """Create the title page with the body graph image"""
        elements = []
        
        # Title
        title = Paragraph("Human Design Analysis Report", self.styles['CustomTitle'])
        elements.append(title)
        elements.append(Spacer(1, 20))
        
        # Subtitle
        subtitle = Paragraph("Comprehensive Chart Analysis with ChatGPT Insights", self.styles['CustomHeading'])
        elements.append(subtitle)
        elements.append(Spacer(1, 30))
        
        # Add the body graph image
        try:
            # Get image dimensions to maintain aspect ratio
            from PIL import Image as PILImage
            pil_img = PILImage.open(image_path)
            img_width, img_height = pil_img.size
            aspect_ratio = img_width / img_height
            
            # Calculate dimensions to fill page width while maintaining aspect ratio
            page_width = 7.5 * inch  # Leave some margin
            page_height = 9 * inch   # Leave space for title and info
            
            # Calculate scaled dimensions
            if aspect_ratio > (page_width / page_height):
                # Image is wider - scale to page width
                scaled_width = page_width
                scaled_height = page_width / aspect_ratio
            else:
                # Image is taller - scale to page height
                scaled_height = page_height
                scaled_width = page_height * aspect_ratio
            
            img = Image(image_path, width=scaled_width, height=scaled_height)
            img.hAlign = 'CENTER'
            elements.append(img)
        except Exception as e:
            error_text = Paragraph(f"Error loading image: {str(e)}", self.styles['CustomBody'])
            elements.append(error_text)
        
        elements.append(Spacer(1, 30))
        
        # Report info
        report_date = datetime.now().strftime("%B %d, %Y")
        date_text = Paragraph(f"Report Generated: {report_date}", self.styles['CustomBody'])
        elements.append(date_text)
        
        chart_name = os.path.splitext(os.path.basename(image_path))[0]
        chart_text = Paragraph(f"Chart: {chart_name}", self.styles['CustomBody'])
        elements.append(chart_text)
        
        return elements
    
    def create_planetary_table(self, result):
        """Create the planetary information table"""
        elements = []
        
        # Heading
        heading = Paragraph("Planetary Information", self.styles['CustomHeading'])
        elements.append(heading)
        elements.append(Spacer(1, 12))
        
        # Extract planetary data
        planetary_info = result.get('planetary_info', {})
        red_numbers = planetary_info.get('red_numbers_clean', [])
        black_numbers = planetary_info.get('black_numbers_clean', [])
        
        planets = ['Sun', 'Earth', 'Moon', 'North Node', 'South Node', 'Mercury', 
                   'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
        
        # Create table data
        table_data = [['Planet', 'Design (Red)', 'Personality (Black)']]
        
        for i, planet in enumerate(planets):
            if i < len(red_numbers) and i < len(black_numbers):
                design = red_numbers[i]
                personality = black_numbers[i]
                table_data.append([planet, design, personality])
        
        # Create table
        table = Table(table_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))
        
        # Add explanation
        explanation = Paragraph(
            "<b>Design (Red):</b> Unconscious aspects of your nature that operate below your awareness.<br/>"
            "<b>Personality (Black):</b> Conscious aspects of your personality that you're aware of expressing.",
            self.styles['CustomBody']
        )
        elements.append(explanation)
        
        return elements
    
    def create_centers_analysis(self, result):
        """Create centers analysis with ChatGPT insights for defined and undefined centers"""
        elements = []
        
        # Heading
        heading = Paragraph("Centers Analysis", self.styles['CustomHeading'])
        elements.append(heading)
        elements.append(Spacer(1, 12))
        
        # Get center information
        center_analysis = result.get('center_analysis', {})
        defined_centers = center_analysis.get('defined_centers', [])
        
        # All Human Design centers
        all_centers = ['Head', 'Ajna', 'Throat', 'G', 'Heart', 'Solar Plexus', 'Sacral', 'Spleen', 'Root']
        undefined_centers = [center for center in all_centers if center not in defined_centers]
        
        # Defined Centers Section
        defined_heading = Paragraph("Defined Centers", self.styles['CustomSubHeading'])
        elements.append(defined_heading)
        elements.append(Spacer(1, 8))
        
        if defined_centers:
            defined_text = Paragraph(
                f"<b>Defined Centers:</b> {', '.join(defined_centers)}<br/>"
                f"These centers provide consistent energy and represent your natural gifts and talents.",
                self.styles['CustomBody']
            )
            elements.append(defined_text)
            elements.append(Spacer(1, 12))
            
            # Analyze each defined center with ChatGPT
            for center in defined_centers:
                center_header = Paragraph(f"Center: {center}", self.styles['CustomSubHeading'])
                elements.append(center_header)
                
                # Get ChatGPT analysis for defined center
                if self.ocr.chatgpt:
                    try:
                        chatgpt_analysis = self.get_center_chatgpt_analysis(center, True)
                        chatgpt_para = Paragraph(f"<b>Analysis:</b><br/>{chatgpt_analysis}", self.styles['GateAnalysis'])
                        elements.append(chatgpt_para)
                    except Exception as e:
                        error_para = Paragraph(f"ChatGPT analysis unavailable: {str(e)}", self.styles['CustomBody'])
                        elements.append(error_para)
                else:
                    basic_para = Paragraph(f"<b>Description:</b> {self.get_center_basic_description(center, True)}", self.styles['CustomBody'])
                    elements.append(basic_para)
                
                elements.append(Spacer(1, 12))
        else:
            no_defined = Paragraph("No defined centers found.", self.styles['CustomBody'])
            elements.append(no_defined)
        
        elements.append(Spacer(1, 20))
        
        # Undefined Centers Section
        undefined_heading = Paragraph("Undefined Centers", self.styles['CustomSubHeading'])
        elements.append(undefined_heading)
        elements.append(Spacer(1, 8))
        
        if undefined_centers:
            undefined_text = Paragraph(
                f"<b>Undefined Centers:</b> {', '.join(undefined_centers)}<br/>"
                f"These centers are open and represent areas where you're influenced by others and can be wise.",
                self.styles['CustomBody']
            )
            elements.append(undefined_text)
            elements.append(Spacer(1, 12))
            
            # Analyze each undefined center with ChatGPT
            for center in undefined_centers:
                center_header = Paragraph(f"Center: {center}", self.styles['CustomSubHeading'])
                elements.append(center_header)
                
                # Get ChatGPT analysis for undefined center
                if self.ocr.chatgpt:
                    try:
                        chatgpt_analysis = self.get_center_chatgpt_analysis(center, False)
                        chatgpt_para = Paragraph(f"<b>Analysis:</b><br/>{chatgpt_analysis}", self.styles['GateAnalysis'])
                        elements.append(chatgpt_para)
                    except Exception as e:
                        error_para = Paragraph(f"ChatGPT analysis unavailable: {str(e)}", self.styles['CustomBody'])
                        elements.append(error_para)
                else:
                    basic_para = Paragraph(f"<b>Description:</b> {self.get_center_basic_description(center, False)}", self.styles['CustomBody'])
                    elements.append(basic_para)
                
                elements.append(Spacer(1, 12))
        else:
            all_defined = Paragraph("All centers are defined - this is very rare!", self.styles['CustomBody'])
            elements.append(all_defined)
        
        return elements
    
    def get_center_chatgpt_analysis(self, center_name, is_defined):
        """Get ChatGPT analysis for a center"""
        try:
            if is_defined:
                prompt = f"""In Human Design, the {center_name} center is defined (colored in) in this person's chart. 
                Can you explain what this means for them in practical terms?
                
                Please include:
                - What this defined center brings to their life
                - How they can work with this energy
                - What gifts and challenges this center provides
                - How this affects their daily life and relationships
                
                Make it personal and practical, like you're explaining it to a friend."""
            else:
                prompt = f"""In Human Design, the {center_name} center is undefined (open/white) in this person's chart. 
                Can you explain what this means for them in practical terms?
                
                Please include:
                - What this undefined center means for their life
                - How they can work with this openness
                - What wisdom and challenges this center provides
                - How this affects their daily life and relationships
                
                Make it personal and practical, like you're explaining it to a friend."""
            
            response = self.ocr.chatgpt.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": """You are a Human Design expert. Provide detailed, practical insights about centers, 
                        explaining how they influence daily life, relationships, and personal growth."""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"ChatGPT analysis failed: {str(e)}"
    
    def get_center_basic_description(self, center_name, is_defined):
        """Get basic description for a center when ChatGPT is not available"""
        descriptions = {
            'Head': {
                'defined': 'Provides consistent mental pressure and inspiration. You have reliable access to ideas and mental stimulation.',
                'undefined': 'Open to mental pressure from others. You can be wise about mental processes and ideas.'
            },
            'Ajna': {
                'defined': 'Provides consistent mental awareness and certainty. You have reliable mental processing and decision-making.',
                'undefined': 'Open to mental awareness from others. You can be wise about mental processes and perspectives.'
            },
            'Throat': {
                'defined': 'Provides consistent communication and manifestation energy. You have reliable ways to express yourself.',
                'undefined': 'Open to communication from others. You can be wise about expression and manifestation.'
            },
            'G': {
                'defined': 'Provides consistent love, direction, and identity. You have reliable sense of self and purpose.',
                'undefined': 'Open to love and direction from others. You can be wise about identity and life direction.'
            },
            'Heart': {
                'defined': 'Provides consistent willpower and ego energy. You have reliable drive and determination.',
                'undefined': 'Open to willpower from others. You can be wise about ego and determination.'
            },
            'Solar Plexus': {
                'defined': 'Provides consistent emotional awareness and sensitivity. You have reliable emotional processing.',
                'undefined': 'Open to emotions from others. You can be wise about emotional processes and feelings.'
            },
            'Sacral': {
                'defined': 'Provides consistent life force and work energy. You have reliable vitality and productivity.',
                'undefined': 'Open to life force from others. You can be wise about work and vitality.'
            },
            'Spleen': {
                'defined': 'Provides consistent intuition and survival instincts. You have reliable gut feelings and health awareness.',
                'undefined': 'Open to intuition from others. You can be wise about health and survival instincts.'
            },
            'Root': {
                'defined': 'Provides consistent pressure and drive. You have reliable motivation and stress response.',
                'undefined': 'Open to pressure from others. You can be wise about stress and motivation.'
            }
        }
        
        return descriptions.get(center_name, {}).get('defined' if is_defined else 'undefined', 'No description available')
    
    def create_channels_analysis(self, result):
        """Create active channels analysis with ChatGPT insights"""
        elements = []
        
        # Heading
        heading = Paragraph("Active Channels Analysis", self.styles['CustomHeading'])
        elements.append(heading)
        elements.append(Spacer(1, 12))
        
        # Get channel information
        channel_descriptions = result.get('channel_descriptions', [])
        
        if not channel_descriptions:
            no_channels = Paragraph("No active channels found in this chart.", self.styles['CustomBody'])
            elements.append(no_channels)
            return elements
        
        # Analyze each channel
        for i, channel_desc in enumerate(channel_descriptions, 1):
            # Channel header
            channel_header = Paragraph(
                f"Channel {channel_desc['channel']}: {channel_desc['name']}",
                self.styles['CustomSubHeading']
            )
            elements.append(channel_header)
            
            # Channel details
            centers_text = f"Connects: {channel_desc['centers'][0]} ↔ {channel_desc['centers'][1]}"
            centers_para = Paragraph(centers_text, self.styles['CustomBody'])
            elements.append(centers_para)
            
            # Basic description
            desc_para = Paragraph(f"<b>Description:</b> {channel_desc['description']}", self.styles['CustomBody'])
            elements.append(desc_para)
            
            # ChatGPT analysis if available
            if self.ocr.chatgpt:
                try:
                    chatgpt_analysis = self.ocr.chatgpt.analyze_channel(
                        channel_num=channel_desc['channel'],
                        channel_name=channel_desc['name'],
                        centers=channel_desc['centers'],
                        gates=channel_desc['gates'],
                        description=channel_desc['description']
                    )
                    
                    chatgpt_para = Paragraph(f"<b>ChatGPT Analysis:</b><br/>{chatgpt_analysis}", self.styles['GateAnalysis'])
                    elements.append(chatgpt_para)
                except Exception as e:
                    error_para = Paragraph(f"ChatGPT analysis unavailable: {str(e)}", self.styles['CustomBody'])
                    elements.append(error_para)
            
            elements.append(Spacer(1, 15))
        
        return elements
    
    def create_gates_analysis(self, result):
        """Create detailed gates analysis with ChatGPT insights"""
        elements = []
        
        # Heading
        heading = Paragraph("Detailed Gates Analysis", self.styles['CustomHeading'])
        elements.append(heading)
        elements.append(Spacer(1, 12))
        
        # Extract gate information
        planetary_info = result.get('planetary_info', {})
        red_numbers = planetary_info.get('red_numbers_clean', [])
        black_numbers = planetary_info.get('black_numbers_clean', [])
        
        # Extract gate numbers
        red_gates = [int(float(num)) for num in red_numbers]
        black_gates = [int(float(num)) for num in black_numbers]
        all_gates = list(set(red_gates + black_gates))
        
        # Gate activation summary
        conscious_gates = [gate for gate in all_gates if gate in black_gates and gate not in red_gates]
        unconscious_gates = [gate for gate in all_gates if gate in red_gates and gate not in black_gates]
        both_gates = [gate for gate in all_gates if gate in red_gates and gate in black_gates]
        
        # Summary table
        summary_data = [
            ['Activation Type', 'Gates', 'Count'],
            ['Personality Only (Conscious/Black)', ', '.join(map(str, sorted(conscious_gates))), str(len(conscious_gates))],
            ['Design Only (Unconscious/Red)', ', '.join(map(str, sorted(unconscious_gates))), str(len(unconscious_gates))],
            ['Both Personality & Design', ', '.join(map(str, sorted(both_gates))), str(len(both_gates))]
        ]
        
        summary_table = Table(summary_data, colWidths=[2*inch, 3*inch, 1*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
        ]))
        
        elements.append(summary_table)
        elements.append(Spacer(1, 20))
        
        # Analyze each gate
        for gate_num in sorted(all_gates):
            # Determine activation type
            if gate_num in both_gates:
                activation_type = "Both Conscious and Unconscious"
            elif gate_num in conscious_gates:
                activation_type = "Conscious Only (Black)"
            else:
                activation_type = "Unconscious Only (Red)"
            
            # Get gate info
            gate_info = self.ocr.gates.get(gate_num, {})
            gate_name = gate_info.get('name', f'Gate {gate_num}')
            center = self.ocr.get_center_for_gate(gate_num)
            
            # Gate header
            gate_header = Paragraph(
                f"Gate {gate_num}: {gate_name}",
                self.styles['CustomSubHeading']
            )
            elements.append(gate_header)
            
            # Gate details
            details_text = f"Center: {center} | Activation: {activation_type}"
            details_para = Paragraph(details_text, self.styles['CustomBody'])
            elements.append(details_para)
            
            # ChatGPT analysis
            try:
                chatgpt_analysis = self.ocr.fetch_gate_web_info(gate_num, activation_type)
                chatgpt_para = Paragraph(f"<b>Analysis:</b><br/>{chatgpt_analysis}", self.styles['GateAnalysis'])
                elements.append(chatgpt_para)
            except Exception as e:
                error_para = Paragraph(f"Analysis unavailable: {str(e)}", self.styles['CustomBody'])
                elements.append(error_para)
            
            elements.append(Spacer(1, 15))
        
        return elements
    
    def create_global_summary(self, result):
        """Create comprehensive global summary section"""
        elements = []
        
        # Heading
        heading = Paragraph("Global Summary", self.styles['CustomHeading'])
        elements.append(heading)
        elements.append(Spacer(1, 12))
        
        # Extract data for summary
        planetary_info = result.get('planetary_info', {})
        center_analysis = result.get('center_analysis', {})
        channel_descriptions = result.get('channel_descriptions', [])
        gate_descriptions = result.get('gate_descriptions', [])
        
        red_numbers = planetary_info.get('red_numbers_clean', [])
        black_numbers = planetary_info.get('black_numbers_clean', [])
        
        red_gates = [int(float(num)) for num in red_numbers]
        black_gates = [int(float(num)) for num in black_numbers]
        all_gates = list(set(red_gates + black_gates))
        
        defined_centers = center_analysis.get('defined_centers', [])
        all_centers = ['Head', 'Ajna', 'Throat', 'G', 'Heart', 'Solar Plexus', 'Sacral', 'Spleen', 'Root']
        undefined_centers = [center for center in all_centers if center not in defined_centers]
        
        # Chart Overview
        overview_text = f"""
        <b>Chart Overview:</b><br/>
        This Human Design chart reveals a unique energetic blueprint with {len(defined_centers)} defined centers 
        and {len(undefined_centers)} undefined centers. The chart contains {len(all_gates)} active gates 
        distributed across {len(channel_descriptions)} active channels, creating a complex and dynamic 
        energy system that influences every aspect of life.
        """
        
        overview_para = Paragraph(overview_text, self.styles['CustomBody'])
        elements.append(overview_para)
        elements.append(Spacer(1, 15))
        
        # Centers Summary
        centers_text = f"""
        <b>Centers Analysis:</b><br/>
        <b>Defined Centers ({len(defined_centers)}):</b> {', '.join(defined_centers)}<br/>
        These centers provide consistent energy and represent your natural gifts and talents. 
        They are reliable sources of energy that you can depend on.<br/><br/>
        
        <b>Undefined Centers ({len(undefined_centers)}):</b> {', '.join(undefined_centers)}<br/>
        These centers are open and represent areas where you're influenced by others and can be wise. 
        They are sources of wisdom and learning opportunities.
        """
        
        centers_para = Paragraph(centers_text, self.styles['CustomBody'])
        elements.append(centers_para)
        elements.append(Spacer(1, 15))
        
        # Channels Summary
        channels_text = f"""
        <b>Active Channels ({len(channel_descriptions)}):</b><br/>
        """
        
        if channel_descriptions:
            channel_list = []
            for channel in channel_descriptions:
                channel_list.append(f"• {channel['channel']}: {channel['name']} ({channel['centers'][0]} ↔ {channel['centers'][1]})")
            
            channels_text += "<br/>".join(channel_list)
            channels_text += "<br/><br/>These channels create defined centers and represent your natural gifts and talents. Each channel brings specific energy and abilities to your life."
        else:
            channels_text += "No active channels found in this chart."
        
        channels_para = Paragraph(channels_text, self.styles['CustomBody'])
        elements.append(channels_para)
        elements.append(Spacer(1, 15))
        
        # Gates Summary
        conscious_gates = [g for g in all_gates if g in black_gates and g not in red_gates]
        unconscious_gates = [g for g in all_gates if g in red_gates and g not in black_gates]
        both_gates = [g for g in all_gates if g in red_gates and g in black_gates]
        
        gates_text = f"""
        <b>Active Gates Analysis ({len(all_gates)} total):</b><br/>
        <b>Personality Gates (Conscious/Black) - {len(conscious_gates)}:</b> {', '.join(map(str, sorted(conscious_gates)))}<br/>
        These gates represent aspects of your personality that you're aware of expressing.<br/><br/>
        
        <b>Design Gates (Unconscious/Red) - {len(unconscious_gates)}:</b> {', '.join(map(str, sorted(unconscious_gates)))}<br/>
        These gates represent aspects of your design that operate below your awareness.<br/><br/>
        
        <b>Both Personality & Design - {len(both_gates)}:</b> {', '.join(map(str, sorted(both_gates)))}<br/>
        These gates are your most powerful influences, operating both consciously and unconsciously.
        """
        
        gates_para = Paragraph(gates_text, self.styles['CustomBody'])
        elements.append(gates_para)
        elements.append(Spacer(1, 15))
        
        # Key Insights with ChatGPT
        if self.ocr.chatgpt:
            try:
                insights_prompt = f"""
                Based on this Human Design chart analysis, provide a comprehensive summary of key insights:
                
                - {len(defined_centers)} defined centers: {', '.join(defined_centers)}
                - {len(undefined_centers)} undefined centers: {', '.join(undefined_centers)}
                - {len(channel_descriptions)} active channels
                - {len(all_gates)} active gates ({len(conscious_gates)} conscious, {len(unconscious_gates)} unconscious, {len(both_gates)} both)
                
                Please provide:
                1. Overall chart theme and energy
                2. Key strengths and gifts
                3. Areas for growth and wisdom
                4. Practical guidance for living authentically
                5. Relationship dynamics
                
                Make it personal, practical, and inspiring.
                """
                
                insights_response = self.ocr.chatgpt.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system", 
                            "content": """You are a Human Design expert providing comprehensive chart analysis. 
                            Give practical, personalized insights that help people understand their unique design."""
                        },
                        {
                            "role": "user",
                            "content": insights_prompt
                        }
                    ],
                    max_tokens=1200,
                    temperature=0.7
                )
                
                insights_text = f"<b>Key Insights & Guidance:</b><br/>{insights_response.choices[0].message.content}"
                
            except Exception as e:
                insights_text = f"<b>Key Insights:</b><br/>ChatGPT analysis unavailable: {str(e)}<br/><br/>This Human Design chart reveals a unique combination of conscious and unconscious energies. Understanding these patterns can help you align with your authentic nature and make decisions that honor your unique design."
        else:
            insights_text = """
            <b>Key Insights:</b><br/>
            This Human Design chart reveals a unique combination of conscious and unconscious energies. 
            The gates that are active in both your Personality (conscious) and Design (unconscious) represent 
            your most powerful and consistent influences. The Personality-only gates show aspects you're 
            aware of expressing, while Design-only gates represent energies that operate below your awareness 
            but are often more visible to others.<br/><br/>
            
            The active channels create defined centers that provide consistent energy flow and represent 
            your natural gifts and talents. Understanding these patterns can help you align with your 
            authentic nature and make decisions that honor your unique design.
            """
        
        insights_para = Paragraph(insights_text, self.styles['CustomBody'])
        elements.append(insights_para)
        
        return elements
    
    def create_summary(self, result):
        """Create summary section (legacy method - now using create_global_summary)"""
        return self.create_global_summary(result)

def main():
    """Main function to generate PDF report"""
    image_path = "body-graphs/IMG_1974.PNG"
    
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
    output_path = generator.generate_pdf_report(image_path)
    
    print(f"\n🎉 PDF report generated successfully!")
    print(f"📄 File: {output_path}")
    print(f"📊 Size: {os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
