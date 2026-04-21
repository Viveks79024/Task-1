from services.groq_client import generate_ai_response

def run_agent(question):

    prompt = f"""
    You are a medical assistant helping pharma representatives.
    Answer the doctor's query clearly.

    Question: {question}
    """

    response = generate_ai_response(prompt)

    return response