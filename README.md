# PICBASIC Conversion Accuracy Evaluation

This project provides a framework for evaluating the accuracy of AI-generated conversions from PICBASIC code to modern programming languages like Python and C++.

## Project Structure

- `PROGRAM ORDER.ENTRY.txt` - Original PICBASIC order entry system code
- `HANGMAN.GAME` - Original PICBASIC hangman game code
- `Order Entry/` - Folder containing AI-generated conversions of the order entry system
- `Hangman game/` - Folder containing AI-generated conversions of the hangman game
- `evaluations/` - Folder containing detailed evaluation reports for each AI model and source file
- `accuracy_evaluation_plan.md` - Comprehensive plan for evaluation methodology
- `accuracy_results.md` - Summary table of evaluation results
- `evaluation_checklist.md` - Detailed checklist for consistent evaluations
- `evaluation_helper.py` - Script to assist in the evaluation process

## Evaluation Results Summary

The evaluation of PICBASIC to modern code conversion across different AI models has been completed for the Order Entry program. Here are the key results:

| AI Model   | Total Score (100) |
| ---------- | ----------------- |
| Claude-3.7 | 98                |
| Gemini     | 91                |
| ChatGPT    | 77                |

Claude-3.7 demonstrates superior conversion capabilities, particularly in structural adaptation and code quality metrics. Gemini also performs very well, with strong typing and data encapsulation. ChatGPT provides a functional conversion that remains closer to the procedural style of the original.

## Key Findings

1. **Object-Oriented Transformation**: The most successful conversions transformed procedural PICBASIC code into well-structured object-oriented Python.

2. **Data Encapsulation**: Converting flat variable structures to appropriate classes/data structures significantly improved code quality.

3. **Documentation Quality**: All models provided good documentation, with Claude-3.7 excelling in comprehensive docstrings.

4. **Modernization Balance**: The best conversions balanced preserving original functionality while leveraging modern language features.

## Setup

1. Clone this repository
2. Review the original PICBASIC source files and the converted files in their respective folders
3. Familiarize yourself with the evaluation metrics in `accuracy_evaluation_plan.md`

## Evaluation Process

1. **Run the helper script** to get initial statistics:

   ```
   python evaluation_helper.py order_entry
   ```

2. **Use the checklist** in `evaluation_checklist.md` to systematically evaluate each conversion

3. **Create detailed evaluations** for each AI model and source file combination:

   - Use the template from `accuracy_evaluation_plan.md`
   - Save the evaluations in the `evaluations/` folder following the naming convention:
     - `{ai_model}_{source_file}.md` (e.g., `claude_order_entry.md`)

4. **Update the summary table** in `accuracy_results.md` with the scores from your evaluations

5. **Analyze the results** to identify strengths and weaknesses across AI models

## Adding New AI Models

To add evaluations for additional AI models:

1. Generate conversions using your AI model of choice
2. Save the converted code in the appropriate folder (`Order Entry/` or `Hangman game/`)
3. Update the `evaluation_helper.py` script to include the new model
4. Follow the standard evaluation process

## License

This project is intended for educational and research purposes.
