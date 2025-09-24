# LLM RESPONSE: Automated QA Evaluation with LangSmith & Gemini

## Overview

This project automates the evaluation of LLM-generated answers to computer science questions using [LangSmith](https://smith.langchain.com/) and Google's Gemini model. It reads a dataset of questions and answers, generates predictions, and grades them using custom and LLM-based evaluators.

## Directory Structure

```
.env                  # Environment variables (API keys, config)
data.csv              # CSV file with questions and answers
eval.py               # Script to run evaluation experiments
main.py               # Script to create LangSmith dataset from CSV
prompt.txt            # Prompt template for grading
requirements.txt      # Python dependencies

```

## Setup

1. **Clone the repository** and navigate to the project folder.

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure API keys**:
   - Edit `.env` with your LangSmith and Google Gemini API keys.
   - Example:
     ```
     LANGCHAIN_API_KEY=your_langsmith_api_key
     GOOGLE_API_KEY=your_google_api_key
     ```

## Usage

### 1. Prepare the Dataset

- Ensure `data.csv` contains your questions and answers in the format:
  ```
  Question,Answer
  What is an algorithm?,A step-by-step set of operations to solve a problem or perform a task.
  ...
  ```

### 2. Create LangSmith Dataset

Run [`main.py`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/main.py) to upload the questions and answers to LangSmith:

```sh
python main.py
```

This will create a dataset named `test_data` in your LangSmith project.

### 3. Run Evaluation

Run [`eval.py`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/eval.py) to evaluate LLM-generated answers:

```sh
python eval.py
```

- The script uses Gemini to generate answers for each question.
- It grades each answer using:
  - A custom length-based metric.
  - An LLM-based QA evaluator using the prompt in [`prompt.txt`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/prompt.txt).

### 4. View Results

- Results are stored and viewable in your LangSmith dashboard under the experiment prefix `google-gemini`.

## Customization

- **Prompt**: Edit [`prompt.txt`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/prompt.txt) or the `template` variable in [`eval.py`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/eval.py) to change grading instructions.
- **Evaluation Metrics**: Add or modify evaluators in [`eval.py`](c:/Users/HP/Desktop/GenAI_Projects/LLM RESPONSE/eval.py).

## Troubleshooting

- Ensure your API keys are correct and active.
- Check that your LangSmith project name matches `.env`.
- For CSV parsing issues, ensure no extra commas in questions/answers.

## References

- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangChain Google Gemini Integration](https://python.langchain.com/docs/integrations/llms/google_genai)
- [Gemini Model](https://ai.google.dev/gemini)

## License

This project is for educational and research purposes.

---

**Contact:** For issues or questions, open an issue 
