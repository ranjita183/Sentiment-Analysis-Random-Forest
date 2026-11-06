import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("amazon_reviews_100_mixed.csv")

# ==============================
# Feature Selection
# ==============================
X = df["Review"]          # Review Text
y = df["Sentiment"]       # Target Variable

# ==============================
# Convert Text to Numerical Features
# ==============================
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ==============================
# Encode Target Labels
# ==============================
df["Sentiment"] = pd.factorize(df["Sentiment"])[0]
y = df["Sentiment"]

# Store label mapping
label_mapping = dict(enumerate(pd.factorize(df["Sentiment"])[1]))

# ==============================
# Split Dataset
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.20,
    random_state=42
)

# ==============================
# Train Random Forest Model
# ==============================
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ==============================
# Model Evaluation
# ==============================
y_pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==============================
# Predict New Review
# ==============================
review = "Met expectations"

review_vector = vectorizer.transform([review])

prediction = model.predict(review_vector)

print("\nReview:", review)

if prediction[0] == 1:
    print("Predicted Sentiment: Positive ")
else:
    print("Predicted Sentiment: Negative ")