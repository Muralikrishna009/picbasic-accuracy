"""
PICBASIC Conversion Evaluation Helper

This script analyzes original PICBASIC code and corresponding converted code files
to generate preliminary statistics that can assist in the evaluation process.
"""

import os
import re
import sys
from collections import defaultdict, Counter

def count_code_structures(code, language):
    """Count basic code structures in the provided code string."""
    
    stats = defaultdict(int)
    
    if language == 'picbasic':
        # Count PICBASIC structures
        stats['if_statements'] = len(re.findall(r'\bIF\b.*\bTHEN\b', code, re.IGNORECASE))
        stats['gosub'] = len(re.findall(r'\bGOSUB\b', code, re.IGNORECASE))
        stats['return'] = len(re.findall(r'\bRETURN\b', code, re.IGNORECASE))
        stats['goto'] = len(re.findall(r'\bGOTO\b', code, re.IGNORECASE))
        stats['input'] = len(re.findall(r'\bINPUT\b', code, re.IGNORECASE))
        stats['print'] = len(re.findall(r'\bCRT\b', code, re.IGNORECASE))
        stats['read'] = len(re.findall(r'\bREAD\b', code, re.IGNORECASE))
        stats['open'] = len(re.findall(r'\bOPEN\b', code, re.IGNORECASE))
        stats['end'] = len(re.findall(r'\bEND\b', code, re.IGNORECASE))
        
        # Extract variable names
        vars_pattern = r'([A-Z][A-Z0-9\.\_]+)\s*='
        stats['variables'] = len(set(re.findall(vars_pattern, code, re.IGNORECASE)))
        
        # Extract label/subroutine names
        labels = re.findall(r'^([A-Z][A-Z0-9\.\_]+):', code, re.IGNORECASE | re.MULTILINE)
        stats['labels'] = len(labels)
        
        # Count lines
        stats['total_lines'] = len(code.split('\n'))
        
    elif language == 'python':
        # Count Python structures
        stats['if_statements'] = len(re.findall(r'\bif\b', code))
        stats['functions'] = len(re.findall(r'\bdef\b', code))
        stats['imports'] = len(re.findall(r'\bimport\b', code))
        stats['classes'] = len(re.findall(r'\bclass\b', code))
        stats['for_loops'] = len(re.findall(r'\bfor\b', code))
        stats['while_loops'] = len(re.findall(r'\bwhile\b', code))
        stats['print'] = len(re.findall(r'\bprint\b', code))
        stats['input'] = len(re.findall(r'\binput\b', code))
        
        # Count docstrings and comments
        docstrings = re.findall(r'""".*?"""', code, re.DOTALL)
        comments = re.findall(r'#.*?$', code, re.MULTILINE)
        stats['docstrings'] = len(docstrings)
        stats['comments'] = len(comments)
        
        # Count variables (rough approximation)
        var_assignments = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code)
        stats['variables'] = len(set(var_assignments))
        
        # Count lines
        stats['total_lines'] = len(code.split('\n'))
    
    elif language == 'cpp':
        # Count C++ structures
        stats['if_statements'] = len(re.findall(r'\bif\b\s*\(', code))
        stats['functions'] = len(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(', code))
        stats['classes'] = len(re.findall(r'\bclass\b', code))
        stats['for_loops'] = len(re.findall(r'\bfor\b\s*\(', code))
        stats['while_loops'] = len(re.findall(r'\bwhile\b\s*\(', code))
        stats['includes'] = len(re.findall(r'#include', code))
        stats['cout'] = len(re.findall(r'std::cout|cout', code))
        stats['cin'] = len(re.findall(r'std::cin|cin', code))
        
        # Count comments
        single_comments = re.findall(r'//.*?$', code, re.MULTILINE)
        multi_comments = re.findall(r'/\*.*?\*/', code, re.DOTALL)
        stats['comments'] = len(single_comments) + len(multi_comments)
        
        # Count variables (rough approximation)
        var_types = ['int', 'float', 'double', 'char', 'bool', 'string', 'vector', 'std::string', 'std::vector']
        var_pattern = '|'.join(var_types)
        var_declarations = re.findall(rf'\b({var_pattern})\b\s+([a-zA-Z_][a-zA-Z0-9_]*)', code)
        stats['variables'] = len(set([v[1] for v in var_declarations]))
        
        # Count lines
        stats['total_lines'] = len(code.split('\n'))
    
    return stats

def analyze_files(original_file, converted_files):
    """Analyze original PICBASIC and converted files."""
    
    # Read original file
    with open(original_file, 'r') as f:
        original_code = f.read()
    
    # Get statistics for original code
    original_stats = count_code_structures(original_code, 'picbasic')
    
    # Process each converted file
    results = {}
    for model, file_path in converted_files.items():
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} does not exist. Skipping.")
            continue
            
        with open(file_path, 'r') as f:
            converted_code = f.read()
        
        # Detect language from file extension
        if file_path.endswith('.py'):
            language = 'python'
        elif file_path.endswith('.cpp') or file_path.endswith('.c'):
            language = 'cpp'
        else:
            print(f"Warning: Unknown language for file {file_path}. Assuming Python.")
            language = 'python'
            
        converted_stats = count_code_structures(converted_code, language)
        results[model] = {
            'language': language,
            'stats': converted_stats
        }
    
    # Print summary
    print(f"Analysis for {os.path.basename(original_file)}")
    print("=" * 80)
    print(f"Original PICBASIC: {original_stats['total_lines']} lines")
    print(f"  - IF statements: {original_stats['if_statements']}")
    print(f"  - GOSUBs: {original_stats['gosub']}")
    print(f"  - Labels/Routines: {original_stats['labels']}")
    print(f"  - Variables: {original_stats['variables']}")
    print()
    
    for model, data in results.items():
        print(f"{model} ({data['language']}): {data['stats']['total_lines']} lines")
        print(f"  - {'Functions' if data['language'] == 'python' else 'Functions'}: {data['stats']['functions']}")
        print(f"  - IF statements: {data['stats']['if_statements']}")
        print(f"  - {'Docstrings' if data['language'] == 'python' else 'Comments'}: {data['stats']['docstrings'] if data['language'] == 'python' else data['stats']['comments']}")
        print(f"  - Variables: {data['stats']['variables']}")
        print()
    
    return {
        'original': original_stats,
        'conversions': results
    }

def calculate_structural_similarity(original_stats, converted_stats, language):
    """Calculate a rough structural similarity score based on code statistics."""
    score = 0.0
    total_points = 0.0
    
    # Compare control structures
    if language == 'python':
        # Check if functions roughly match labels/subroutines
        if abs(original_stats['labels'] - converted_stats['functions']) <= 2:
            score += 10
        elif abs(original_stats['labels'] - converted_stats['functions']) <= 5:
            score += 5
        total_points += 10
        
        # Check if control flow is preserved
        if abs(original_stats['if_statements'] - converted_stats['if_statements']) <= 3:
            score += 10
        elif abs(original_stats['if_statements'] - converted_stats['if_statements']) <= 6:
            score += 5
        total_points += 10
        
    elif language == 'cpp':
        # Similar checks for C++
        if abs(original_stats['labels'] - converted_stats['functions']) <= 2:
            score += 10
        elif abs(original_stats['labels'] - converted_stats['functions']) <= 5:
            score += 5
        total_points += 10
        
        if abs(original_stats['if_statements'] - converted_stats['if_statements']) <= 3:
            score += 10
        elif abs(original_stats['if_statements'] - converted_stats['if_statements']) <= 6:
            score += 5
        total_points += 10
    
    # Calculate percentage
    if total_points > 0:
        return (score / total_points) * 100
    return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluation_helper.py [order_entry|hangman]")
        sys.exit(1)
    
    example = sys.argv[1].lower()
    
    if example == 'order_entry':
        original_file = 'PicBasic-Example1-OrderEntry.txt'
        converted_files = {
            'ChatGPT': 'Order Entry/ChatGPT.py',
            'Claude-3.7': 'Order Entry/Claude-3.7-sonnet.py',
            'Gemini': 'Order Entry/Gemini.py'
        }
    elif example == 'hangman':
        original_file = 'PicBasic-Example2-HangmanGame.txt'
        converted_files = {
            'ChatGPT': 'Hangman game/ChatGPT.py',
            'Claude-3.7': 'Hangman game/Claude-3.7-sonnet.py'
        }
    else:
        print(f"Unknown example: {example}")
        print("Valid options: order_entry, hangman")
        sys.exit(1)
    
    results = analyze_files(original_file, converted_files)
    
    print("\nStructural Similarity Scores (rough estimate):")
    print("=" * 80)
    
    for model, data in results['conversions'].items():
        similarity = calculate_structural_similarity(
            results['original'], 
            data['stats'], 
            data['language']
        )
        print(f"{model}: {similarity:.1f}% structural similarity")

if __name__ == "__main__":
    main() 