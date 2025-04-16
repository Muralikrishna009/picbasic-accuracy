# PICBASIC Conversion Evaluation Checklist

Use this checklist when evaluating each AI-generated conversion to ensure consistent and thorough assessments.

## Setup

- [ ] Run the evaluation helper script: `python evaluation_helper.py [order_entry|hangman]`
- [ ] Open original PICBASIC file side-by-side with the converted file
- [ ] Note the language of the conversion (Python, C++, etc.)

## Functional Accuracy (40 points)

### Core Logic Implementation (20 points)

- [ ] Verify all business rules are correctly implemented
- [ ] Check that key algorithms are preserved
- [ ] Confirm calculations and data transformations are equivalent
- [ ] Ensure program flow matches the original intent

### Control Flow Preservation (10 points)

- [ ] Check that all conditional statements (IF-THEN-ELSE) are correctly converted
- [ ] Verify all loops have equivalent behavior
- [ ] Confirm that GOSUB routines are properly converted to functions or methods
- [ ] Ensure GOTO statements are handled appropriately (restructured or eliminated)
- [ ] Check that program termination conditions are preserved

### Data Operations (10 points)

- [ ] Verify all file operations (OPEN, READ, WRITE) are correctly implemented
- [ ] Check that variable assignments and data transformations are accurate
- [ ] Confirm that input/output operations work as expected
- [ ] Ensure data validations are preserved

## Structural Adaptation (30 points)

### Language Paradigm Adaptation (15 points)

- [ ] Assess how well PICBASIC concepts are translated to the target language's paradigm
- [ ] Check for appropriate use of functions vs. methods vs. classes
- [ ] Verify that global variables are handled appropriately
- [ ] Confirm that routines are logically grouped

### Modern Programming Practices (10 points)

- [ ] Check for appropriate use of data structures (lists, dictionaries, etc.)
- [ ] Verify use of modern control structures
- [ ] Assess modularity and code organization
- [ ] Check for use of language-specific features where appropriate

### Error Handling (5 points)

- [ ] Verify that error conditions are properly handled
- [ ] Check for input validation
- [ ] Confirm that exceptional cases are addressed
- [ ] Assess defensive programming techniques

## Code Quality (20 points)

### Readability (5 points)

- [ ] Check naming conventions (variables, functions, classes)
- [ ] Assess code formatting and structure
- [ ] Verify appropriate use of whitespace and indentation
- [ ] Check for intuitive organization

### Maintainability (5 points)

- [ ] Verify functions/methods have appropriate scope and size
- [ ] Assess coupling between components
- [ ] Check for duplicated code
- [ ] Confirm logical organization of code elements

### Efficiency (5 points)

- [ ] Check for appropriate algorithm choices
- [ ] Verify efficient use of language features
- [ ] Assess performance considerations
- [ ] Check for unnecessary operations

### Documentation (5 points)

- [ ] Verify presence of docstrings or comments for functions/methods
- [ ] Check for explanations of complex logic
- [ ] Assess overall documentation quality
- [ ] Confirm header comments explaining program purpose

## Additional Features (10 points)

### Enhanced Functionality (5 points)

- [ ] Identify improvements beyond direct translation
- [ ] Check for sensible additions that enhance usability
- [ ] Verify that enhancements don't break core functionality
- [ ] Assess value of added features

### Modernization (5 points)

- [ ] Check for use of language-specific features that improve the code
- [ ] Verify modernized UI/UX where applicable
- [ ] Assess overall approach to modernization
- [ ] Confirm balance between faithfulness to original and modern improvements

## Final Assessment

- [ ] Calculate scores for each section
- [ ] Sum up the total score (out of 100)
- [ ] Write detailed comments highlighting strengths and weaknesses
- [ ] Add the results to the summary table in `accuracy_results.md`
- [ ] Create a detailed evaluation document for this AI model and source file
