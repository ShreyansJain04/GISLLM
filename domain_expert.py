"""Enhanced Domain Expert with Advanced RAG and Multi-LLM Support."""
import os
from pathlib import Path
from typing import Tuple, List, Optional, Dict, Any, Union

from advanced_rag import AdvancedRAGSystem
from llm_providers import llm_manager
from sentence_transformers import SentenceTransformer, util
import torch


# Load a pre-trained model for sentence similarity
# This model is lightweight and effective for semantic similarity tasks
similarity_model = SentenceTransformer('all-MiniLM-L6-v2')


# Initialize the advanced RAG system
rag_system = AdvancedRAGSystem(
    docs_path=Path('docs'),
    embedding_model='all-MiniLM-L6-v2',
    rerank_model='cross-encoder/ms-marco-MiniLM-L-6-v2',
    chunk_size=512,
    chunk_overlap=128
)


def query_domain_expert(
    prompt: str, 
    context: str = "", 
    citations: Optional[List[str]] = None,
    provider: Optional[str] = None,
    temperature: float = 0.7
) -> str:
    """
    Query the domain expert LLM with advanced RAG context.
    
    Args:
        prompt: The question or request
        context: Optional pre-retrieved context
        citations: Optional citations for the context
        provider: Specific LLM provider to use (None = use default)
        temperature: LLM temperature setting
    
    Returns:
        Generated response from the domain expert
    """
    # Enhance prompt with context and citations
    if context:
        if citations:
            citations_text = "\n".join([f"Source: {cite}" for cite in citations])
            enhanced_prompt = (
                f"You are a domain expert tutor. Use the following context to answer accurately. "
                f"Base your answer ONLY on the provided context. If the context doesn't contain "
                f"enough information, say so clearly. Include citations from the sources listed.\n\n"
                f"Context:\n{context}\n\n"
                f"Sources:\n{citations_text}\n\n"
                f"Question: {prompt}\n\n"
                f"Answer (include citations where relevant):"
            )
        else:
            enhanced_prompt = (
                f"You are a domain expert tutor. Use the following context to answer:\n\n"
                f"Context:\n{context}\n\n"
                f"Question: {prompt}"
            )
    else:
        enhanced_prompt = f"You are a domain expert tutor. {prompt}"
    
    # Generate response using LLM manager
    try:
        response = llm_manager.generate(
            enhanced_prompt, 
            provider=provider,
            temperature=temperature
        )
        return response
    except Exception as e:
        # Fallback response if LLM fails
        return f"[Error: {str(e)}] Unable to generate response. Please check LLM configuration."


def retrieve_context_with_citations(topic: str, k: int = 5) -> Tuple[str, List[str]]:
    """
    Retrieve context using advanced RAG system.
    
    Returns:
        Tuple of (context, citations)
    """
    context, citations, _ = rag_system.retrieve(
        query=topic,
        k=k,
        use_reranking=True,
        alpha=0.7  # Favor semantic search
    )
    return context, citations


def explain_concept(topic: str, detail_level: str = "standard") -> str:
    """
    Explain a concept with appropriate detail level.
    
    Args:
        topic: The concept to explain
        detail_level: "simple", "standard", or "advanced"
    """
    # Retrieve relevant context
    context, citations = retrieve_context_with_citations(topic)
    
    if not context:
        # Check available sources
        stats = rag_system.get_statistics()
        if stats['total_documents'] == 0:
            return (
                f"No documents found in the docs folder. Please add relevant PDF or text files "
                f"to get accurate, source-based explanations about '{topic}'."
            )
        else:
            sources = list(stats['source_breakdown'].keys())
            return (
                f"I don't have specific information about '{topic}' in the available documents. "
                f"Available sources: {', '.join(sources)}. Please ensure your query matches "
                f"content in these documents or add relevant documents to the docs folder."
            )
    
    # Adjust prompt based on detail level
    prompts = {
        "simple": f"Explain '{topic}' in simple terms that a beginner can understand. Use analogies if helpful.",
        "standard": f"Explain the concept of '{topic}' clearly and comprehensively.",
        "advanced": f"Provide an in-depth explanation of '{topic}' including technical details and nuances."
    }
    
    prompt = prompts.get(detail_level, prompts["standard"])
    return query_domain_expert(prompt, context, citations)


