from transformers import pipeline

summarizer = pipeline("summarization")

result = summarizer(
    "Artificial Intelligence is a technology that enables machines to perform tasks that normally require human intelligence.",
    max_length=20,
    min_length=5,
    do_sample=False
)

print(result)