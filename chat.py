import os
import google.generativeai as genai

# Set up the API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def roast_user(name, user_comeback, roast_level):
    model = genai.GenerativeModel("gemini-2.0-flash")

    try:
        # Step 1: Rate the user's comeback
        rating_prompt = f"Rate this roast from {name} on a scale of 1 to 10 in a single sentence: '{user_comeback}'"
        rating_response = model.generate_content(rating_prompt).text.strip()

        # Step 2: Generate a roast based on the selected level
        roast_prompt = f"Roast {name} in ONE savage sentence based on their comeback: '{user_comeback}'. Make it {roast_level}-level."
        roast_response = model.generate_content(roast_prompt).text.strip()

        return {
            "rating": rating_response,
            "roast": roast_response
        }
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("🔥 Welcome to the Ultimate Roast Battle! 🔥")
    name = input("What's your name? ")

    # Select Roast Level
    print("\nChoose Your Roast Level: \n1. Kid 🍼 (Playful) \n2. Adult 🍻 (Savage) \n3. Dark ☠️ (Brutal)")
    choice = input("Enter 1, 2, or 3: ")

    roast_levels = {"1": "kid-friendly", "2": "adult", "3": "dark humor"}
    roast_level = roast_levels.get(choice, "adult")  # Default to adult if invalid input

    print(f"\nAlright {name}, you're getting {roast_level} roasts! Let's go 🔥")

    while True:
        user_comeback = input(f"\nAlright {name}, hit me with your best shot: ")

        if user_comeback.lower() in ["exit", "quit", "stop"]:
            print(f"Damn, {name}, you tapping out already? Weak. 😜")
            break
        
        print(roast_user(name, user_comeback, roast_level))
