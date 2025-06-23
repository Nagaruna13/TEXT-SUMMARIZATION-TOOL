 Load pre-trained summarizer model
summarizer = pipeline("summarization")

# Input text (you can replace this with any long text)
text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. These machines can perform tasks such as recognizing speech, making decisions, and translating languages.
AI is becoming increasingly important in many industries including healthcare, finance, and transportation. The rise of AI has led to innovations such as self-driving cars, virtual assistants, and personalized recommendations.
"""

# Generate summary
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

# Print summary
print("🔍 Summary:\n", summary[0]['summary_text'])
