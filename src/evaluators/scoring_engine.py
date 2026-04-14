
def calculate_score(momentum, fundamental, onchain, technical):
    """
    설계서에 정의된 가중치에 따라 종합 투자 점수를 계산합니다.
    Total Score = 0.35 * Momentum + 0.30 * Fundamental + 0.20 * Onchain + 0.15 * Technical

    Args:
        momentum (float): 모멘텀 점수 (0-100)
        fundamental (float): 펀더멘탈 점수 (0-100)
        onchain (float): 온체인 점수 (0-100)
        technical (float): 기술적 분석 점수 (0-100)

    Returns:
        float: 계산된 종합 점수
    """
    weights = {
        'momentum': 0.35,
        'fundamental': 0.30,
        'onchain': 0.20,
        'technical': 0.15
    }

    total_score = (
        momentum * weights['momentum'] + 
        fundamental * weights['fundamental'] + 
        onchain * weights['onchain'] + 
        technical * weights['technical']
    )

    return total_score

if __name__ == '__main__':
    # 테스트 예제: 특정 자산(예: BTC)에 대한 가상 점수
    btc_scores = {
        "momentum": 85,      # 최근 뉴스 및 소셜 미디어에서 긍정적 언급 증가
        "fundamental": 75,   # 네트워크 성장 및 채택률 꾸준
        "onchain": 90,       # 활성 주소 및 거래량 급증, 고래들의 축적 정황
        "technical": 65      # 주요 이동평균선 상향 돌파
    }

    btc_total_score = calculate_score(
        btc_scores["momentum"],
        btc_scores["fundamental"],
        btc_scores["onchain"],
        btc_scores["technical"]
    )

    print(f"자산: Bitcoin (BTC)")
    print(f" - 모멘텀 점수: {btc_scores['momentum']}")
    print(f" - 펀더멘탈 점수: {btc_scores['fundamental']}")
    print(f" - 온체인 점수: {btc_scores['onchain']}")
    print(f" - 기술적 분석 점수: {btc_scores['technical']}")
    print(f"\n >> 종합 투자 점수: {btc_total_score:.2f}")
