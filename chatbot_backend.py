import json
import random
import re
import datetime

class MentalWellnessChatbot:
    def __init__(self, response_file="responses.json"):
        # Load predefined responses
        with open(response_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)["responses"]
        self.mood_log = []  # Tracks moods over conversation

    # ---------------- TEXT CLEANING ----------------
    def clean_text(self, text):
        """Lowercase and remove punctuation for better matching."""
        return re.sub(r"[^\w\s]", "", text.lower())

    # ---------------- GET CHAT RESPONSE ----------------
    def get_response(self, user_message):
        user_message_clean = self.clean_text(user_message)
        possible_responses = []

        # Partial keyword matching
        for item in self.data:
            for keyword in item["keywords"]:
                if keyword in user_message_clean:
                    possible_responses.append(item)

        if possible_responses:
            chosen = random.choice(possible_responses)
            self.mood_log.append(chosen["mood"])
            return chosen["response"]
        else:
            # Default fallback response
            self.mood_log.append("neutral")
            return "I understand. Can you tell me a bit more about how you're feeling?"

    # ---------------- LOG DAILY MOOD ----------------
    def log_mood(self, mood):
        """Log mood manually from dashboard."""
        today = datetime.date.today().strftime("%Y-%m-%d")
        self.mood_log.append({"date": today, "mood": mood})

    # ---------------- GET MOOD SUMMARY ----------------
    def get_mood_summary(self):
        """Summarize moods over the conversation."""
        if not self.mood_log:
            return "No mood tracked yet."
        
        # Flatten moods in case both string moods and dicts exist
        moods = []
        for entry in self.mood_log:
            if isinstance(entry, dict):
                moods.append(entry["mood"])
            else:
                moods.append(entry)

        mood_count = {}
        for mood in moods:
            mood_count[mood] = mood_count.get(mood, 0) + 1
        
        # Most frequent mood
        top_mood = max(mood_count, key=mood_count.get)
        return f"Current mood trend: {top_mood}."

    # ---------------- GET MOOD TREND FOR DASHBOARD ----------------
    def get_mood_trend(self):
        """Return a simple dictionary of moods over time for visualization."""
        trend = {}
        for entry in self.mood_log:
            if isinstance(entry, dict):
                date = entry["date"]
                mood = entry["mood"]
                trend[date] = mood
        return trend