# utils/rewriter.py

def rewrite_caption(base_caption: str, platform: str, tone: str) -> str:
    """
    Rewrites a base caption for a specific platform (Instagram, Twitter, WhatsApp)
    and applies a tone/style (Funny, Romantic, Deep, Savage).

    Args:
        base_caption (str): The original caption from the image model.
        platform (str): The platform to customize for.
        tone (str): The desired caption style or vibe.

    Returns:
        str: Final caption customized with tone and platform.
    """

    # Clean and normalize base caption
    base_caption = base_caption.strip().capitalize()  # "a cool cat" -> "A cool cat"

    # Add style (tone) prefix
    if tone == "Funny":
        tone_prefix = "😂 Here's a funny take: "
    elif tone == "Romantic":
        tone_prefix = "❤️ Feeling the love: "
    elif tone == "Deep":
        tone_prefix = "💭 Deep thoughts: "
    elif tone == "Savage":
        tone_prefix = "💀 Ruthless vibes: "
    else:
        tone_prefix = ""

    # Add platform-specific suffix
    if platform == "Instagram":
        platform_suffix = " "
    elif platform == "Twitter":
        platform_suffix = " "
    elif platform == "WhatsApp":
        platform_suffix = " "
    else:
        platform_suffix = ""

    # Combine everything into the final caption
    return f"{base_caption}"
