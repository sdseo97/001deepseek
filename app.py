import streamlit as st
from openai import OpenAI

# Streamlit 앱 제목 설정
st.title("DeepSeek 블로그 글 생성기")

# 사이드바에 API 키 입력 필드 추가
api_key = st.sidebar.text_input("DeepSeek API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    
    # 키워드 입력 필드
    keyword = st.text_input("블로그 글을 생성할 키워드를 입력하세요")
    
    if keyword:
        # SEO 최적화를 위한 프롬프트 구성
        prompt = f"""
        다음 키워드를 기반으로 구글 SEO에 최적화된 블로그 글을 작성해주세요.
        키워드: {keyword}
        
        요구사항:
        1. 제목은 키워드를 포함해야 함
        2. 1500자 이상의 상세한 내용
        3. H2, H3 태그를 사용한 구조화된 내용
        4. 키워드 밀도 2-3% 유지
        5. 자연스러운 문장 구성
        6. 관련 통계 및 데이터 포함
        7. 결론 부분에 요약 및 CTA 포함
        """
        
        # 채팅 메시지 구성
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        # 글 생성 버튼
        if st.button("블로그 글 생성"):
            with st.spinner("블로그 글을 생성 중입니다..."):
                try:
                    # DeepSeek API 호출
                    response = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=messages,
                        temperature=0.7,
                        max_tokens=2000
                    )
                    
                    # 생성된 글 표시
                    generated_text = response.choices[0].message.content
                    st.subheader("생성된 블로그 글")
                    st.markdown(generated_text)
                    
                except Exception as e:
                    st.error(f"글 생성 중 오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요. 사이드바에서 입력할 수 있습니다.")
