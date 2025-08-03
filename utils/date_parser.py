from datetime import datetime, timedelta


def normalize_time(time_str: str) -> str:
    try:
        return datetime.strptime(time_str.strip().lower(), "%I:%M %p").strftime("%H:%M")
    except ValueError:
        try:
            return datetime.strptime(time_str.strip().lower(), "%I %p").strftime(
                "%H:%M"
            )
        except ValueError:
            return time_str  # fallback to original


def parse_natural_date(text):
    text = text.lower()
    today = datetime.today()

    if "today" in text:
        return today.strftime("%Y-%m-%d")
    elif "tomorrow" in text:
        return (today + timedelta(days=1)).strftime("%Y-%m-%d")
    elif "next week" in text:
        return (today + timedelta(days=7)).strftime("%Y-%m-%d")
    elif "next monday" in text:
        return _next_weekday(today, 0)
    elif "next tuesday" in text:
        return _next_weekday(today, 1)
    elif "next wednesday" in text:
        return _next_weekday(today, 2)
    elif "next thursday" in text:
        return _next_weekday(today, 3)
    elif "next friday" in text:
        return _next_weekday(today, 4)
    elif "next saturday" in text:
        return _next_weekday(today, 5)
    elif "next sunday" in text:
        return _next_weekday(today, 6)
    else:
        return None


def _next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return (d + timedelta(days=days_ahead)).strftime("%Y-%m-%d")
