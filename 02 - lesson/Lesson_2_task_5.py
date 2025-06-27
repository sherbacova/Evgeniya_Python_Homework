def month_to_season(month):
  if 1 <= month <= 2 or 12 == month:
    return "зима"
  elif 6 <= month <= 8:
    return "лето"
  elif 9 <= month <= 11:
    return "осень"
  elif 3 <= month <= 5:
    return "весна"
  else:
    return "Неверный номер месяца"