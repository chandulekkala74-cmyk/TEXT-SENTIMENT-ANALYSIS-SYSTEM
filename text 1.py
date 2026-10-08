import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER model automatically
nltk.download("vader_lexicon", quiet=True)

# Create analyzer
analyzer = SentimentIntensityAnalyzer()

print("=" * 60)
print("             TEXT SENTIMENT ANALYSIS SYSTEM")
print("=" * 60)

while True:

    text = input("\nEnter your text (type 'exit' to stop): ")

    if text.lower() == "exit":
        print("\nThank you for using the system!")
        break

    if not text.strip():
        print("Please enter some text.")
        continue

    # Analyze sentiment
    result = analyzer.polarity_scores(text)
    score = result["compound"]

    # Determine sentiment
    if score >= 0.05:
        sentiment = "POSITIVE 😊"
    elif score <= -0.05:
        sentiment = "NEGATIVE 😞"
    else:
        sentiment = "NEUTRAL 😐"

    # Display result
    print("\n" + "-" * 45)
    print("TEXT       :", text)
    print("SENTIMENT  :", sentiment)
    print("POSITIVE   :", round(result["pos"], 3))
    print("NEGATIVE   :", round(result["neg"], 3))
    print("NEUTRAL    :", round(result["neu"], 3))
    print("SCORE      :", round(score, 3))
    print("-" * 45)