from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I hate this product. It is very bad.")
print(result)