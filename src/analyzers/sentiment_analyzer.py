
def analyze_sentiment(text):
    """
    간단한 키워드 매칭을 통해 텍스트의 감정을 분석합니다.

    Args:
        text (str): 분석할 텍스트 (예: 뉴스 기사 제목 또는 요약)

    Returns:
        dict: "sentiment" (positive, negative, neutral)와 "score"를 포함하는 딕셔너리
    """
    if not isinstance(text, str):
        return {"sentiment": "neutral", "score": 0}

    text_lower = text.lower()
    
    positive_keywords = ["up", "rise", "increase", "profit", "bullish", "growth", "success", "launch", "optimistic"]
    negative_keywords = ["down", "fall", "decrease", "loss", "bearish", "drop", "failure", "scam", "pessimistic", "bubble"]

    score = 0
    for keyword in positive_keywords:
        if keyword in text_lower:
            score += 1
    
    for keyword in negative_keywords:
        if keyword in text_lower:
            score -= 1

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"sentiment": sentiment, "score": score}


if __name__ == '__main__':
    # 테스트 예제
    sample_text_1 = "Stock prices rise after successful product launch."
    sample_text_2 = "Market sees a significant drop due to economic concerns."
    sample_text_3 = "The company reported stable earnings for the quarter."

    result_1 = analyze_sentiment(sample_text_1)
    result_2 = analyze_sentiment(sample_text_2)
    result_3 = analyze_sentiment(sample_text_3)

    print(f"Text: '{sample_text_1}'\nResult: {result_1}\n")
    print(f"Text: '{sample_text_2}'\nResult: {result_2}\n")
    print(f"Text: '{sample_text_3}'\nResult: {result_3}\n")