def generate_example(topic: str, difficulty: str = "medium") -> str:
    """
    Generate an example for a topic with specified difficulty.
    
    Args:
        topic: The topic for the example
        difficulty: "easy", "medium", or "hard"
    """
    context, citations = retrieve_context_with_citations(topic)
    
    if not context:
        stats = rag_system.get_statistics()
        if stats['total_documents'] == 0:
            return (
                f"No documents found. Please add relevant documents to get examples based on "
                f"your specific materials."
            )
        else:
            sources = list(stats['source_breakdown'].keys())
            return (
                f"I don't have specific examples for '{topic}' in the available documents. "
                f"Available sources: {', '.join(sources)}."
            )
    
    difficulty_prompts = {
        "easy": f"Provide a simple, straightforward example for '{topic}' that clearly illustrates the basic concept.",
        "medium": f"Provide a practical worked example for '{topic}' that demonstrates typical usage.",
        "hard": f"Provide a challenging example for '{topic}' that explores edge cases or advanced applications."
    }
    
    prompt = difficulty_prompts.get(difficulty, difficulty_prompts["medium"])
    return query_domain_expert(prompt, context, citations)


def generate_question(topic: str, previous_questions: Optional[List[Union[str, Dict]]] = None, difficulty: str = "medium", question_type: str = "objective") -> Dict:
    """Generate a question for a given topic, ensuring it's not a semantic duplicate.
    
    Args:
        topic: The topic to generate a question for
        previous_questions: List of previously asked questions (strings or dicts) to avoid repetition
        difficulty: Difficulty level ("easy", "medium", "hard")
        question_type: Type of question ("objective", "analytical", "synthesis")
        
    Returns:
        Dict containing question text and options if objective
    """
    if previous_questions is None:
        previous_questions = []
   
    # Extract question texts from previous_questions
    previous_texts = []
    for q in previous_questions:
        if isinstance(q, dict):
            if 'text' in q:
                previous_texts.append(q['text'])
            elif 'question' in q:
                previous_texts.append(q['question'])
        elif isinstance(q, str):
            previous_texts.append(q)

    max_retries = 3
    for _ in range(max_retries):
        # Try to get context for the topic
        try:
            context = _retrieve_context(topic)
        except Exception as e:
            print(f"RAG retrieval failed: {e}")
            # Fallback to generating question without context
            return _generate_fallback_question(topic, previous_texts, difficulty, question_type)
        
        # Generate a question
        generated_question = _generate_question_from_context(context, topic, previous_texts, difficulty, question_type)

        # Check for semantic duplicates
        if not is_question_duplicate(generated_question["text"], previous_texts):
            return generated_question
    
    # If all retries fail, return the last generated question or a fallback
    return generated_question or _generate_fallback_question(topic, previous_texts, difficulty, question_type)


