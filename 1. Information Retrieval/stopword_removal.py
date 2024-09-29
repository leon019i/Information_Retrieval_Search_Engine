import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download stopwords
# nltk.download('stopwords')

# Define text
text = "This is an example sentence demonstrating the removal of stopwords."

# Load stopwords
stop_words = set(stopwords.words('english'))

# Tokenize the text
words = word_tokenize(text)


filtered_words = [word for word in words if word.lower() not in stop_words]

filtered_text = ' '.join(filtered_words)

print(f"Original text: {text}")

print(f"After removal of stopwords: {filtered_text}")
