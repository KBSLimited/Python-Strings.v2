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
def summarize_review(review, max_length=30):
    # Check if the review length is less than or equal to the max length
    if len(review) <= max_length:
        return review
    
    # Truncate to the max length
    truncated_review = review[:max_length]
    
    # Check if the last character is a space or part of a word
    if truncated_review[-1] != " " and " " in truncated_review:
        # Find the last space within the truncated review
        last_space = truncated_review.rfind(" ")
        truncated_review = truncated_review[:last_space]
    
    # Append "…" to indicate the summary is truncated
    return truncated_review + "…"

# Example usage:
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Create summaries for each review
for review in reviews:
    summary = summarize_review(review)
    print(f"Original review: {review}")
    print(f"Summary: {summary}")
    print()