def _generate_question_from_context(context: str, topic: str, previous_texts: List[str], difficulty: str, question_type: str) -> Dict:
    """Helper function to generate a question from a given context."""
    if question_type == "objective":
        # Build prompt for multiple choice question
        prompt = (
            f"Create a multiple choice question about '{topic}' based on the provided context.\n"
            f"Difficulty level: {difficulty}\n"
            "Requirements:\n"
            "1. Question should test understanding, not just recall\n"
            "2. All options should be plausible and related to the topic\n"
            "3. Only one option should be correct\n"
            "4. Options should be clear and concise\n"
            "Format:\n"
            "QUESTION: <question text>\n"
            "CORRECT: <correct answer>\n"
            "WRONG1: <plausible wrong answer 1>\n"
            "WRONG2: <plausible wrong answer 2>\n"
            "WRONG3: <plausible wrong answer 3>\n"
            "EXPLANATION: <brief explanation of why the correct answer is right>"
        )
        
        if previous_texts:
            prompt += "\nAvoid these previous questions:\n" + "\n".join(f"- {q}" for q in previous_texts)
        
        # Get response from LLM
        response = query_domain_expert(prompt, context)
        
        # Parse response
        try:
            lines = response.split('\n')
            question_text = next(line.replace('QUESTION: ', '') for line in lines if line.startswith('QUESTION:'))
            correct_ans = next(line.replace('CORRECT: ', '') for line in lines if line.startswith('CORRECT:'))
            wrong1 = next(line.replace('WRONG1: ', '') for line in lines if line.startswith('WRONG1:'))
            wrong2 = next(line.replace('WRONG2: ', '') for line in lines if line.startswith('WRONG2:'))
            wrong3 = next(line.replace('WRONG3: ', '') for line in lines if line.startswith('WRONG3:'))
            explanation = next(line.replace('EXPLANATION: ', '') for line in lines if line.startswith('EXPLANATION:'))
            
            # Randomize option order
            options = [correct_ans, wrong1, wrong2, wrong3]
            import random
            random.shuffle(options)
            correct_idx = options.index(correct_ans)
            
            return {
                "text": question_text,
                "options": options,
                "correct_option": correct_idx,
                "explanation": explanation,
                "type": "objective",
                "difficulty": difficulty
            }
        except Exception as e:
            print(f"Error parsing LLM response: {e}")
            # Fallback to basic question if parsing fails
            return _generate_fallback_question(topic, previous_texts, difficulty, question_type)
    else:
        # Generate subjective/analytical question
        prompt = (
            f"Create a {question_type} question about '{topic}' that requires {difficulty} level understanding.\n"
            "The question should encourage critical thinking and detailed explanation."
        )
        if previous_texts:
            prompt += "\nAvoid these previous questions:\n" + "\n".join(f"- {q}" for q in previous_texts)
        
        question_text = query_domain_expert(prompt, context)
        return {
            "text": question_text,
            "type": "subjective",
            "difficulty": difficulty
        }


def check_answer(question: Dict, answer: str) -> Tuple[bool, str]:
    """Check if the answer is correct.
    
    Args:
        question: Question dict containing text and options if objective
        answer: User's answer
        
    Returns:
        Tuple of (is_correct, feedback)
    """
    
    # print(f"check_answer received question: {question}")
    # print(f"check_answer received answer: {answer}")
    # print(f"Question type: {question.get('type')}")
    # print(f"Question options: {question.get('options', [])}")
    # print(f"Question correct_option: {question.get('correct_option')}")
    
    if question.get("type") == "objective":
        try:
            selected_option = int(answer)
            is_correct = selected_option == question["correct_option"]
            
            feedback = question.get("explanation", "")
            if is_correct:
                feedback = "✅ Correct! " + feedback
            else:
                correct_text = question["options"][question["correct_option"]]
                feedback = f"❌ Incorrect. The correct answer was: {correct_text}\n\nExplanation: {feedback}"
            
            return is_correct, feedback
        except ValueError:
            return False, "Please enter a valid option number (0-3)"
    else:
        # For subjective questions, use semantic similarity
        context = _retrieve_context(question["text"])
        
        # Build evaluation prompt
        prompt = (
            f"Question: {question['text']}\n"
            f"Student's answer: {answer}\n\n"
            "Evaluate the answer based on:\n"
            "1. Accuracy of information\n"
            "2. Completeness of explanation\n"
            "3. Understanding of concepts\n\n"
            "Provide:\n"
            "SCORE: (number between 0 and 1)\n"
            "FEEDBACK: (constructive feedback explaining the score)"
        )
        
        response = query_domain_expert(prompt, context)
        
        try:
            # Parse score and feedback
            score_line = next(line for line in response.split('\n') if line.startswith('SCORE:'))
            score = float(score_line.replace('SCORE:', '').strip())
            
            feedback_line = next(line for line in response.split('\n') if line.startswith('FEEDBACK:'))
            feedback = feedback_line.replace('FEEDBACK:', '').strip()
            
            # Consider score >= 0.8 as correct for subjective questions
            is_correct = score >= 0.8
            
            return is_correct, feedback
        except Exception as e:
            print(f"Error parsing evaluation response: {e}")
            # Fallback scoring
            return False, "Unable to evaluate answer. Please try again."


