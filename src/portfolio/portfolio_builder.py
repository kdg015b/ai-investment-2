
def build_portfolio(scores):
    """
    점수 리스트를 기반으로 상위 5개 자산을 선택하고 투자 비중을 할당합니다.

    Args:
        scores (list of dict): 각 자산의 이름과 점수를 담은 딕셔너리 리스트
                               (예: [{'name': 'BTC', 'score': 80}, ...])

    Returns:
        list of dict: 투자 비중('weight')이 추가된 상위 5개 자산 리스트
                      입력 리스트가 비어있으면 빈 리스트를 반환합니다.
    """
    if not scores:
        return []

    # 점수가 높은 순서대로 자산을 정렬합니다.
    sorted_assets = sorted(scores, key=lambda x: x.get('score', 0), reverse=True)
    
    # 상위 5개 자산을 선택합니다.
    top5 = sorted_assets[:5]

    # 상위 5개 자산의 총 점수를 계산합니다.
    total_score = sum([x.get('score', 0) for x in top5])

    if total_score == 0:
        # 모든 점수가 0일 경우, 균등하게 비중을 할당합니다.
        for asset in top5:
            asset['weight'] = round(100 / len(top5), 2)
        return top5

    # 각 자산의 점수 비율에 따라 투자 비중을 계산하고 추가합니다.
    for asset in top5:
        asset['weight'] = round(asset.get('score', 0) / total_score * 100, 2)

    return top5

if __name__ == '__main__':
    # 테스트 예제: 여러 자산에 대한 가상 점수 리스트
    sample_scores = [
        {'name': 'Bitcoin (BTC)', 'score': 80.5},
        {'name': 'Ethereum (ETH)', 'score': 88.2},
        {'name': 'Solana (SOL)', 'score': 91.0},
        {'name': 'Binance Coin (BNB)', 'score': 75.3},
        {'name': 'Cardano (ADA)', 'score': 82.1},
        {'name': 'XRP', 'score': 65.7},
        {'name': 'Dogecoin (DOGE)', 'score': 50.4}
    ]

    final_portfolio = build_portfolio(sample_scores)

    print("--- 최종 투자 포트폴리오 (Top 5) ---")
    for asset in final_portfolio:
        print(f"  - 자산: {asset['name']}")
        print(f"    - 투자 점수: {asset['score']}")
        print(f"    - 추천 비중: {asset['weight']}%\n")

    total_weight = sum(a['weight'] for a in final_portfolio)
    print(f"총 비중 합계: {total_weight:.2f}% (소수점 오차로 100이 아닐 수 있음)")
