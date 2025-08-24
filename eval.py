from langsmith import Client
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.prompt import PromptTemplate
from langsmith.evaluation import LangChainStringEvaluator
from langsmith.schemas import Run, Example
from langsmith import evaluate


load_dotenv()
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


client = Client()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)


template = """You are an expert professor specialized in grading students' answers to questions.
You are grading the following question:
{query}
Here is the real answer:
{answer}
You are grading the following predicted answer:
{result}
Respond with CORRECT or INCORRECT:
Grade:
"""

prompt = PromptTemplate(input_variables=["query", "answer", "result"], template=template)


qa_evaluator = LangChainStringEvaluator("qa", config={"llm": llm, "prompt": prompt})

def evaluate_length(run: Run, example: Example) -> dict:
    prediction = run.outputs.get("output") or ""
    required = example.outputs.get("answer") or ""
    score = int(len(prediction) < 2 * len(required))
    return {"key": "length", "score": score}

def my_app(question):
    result = llm.invoke(question)
    return result.content


def langsmith_app(inputs):
    output = my_app(inputs["question"])
    return {"output": output}

experiment = evaluate(
    langsmith_app,
    data="test_data",
    evaluators=[evaluate_length, qa_evaluator],
    experiment_prefix="google-gemini"
)

