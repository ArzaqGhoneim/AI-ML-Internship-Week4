# AI Knowledge Assistant — Week 4 Capstone

**Retrieval-Augmented Knowledge Assistant using a tested TF-IDF baseline and an extended LangChain + FAISS + LangGraph prototype.**

## Overview
This project demonstrates a small, source-aware knowledge assistant. The repository contains a dependency-light TF-IDF baseline that was executed locally, plus a Google Colab-friendly extended notebook using sentence-transformer embeddings, FAISS semantic retrieval, and LangGraph orchestration. The advanced notebook is documented as **not locally executed** because those optional packages are not installed in the current runtime.

## Problem Statement
A knowledge assistant should retrieve information relevant to a user question and expose the supporting source documents rather than producing an unsupported answer. This capstone explores that workflow with both lexical TF-IDF retrieval and a semantic RAG-style architecture.

## Objectives
- Prepare a small self-contained knowledge base.
- Retrieve relevant evidence with similarity scores.
- Handle empty and out-of-scope questions conservatively.
- Demonstrate embeddings + FAISS + LangGraph in a reproducible notebook.
- Attribute responses to source titles.
- Test the baseline automatically.

## Key Features
- 9 focused knowledge documents.
- TF-IDF + cosine-similarity baseline.
- Minimum similarity threshold to reduce misleading matches.
- Extractive fallback when no LLM key is available.
- Optional LangChain/Hugging Face embeddings + FAISS.
- Optional LangGraph workflow.
- Optional LangSmith tracing; credentials are never stored.

## Architecture
User Question → Processing → TF-IDF or Sentence-Transformer Representation → Retrieval → Relevant Context + Sources → Evidence/Answer → Evaluation + Optional Observability.

See `docs/ARCHITECTURE.png`.

## Technologies
Python, scikit-learn, pytest, LangChain, sentence-transformers, FAISS, LangGraph, optional LangSmith.

## Repository Structure
```text
AI_Knowledge_Assistant_Week4/
├── README.md
├── requirements.txt
├── app.py
├── src/
├── tests/
├── notebooks/
├── docs/
└── evidence/
```

## Installation
```bash
pip install -r requirements.txt
```
For the tested baseline, the required local dependencies are scikit-learn and pytest. The extended dependencies can be installed in Colab when needed.

## Google Colab
1. Upload `notebooks/AI_Knowledge_Assistant_Week4_NextSteps.ipynb`.
2. Run the dependency cell.
3. Run cells in order.
4. The first semantic-embedding run downloads `sentence-transformers/all-MiniLM-L6-v2`; this is a small model but still requires internet access.
5. Keep screenshots only for cells that actually execute successfully.
6. LangSmith tracing is optional and requires private credentials configured through Colab Secrets/environment variables.

## Usage
```bash
python app.py
```
Example questions include classification metrics, RAG, overfitting, and an out-of-scope question.

## Testing
```bash
pytest -q
```
The current evidence folder contains the **actual local test output** from this environment.

## Verified Results
The baseline tests were executed locally on Python 3.13.5 with scikit-learn and pytest available. See `evidence/test_results.txt` for the exact output. The demo was also executed and its real output is stored in `evidence/demo_output.txt`.

The extended FAISS/LangGraph notebook was **not executed in this runtime** because the optional packages are not installed here. Its cells are prepared for Google Colab and retain the user's original project objectives.

## Limitations
- TF-IDF is lexical and does not capture semantic similarity as well as transformer embeddings.
- The no-key fallback returns retrieved evidence; it does not generate a new LLM answer.
- FAISS/sentence-transformer/LangGraph execution remains pending in the available local runtime.
- No live deployment or public GitHub URL is claimed.

## Future Improvements
Add chunking for longer documents, semantic reranking, a stronger evaluation set, citation formatting, configurable LLM providers, persistence for the vector index, and a deployed UI/API.

## Internship Acknowledgment
This capstone was prepared as part of the **Skill Set Go EduTech Artificial Intelligence and Machine Learning internship**, Week 4.
