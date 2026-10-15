from src.knowledge_assistant import KnowledgeAssistant
from src.retrieval import format_results


def main():
    assistant=KnowledgeAssistant()
    questions=[
        "Which measures can evaluate a classification model?",
        "What is RAG and how does it work?",
        "How can overfitting be reduced?",
        "What is the weather on Mars today?",
    ]
    for q in questions:
        print("="*72); print("Question:",q)
        results=assistant.retrieve(q)
        print(format_results(results))
        if not results: print("Status: NO RELEVANT EVIDENCE")
        else: print("Status: relevant evidence retrieved")

if __name__ == '__main__': main()
