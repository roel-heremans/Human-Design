#!/usr/bin/env python3
"""
Human Design Channel Definitions
Complete mapping of all 36 channels, their gates, and connected centers
"""

# Complete Human Design Channel Definitions
HUMAN_DESIGN_CHANNELS = {
    # Individual Circuit Channels
    "1-8": {"name": "Channel of Inspiration", "centers": ["Head", "Throat"], "circuit": "Individual"},
    "2-14": {"name": "Channel of the Beat", "centers": ["Ajna", "Sacral"], "circuit": "Individual"},
    "3-60": {"name": "Channel of Mutation", "centers": ["Root", "Sacral"], "circuit": "Individual"},
    "4-63": {"name": "Channel of Logic", "centers": ["Ajna", "Head"], "circuit": "Individual"},
    "5-15": {"name": "Channel of Rhythm", "centers": ["Sacral", "Throat"], "circuit": "Individual"},
    "6-59": {"name": "Channel of Mating", "centers": ["Sacral", "Root"], "circuit": "Individual"},
    "7-31": {"name": "Channel of the Alpha", "centers": ["Throat", "G"], "circuit": "Individual"},
    "9-52": {"name": "Channel of Concentration", "centers": ["Sacral", "Root"], "circuit": "Individual"},
    "10-20": {"name": "Channel of Awakening", "centers": ["G", "Throat"], "circuit": "Individual"},
    "10-57": {"name": "Channel of Perfected Form", "centers": ["G", "Spleen"], "circuit": "Individual"},
    "11-56": {"name": "Channel of Curiosity", "centers": ["Ajna", "Throat"], "circuit": "Individual"},
    "12-22": {"name": "Channel of Openness", "centers": ["Throat", "Solar Plexus"], "circuit": "Individual"},
    "13-33": {"name": "Channel of the Prodigal", "centers": ["Throat", "G"], "circuit": "Individual"},
    "14-2": {"name": "Channel of the Beat", "centers": ["Sacral", "Ajna"], "circuit": "Individual"},
    "15-5": {"name": "Channel of Rhythm", "centers": ["Throat", "Sacral"], "circuit": "Individual"},
    "16-48": {"name": "Channel of the Wavelength", "centers": ["Throat", "Spleen"], "circuit": "Individual"},
    "17-62": {"name": "Channel of Acceptance", "centers": ["Ajna", "Throat"], "circuit": "Individual"},
    "18-58": {"name": "Channel of Judgment", "centers": ["Root", "Spleen"], "circuit": "Individual"},
    "19-49": {"name": "Channel of Synthesis", "centers": ["Root", "Solar Plexus"], "circuit": "Individual"},
    "20-34": {"name": "Channel of Charisma", "centers": ["Throat", "Sacral"], "circuit": "Individual"},
    "20-57": {"name": "Channel of the Brainwave", "centers": ["Throat", "Spleen"], "circuit": "Individual"},
    "21-45": {"name": "Channel of the Money Line", "centers": ["Heart", "Throat"], "circuit": "Individual"},
    "23-43": {"name": "Channel of Structuring", "centers": ["Throat", "Ajna"], "circuit": "Individual"},
    "24-61": {"name": "Channel of Awareness", "centers": ["Head", "Ajna"], "circuit": "Individual"},
    "25-51": {"name": "Channel of Initiation", "centers": ["Heart", "G"], "circuit": "Individual"},
    "26-44": {"name": "Channel of Surrender", "centers": ["Throat", "Solar Plexus"], "circuit": "Individual"},
    "27-50": {"name": "Channel of Preservation", "centers": ["Sacral", "Spleen"], "circuit": "Individual"},
    "28-38": {"name": "Channel of Struggle", "centers": ["Root", "Solar Plexus"], "circuit": "Individual"},
    "29-46": {"name": "Channel of Discovery", "centers": ["Sacral", "G"], "circuit": "Individual"},
    "30-41": {"name": "Channel of Recognition", "centers": ["Solar Plexus", "Root"], "circuit": "Individual"},
    "32-54": {"name": "Channel of Transformation", "centers": ["Spleen", "Root"], "circuit": "Individual"},
    "35-36": {"name": "Channel of Transitoriness", "centers": ["Solar Plexus", "Throat"], "circuit": "Individual"},
    "37-40": {"name": "Channel of Community", "centers": ["Heart", "Solar Plexus"], "circuit": "Individual"},
    "39-55": {"name": "Channel of Emoting", "centers": ["Root", "Solar Plexus"], "circuit": "Individual"},
    "42-53": {"name": "Channel of Maturation", "centers": ["Sacral", "Root"], "circuit": "Individual"},
    "47-64": {"name": "Channel of Abstraction", "centers": ["Head", "Ajna"], "circuit": "Individual"},
}

