def is_crisis(text: str) -> bool:
    crisis_signals = [
        "kill myself", "end it all", "suicide",
        "hurt myself", "can't go on", "no reason to live"
    ]
    return any(phrase in text.lower() for phrase in crisis_signals)