def generate_hint(question: str, difficulty_level: int = 1) -> str:
    """
    Generate a hint for a question with varying levels of help.
    
    Args:
        question: The question to provide a hint for
        difficulty_level: 1 (subtle hint) to 3 (explicit guidance)
    """
    context, citations = retrieve_context_with_citations(question)
    
    hint_prompts = {
        1: f"Provide a subtle hint for this question without giving away the answer: {question}",
        2: f"Provide a helpful hint that guides toward the answer for: {question}",
        3: f"Provide clear guidance toward answering this question: {question}"
    }
    
    prompt = hint_prompts.get(difficulty_level, hint_prompts[1])
    return query_domain_expert(prompt, context, citations)


def generate_summary(topic: str, length: str = "medium") -> str:
    """
    Generate a summary of a topic.
    
    Args:
        topic: The topic to summarize
        length: "short", "medium", or "long"
    """
    context, citations = retrieve_context_with_citations(topic)
    
    if not context:
        stats = rag_system.get_statistics()
        sources = list(stats['source_breakdown'].keys()) if stats['total_documents'] > 0 else []
        if sources:
            return (
                f"I don't have specific information about '{topic}' to summarize. "
                f"Available sources: {', '.join(sources)}."
            )
        else:
            return "No documents available to create a summary. Please add relevant documents to the docs folder."
    
    length_instructions = {
        "short": "Give a brief 2-3 sentence summary",
        "medium": "Give a concise paragraph summary",
        "long": "Give a comprehensive summary with key points"
    }
    
    prompt = f"{length_instructions[length]} of '{topic}' based on the provided context."
    return query_domain_expert(prompt, context, citations)


