from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """
    Повертає поточний час у вказаному місті.
    
    Args:
        city: назва міста
    
    Returns:
        dict: інформація про час у вказаному місті
    """
    # Це mock-реалізація для демонстрації
    import datetime
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return {
        "status": "success",
        "city": city,
        "time": current_time
    }

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='time_agent',
    temperature=0.1,
    description="Повідомляє поточний час у вказаному місті.",
    instruction="Ти корисний асистент, який повідомляє поточний час у містах. Використовуй функцію 'get_current_time' для цього. Відповідай українською мовою та використовуй подачу дати/часу у форматі HH:MM:SS.",
    tools=[get_current_time],
)
