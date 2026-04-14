
import os
from collectors.news_collector import fetch_news
from analyzers.sentiment_analyzer import analyze_sentiment
from evaluators.scoring_engine import calculate_score
from portfolio.portfolio_builder import build_portfolio

def main():
    """
    투자 자동화 에이전트 시스템의 메인 실행 함수
    """
    print("--- 투자 자동화 에이전트 시스템 v1.0 실행 ---\n")

    # --- 1단계: 데이터 수집 ---
    print("[1/4] 뉴스 데이터 수집 중...")
    # 실제 실행 시에는 YOUR_NEWS_API_KEY를 실제 키로 대체해야 합니다.
    api_key = os.getenv("NEWS_API_KEY", "d2b1435cd12c47b59e5576722c15112e")
    news_data = fetch_news(api_key)
    
    if not news_data or news_data.get('status') != 'ok':
        print("  >> 뉴스 수집 실패. 프로세스를 종료합니다.")
        return

    articles = news_data.get('articles', [])
    print(f"  >> 총 {len(articles)}개의 뉴스 기사 수집 완료.")

    # --- 2단계: 인사이트 분석 (감정 분석) ---
    print("\n[2/4] 뉴스 인사이트 분석 중...")
    analyzed_articles = []
    for article in articles:
        sentiment_result = analyze_sentiment(article['title'])
        article['sentiment'] = sentiment_result
        analyzed_articles.append(article)
    print("  >> 모든 기사에 대한 감정 분석 완료.")

    # --- 3단계 & 4단계: 투자 평가 (가상 데이터 사용) ---
    # 이 단계에서는 특정 종목들에 대해 가상의 점수를 부여합니다.
    # 추후 이 부분은 수집/분석된 데이터를 기반으로 점수를 계산하는 로직으로 대체되어야 합니다.
    print("\n[3/4] 투자 가치 평가 중... (현재는 가상 데이터 사용)")
    # 감정 분석 결과를 바탕으로 모멘텀 점수를 간단히 계산해봅니다.
    # 여기서는 'bitcoin' 또는 'ethereum'이 언급된 뉴스의 감정 점수 합으로 단순화합니다.
    btc_momentum = sum(a['sentiment']['score'] for a in analyzed_articles if 'bitcoin' in a['title'].lower())
    eth_momentum = sum(a['sentiment']['score'] for a in analyzed_articles if 'ethereum' in a['title'].lower())

    # 가상의 종목별 점수 리스트 (펀더멘탈, 온체인, 기술 점수는 임의로 부여)
    scores_data = [
        {'name': 'Bitcoin', 'momentum': btc_momentum * 10, 'fundamental': 75, 'onchain': 90, 'technical': 65},
        {'name': 'Ethereum', 'momentum': eth_momentum * 10, 'fundamental': 85, 'onchain': 80, 'technical': 70},
        {'name': 'Solana', 'momentum': 60, 'fundamental': 70, 'onchain': 85, 'technical': 75}, # 가상 점수
        {'name': 'BNB', 'momentum': 50, 'fundamental': 78, 'onchain': 70, 'technical': 60}, # 가상 점수
        {'name': 'Cardano', 'momentum': 45, 'fundamental': 82, 'onchain': 65, 'technical': 55}, # 가상 점수
        {'name': 'XRP', 'momentum': 30, 'fundamental': 60, 'onchain': 75, 'technical': 50}, # 가상 점수
    ]

    # 각 종목의 종합 점수 계산
    for asset in scores_data:
        asset['score'] = calculate_score(
            asset['momentum'], asset['fundamental'], asset['onchain'], asset['technical']
        )
    print("  >> 각 자산의 종합 투자 점수 계산 완료.")

    # --- 5단계: 포트폴리오 생성 ---
    print("\n[4/4] 최종 포트폴리오 생성 중...")
    final_portfolio = build_portfolio(scores_data)
    print("  >> 포트폴리오 생성 완료.")

    # --- 최종 결과 출력 ---
    print("\n--- 최종 투자 추천 포트폴리오 (Top 5) ---")
    if not final_portfolio:
        print("  >> 추천 포트폴리오를 생성할 수 없습니다.")
    else:
        for asset in final_portfolio:
            print(f"  - 자산: {asset['name']}")
            print(f"    - 종합 점수: {asset['score']:.2f}")
            print(f"    - 추천 비중: {asset['weight']}%\n")

    total_weight = sum(a.get('weight', 0) for a in final_portfolio)
    print(f"포트폴리오 총 비중: {total_weight:.2f}%\n")
    print("--- 시스템 실행 종료 ---")

if __name__ == '__main__':
    main()
