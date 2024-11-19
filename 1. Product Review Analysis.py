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
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to tally positive and negative words
def tally_sentiment(review, positive_words, negative_words):
    # Convert the review to lowercase for case-insensitive comparison
    review_lower = review.lower()
    
    # Initialize counters for positive and negative words
    positive_count = 0
    negative_count = 0
    
    # Count positive words
    for word in positive_words:
        positive_count += review_lower.count(word)
    
    # Count negative words
    for word in negative_words:
        negative_count += review_lower.count(word)
    
    return positive_count, negative_count

# Loop through reviews and tally sentiment
for review in reviews:
    positive_count, negative_count = tally_sentiment(review, positive_words, negative_words)
    print(f"Review: {review}")
    print(f"Positive words: {positive_count}, Negative words: {negative_count}")
    print()  # For spacing between reviews

#Task 3: Review Summary
