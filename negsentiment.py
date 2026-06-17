from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love this product. It is amazing!")
print(result)