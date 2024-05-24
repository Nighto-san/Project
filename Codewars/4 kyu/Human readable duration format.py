def format_duration(seconds):
    if seconds == 0: return 'now'
    years = seconds // (60 * 60 * 24 * 365)
    seconds %= (60 * 60 * 24 * 365)
    days = seconds // (60 * 60 * 24)
    seconds %= (60 * 60 * 24)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    duration_parts = []
    if years:
        duration_parts.append(f"{years} {'year' if years == 1 else 'years'}")
    if days:
        duration_parts.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours:
        duration_parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        duration_parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds:
        duration_parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    if not duration_parts:
        return "0 seconds"
    elif len(duration_parts) == 1:
        return duration_parts[0]
    else:
        duration_text = ', '.join(duration_parts[:-1]) + " and " + duration_parts[-1]
        return duration_text




print(format_duration(62),"          ", "1 minute and 2 seconds")
print(format_duration(242062374),"          ", "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")