def generate_quiz(topic: str, num_questions: int = 5, mix_types: bool = True) -> List[Dict[str, Any]]:
    """
    Generate a complete quiz on a topic.
    
    Args:
        topic: The topic for the quiz
        num_questions: Number of questions to generate
        mix_types: Whether to mix different question types
    
    Returns:
        List of quiz questions with structure
    """
    context, citations = retrieve_context_with_citations(topic, k=10)  # Get more context for quiz
    
    if not context:
        return [{
            "question": f"No source materials available for {topic}",
            "type": "error",
            "difficulty": "n/a"
        }]
    
    quiz_questions = []
    question_types = ["conceptual", "analytical", "application"] if mix_types else ["conceptual"]
    difficulties = ["easy", "medium", "hard"]
    
    for i in range(num_questions):
        q_type = question_types[i % len(question_types)]
        q_difficulty = difficulties[min(i // len(question_types), 2)]  # Gradually increase difficulty
        
        # Generate unique question
        previous = [q["question"] for q in quiz_questions]
        question = generate_question(topic, previous, q_difficulty, q_type)
        
        quiz_questions.append({
            "question": question,
            "type": q_type,
            "difficulty": q_difficulty,
            "topic": topic
        })
    
    return quiz_questions


def get_available_sources() -> List[str]:
    """Get list of available document sources."""
    stats = rag_system.get_statistics()
    return list(stats['source_breakdown'].keys())


def show_available_sources() -> str:
    """Show what document sources are available with statistics."""
    stats = rag_system.get_statistics()
    
    if stats['total_documents'] == 0:
        return "No documents found in the docs folder. Please add PDF or text files."
    
    lines = [
        f"Total documents: {stats['total_documents']}",
        f"Total sources: {stats['total_sources']}",
        f"Index type: {stats['index_type']}",
        f"Hybrid search: {'Enabled' if stats['has_sparse_index'] else 'Semantic only'}",
        f"Reranking: {'Enabled' if stats['has_reranker'] else 'Disabled'}",
        "",
        "Document sources:"
    ]
    
    for source, count in stats['source_breakdown'].items():
        lines.append(f"  - {source}: {count} chunks")
    
    return "\n".join(lines)


def search_specific_source(source_name: str, query: str) -> str:
    """Search within a specific document source."""
    # Filter search to specific source
    context, citations, docs = rag_system.retrieve(
        query=query,
        filters={"source": source_name},
        k=5
    )
    
    if not context:
        return f"No relevant content found for '{query}' in source '{source_name}'."
    
    prompt = f"Answer the following question based on the specific source: {query}"
    return query_domain_expert(prompt, context, citations)


def get_llm_info() -> Dict[str, Any]:
    """Get information about available LLM providers."""
    return llm_manager.list_providers()


def set_llm_provider(provider: str) -> bool:
    """Set the active LLM provider."""
    try:
        llm_manager.set_active_provider(provider)
        return True
    except ValueError:
        return False


# Legacy functions for backward compatibility
def _retrieve_context(topic: str) -> str:
    """Legacy retrieval helper - kept for backward compatibility."""
    context, _ = retrieve_context_with_citations(topic)
    return context


def _generate_fallback_question(topic: str, previous_texts: List[str], difficulty: str, question_type: str) -> Dict:
    """Generate a question without RAG context as fallback."""
    
    if question_type == "objective":
        # Predefined question templates for common GIS topics
        fallback_questions = {
            "GIS Basics": {
                "easy": {
                    "text": "What does GIS stand for?",
                    "options": ["Geographic Information System", "Global Information Service", "Geological Information System", "Geographic Internet Service"],
                    "correct_option": 0,
                    "explanation": "GIS stands for Geographic Information System, which is used to capture, store, analyze and display geographic data."
                },
                "medium": {
                    "text": "Which of the following is NOT a fundamental component of GIS?",
                    "options": ["Hardware", "Software", "Data", "Internet Connection"],
                    "correct_option": 3,
                    "explanation": "While internet can be useful, the fundamental components of GIS are hardware, software, data, procedures, and people."
                },
                "hard": {
                    "text": "In GIS topology, what does the term 'node' refer to?",
                    "options": ["A point where lines intersect or end", "A type of spatial analysis", "A coordinate system", "A data format"],
                    "correct_option": 0,
                    "explanation": "In GIS topology, a node is a point where lines (arcs) intersect or end, forming the basic building blocks of network topology."
                }
            },
            "Coordinate Systems": {
                "easy": {
                    "text": "What is a coordinate system used for in GIS?",
                    "options": ["To locate features on Earth's surface", "To store attribute data", "To create maps", "To analyze spatial patterns"],
                    "correct_option": 0,
                    "explanation": "A coordinate system provides a framework for locating features on Earth's surface using coordinates."
                },
                "medium": {
                    "text": "What is the difference between a geographic coordinate system and a projected coordinate system?",
                    "options": ["Geographic uses degrees, projected uses linear units", "They are the same thing", "Geographic is 2D, projected is 3D", "Geographic is older technology"],
                    "correct_option": 0,
                    "explanation": "Geographic coordinate systems use angular units (degrees), while projected coordinate systems use linear units (meters, feet)."
                },
                "hard": {
                    "text": "Which projection property is preserved in an equal-area (equivalent) projection?",
                    "options": ["Shape", "Area", "Distance", "Direction"],
                    "correct_option": 1,
                    "explanation": "Equal-area projections preserve area relationships but may distort shape, distance, or direction."
                }
            }
        }
        
        # Try to find a matching question
        if topic in fallback_questions and difficulty in fallback_questions[topic]:
            question_data = fallback_questions[topic][difficulty].copy()
            question_data["type"] = "objective"
            question_data["difficulty"] = difficulty
            return question_data
    
    # Generic fallback if no specific question found
    return {
        "text": f"What is an important concept related to {topic}?",
        "type": "objective",
        "options": [
            "Data collection and analysis",
            "Spatial relationships",
            "Geographic visualization", 
            "All of the above"
        ],
        "correct_option": 3,
        "explanation": f"All these concepts are important aspects of {topic} in GIS.",
        "difficulty": difficulty
    }


def is_question_duplicate(new_question: str, previous_questions: List[str], similarity_threshold: float = 0.95) -> bool:
    """Check if a new question is a semantic duplicate of any previous question."""
    if not previous_questions:
        return False
    
    # Encode the new question and previous questions into embeddings
    new_embedding = similarity_model.encode(new_question, convert_to_tensor=True)
    previous_embeddings = similarity_model.encode(previous_questions, convert_to_tensor=True)
    
    # Compute cosine similarity between the new question and all previous questions
    cosine_scores = util.pytorch_cos_sim(new_embedding, previous_embeddings)
    
    # If any score is above the threshold, consider it a duplicate
    if torch.any(cosine_scores > similarity_threshold):
        return True
        
    return False



