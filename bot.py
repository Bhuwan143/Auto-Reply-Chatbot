import pyautogui
import time
import pyperclip
from openai import OpenAI

# ----------------- OpenRouter Client -----------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",  # Important for OpenRouter
    api_key="Your API Key",
)


def is_last_message_from_sender(chat_log, sender_name="vedika"):
    """
    Returns True if the last message in chat_log is from the sender_name.
    """
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name.lower() in messages.lower():
        return True
    return False

# ----------------- Main Loop -----------------
# Step 1: Click Chrome icon to focus WhatsApp Web
pyautogui.click(727, 1037)
time.sleep(1)

while True:
    time.sleep(5)
    
    # Step 2: Select chat text
    pyautogui.moveTo(952, 314)
    pyautogui.dragTo(1876, 892, duration=2.0, button='left')
    
    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    # Optional: Click somewhere to remove selection
    pyautogui.click(1857, 457)
    
    # Step 4: Retrieve clipboard text
    chat_history = pyperclip.paste()
    
    # Debug print
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    
    if is_last_message_from_sender(chat_history):
        # ----------------- Generate Response -----------------
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a person named Bhuvan who speaks English, "
                },
                {
                    "role": "system",
                    "content": "Do not start with timestamp or sender name like [21:02, 12/6/2024] vedika: "
                },
                {"role": "user", "content": chat_history}
            ]
        )
        
        # Step 5: Copy response to clipboard
        response = completion.choices[0].message.content
        pyperclip.copy(response)
        
        # Step 6: Click input box
        pyautogui.click(1219, 953)
        time.sleep(0.5)
        
        # Step 7: Paste response and send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
