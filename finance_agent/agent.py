from google.adk.agents.llm_agent import Agent

def convert_currency(amount: float, rate: float) -> dict:
    """
    Конвертує суму з однієї валюти в іншу за вказаним курсом.

    Args:
        amount: сума для конвертації
        rate: обмінний курс

    Returns:
        dict: структурований результат або повідомлення про помилку
    """
    # Валідація вводу (обробка помилок)
    if amount < 0:
        return {"status": "error", "message": "Сума не може бути від'ємною", "result": None}
    if rate <= 0:
        return {"status": "error", "message": "Курс має бути більшим за нуль", "result": None}
        
    return {"status": "success", "result": round(amount * rate, 2), "error": None}

def calculate_roi(profit: float, investment: float) -> dict:
    """
    Обчислює рентабельність інвестицій (ROI) у відсотках.

    Args:
        profit: чистий прибуток
        investment: початкова сума інвестицій

    Returns:
        dict: відсоток ROI або повідомлення про помилку (перевірка на нуль)
    """
    # Валідація вводу (захист від ділення на нуль, як у прикладі safe_divide)
    if investment == 0:
        return {"status": "error", "message": "Ділення на нуль: сума інвестицій не може дорівнювати нулю", "result": None}
        
    roi = (profit / investment) * 100
    return {"status": "success", "result": round(roi, 2), "error": None}

# Створення агента з чіткими інструкціями
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='finance_assistant',
    description="Фінансовий помічник для конвертації валют та розрахунку інвестицій.",
    instruction="""
Ти професійний фінансовий консультант. 

Твої обов'язки:
1. Допомагати користувачам конвертувати валюти за їхнім курсом.
2. Обчислювати рентабельність інвестицій (ROI).

Правила форматування та поведінки:
- ЗАВЖДИ відповідай українською мовою.
- Використовуй форматування Markdown: виділяй фінальні суми **жирним шрифтом**, використовуй марковані списки для зручності.
- Якщо інструмент повертає помилку (наприклад, через ділення на нуль або від'ємну суму), ввічливо поясни користувачу, що він ввів некоректні дані і попроси їх уточнити.
""",
    tools=[convert_currency, calculate_roi],
)