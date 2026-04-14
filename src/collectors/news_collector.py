
import requests
import os

def fetch_news(api_key):
    """
    지정된 API 키를 사용하여 NewsAPI에서 비즈니스 카테고리의 최신 헤드라인을 가져옵니다.

    Args:
        api_key (str): NewsAPI에서 발급받은 API 키

    Returns:
        dict: API 응답을 JSON 형식으로 반환합니다.
              에러 발생 시 None을 반환합니다.
    """
    if not api_key:
        print("에러: NewsAPI 키가 설정되지 않았습니다.")
        return None

    url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"뉴스 데이터를 가져오는 중 에러가 발생했습니다: {e}")
        return None

if __name__ == '__main__':
    # NEWS_API_KEY 환경 변수에서 API 키를 가져오거나, 아래에 직접 입력하세요.
    # 예: api_key = "YOUR_NEWS_API_KEY"
    api_key = os.getenv("NEWS_API_KEY", "YOUR_NEWS_API_KEY")

    if api_key == "YOUR_NEWS_API_KEY":
        print("주의: NewsAPI 키를 설정해야 합니다.")
        print("환경 변수 NEWS_API_KEY를 설정하거나 코드에 직접 키를 입력하세요.")
    else:
        news_data = fetch_news(api_key)
        if news_data and news_data.get('status') == 'ok':
            articles = news_data.get('articles', [])
            print(f"총 {len(articles)}개의 뉴스를 가져왔습니다.")
            for i, article in enumerate(articles[:5], 1): # 상위 5개 뉴스만 출력
                print(f"  [{i}] {article['title']}")
                print(f"      출처: {article['source']['name']}")
