if m.chat.id not in ADMINS:

    editable1 = await m.reply_text(f"This feature is reserved for admin only.")

    return

  else:
