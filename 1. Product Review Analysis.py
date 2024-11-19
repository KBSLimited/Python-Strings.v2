#Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# List of keywords to look for
keywords = ["good", "excellent", "bad", "poor", "average"]

# Function to capitalize keywords in a review
def highlight_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())  # Replace keyword with its uppercase version
    return review

# Loop through reviews and apply the function
for review in reviews:
    highlighted_review = highlight_keywords(review, keywords)
    print(highlighted_review)

#Task 2: Sentiment Tally


#Task 3: Review Summary