# Center to Gates Mapping
CENTER_GATES = {
    "Head": [61, 63, 64],
    "Ajna": [47, 24, 4, 11, 43, 17],
    "Throat": [23, 8, 20, 16, 35, 45, 12, 33, 21, 56, 31, 7],
    "G": [10, 20, 25, 51, 15, 5, 26, 44, 29, 46],
    "Heart": [21, 40, 25, 51, 26, 44],
    "Sacral": [2, 14, 29, 30, 34, 35, 40, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
    "Solar Plexus": [12, 22, 35, 36, 37, 40, 41, 55, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
    "Spleen": [48, 57, 18, 28, 32, 50, 44, 50, 32, 28, 18, 48, 57],
    "Root": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
}

def get_activated_gates_from_numbers(numbers):
    """Extract gate numbers from planetary numbers (e.g., '42.5' -> 42)"""
    gates = []
    for number in numbers:
        if '.' in number:
            gate = int(number.split('.')[0])
            gates.append(gate)
    return gates

def find_defined_channels(activated_gates):
    """Find which channels are defined based on activated gates"""
    defined_channels = []
    
    for channel, info in HUMAN_DESIGN_CHANNELS.items():
        gate1, gate2 = map(int, channel.split('-'))
        
        if gate1 in activated_gates and gate2 in activated_gates:
            defined_channels.append({
                'channel': channel,
                'name': info['name'],
                'centers': info['centers'],
                'circuit': info['circuit'],
                'gates': [gate1, gate2]
            })
    
    return defined_channels

def determine_defined_centers(defined_channels):
    """Determine which centers are defined based on active channels"""
    defined_centers = set()
    
    for channel_info in defined_channels:
        for center in channel_info['centers']:
            defined_centers.add(center)
    
    return list(defined_centers)

def analyze_center_definitions(red_numbers, black_numbers):
    """Analyze center definitions from planetary numbers"""
    
    # Extract gates from both red and black numbers
    red_gates = get_activated_gates_from_numbers(red_numbers)
    black_gates = get_activated_gates_from_numbers(black_numbers)
    
    # Combine all activated gates
    all_activated_gates = list(set(red_gates + black_gates))
    
    # Find defined channels
    defined_channels = find_defined_channels(all_activated_gates)
    
    # Determine defined centers
    defined_centers = determine_defined_centers(defined_channels)
    
    return {
        'activated_gates': all_activated_gates,
        'defined_channels': defined_channels,
        'defined_centers': defined_centers,
        'red_gates': red_gates,
        'black_gates': black_gates
    }

if __name__ == "__main__":
    # Test with sample data
    red_numbers = ['42.5', '32.3', '48.6', '49.4', '16.2', '20.6', '9.2', '34.6', '27.5', '7.2', '17.6', '56.6', '14.4']
    black_numbers = ['62.3', '61.3', '1.3', '38.4', '58.3', '1.2', '44.3', '5.2', '9.5', '10.4', '10.2', '50.5', '50.4']
    
    result = analyze_center_definitions(red_numbers, black_numbers)
    
    print("ACTIVATED GATES:")
    print(f"Red gates: {result['red_gates']}")
    print(f"Black gates: {result['black_gates']}")
    print(f"All activated gates: {result['activated_gates']}")
    
    print("\nDEFINED CHANNELS:")
    for channel in result['defined_channels']:
        print(f"Channel {channel['channel']}: {channel['name']} ({channel['circuit']}) - Connects {channel['centers'][0]} ↔ {channel['centers'][1]}")
    
    print(f"\nDEFINED CENTERS: {result['defined_centers']}")

