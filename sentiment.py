from transformers import pipeline

classifier = pipeline(
    "Sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english5"
)

result = classifier("I Love to drink tea during Winter.")
print(result)