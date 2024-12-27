import streamlit as st

# ページ設定
st.set_page_config(
    page_title="おすすめWebサイト集",
    layout="wide"
)

# サイトデータ
WORKS = [
    {
        "title": "GitHub",
        "description": "世界最大のソフトウェア開発プラットフォーム。オープンソースプロジェクトのホスティングやバージョン管理、コラボレーション機能を提供しています。開発者必須のサービスです。",
        "image_url": "https://github.githubassets.com/images/modules/site/social-cards/campaign-social.png",
        "link_url": "https://github.com"
    },
    {
        "title": "Stack Overflow",
        "description": "プログラミングに関する質問と回答のプラットフォーム。世界中の開発者が質問し、回答を共有しています。技術的な問題解決には欠かせないリソースです。",
        "image_url": "https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded",
        "link_url": "https://stackoverflow.com"
    },
    {
        "title": "MDN Web Docs",
        "description": "Mozillaが提供するWeb技術のための包括的なドキュメント。HTML、CSS、JavaScriptなどのWeb開発に関する詳細な情報とチュートリアルを提供しています。",
        "image_url": "https://developer.mozilla.org/mdn-social-share.cd6c4a5a.png",
        "link_url": "https://developer.mozilla.org"
    },
    {
        "title": "Qiita",
        "description": "日本最大級のエンジニアコミュニティ。技術記事の投稿・共有プラットフォームとして、日本語での技術情報共有に重要な役割を果たしています。",
        "image_url": "https://cdn.qiita.com/assets/qiita-ogp-3b6fcfdd74755a85107071ffc3d9d402.png",
        "link_url": "https://qiita.com"
    }
]

# CSSでスタイリング
st.markdown("""
    <style>
    .work-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
    .work-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .work-description {
        color: #444;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    .image-container img {
        border-radius: 8px;
        transition: transform 0.3s ease;
    }
    .image-container img:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

def main_page():
    st.title("おすすめWebサイト集")
    st.markdown("### 開発者向けの便利なWebサイトを紹介します")
    
    # サイト一覧表示
    for work in WORKS:
        with st.container():
            st.markdown('<div class="work-container">', unsafe_allow_html=True)
            cols = st.columns([1, 2])
            
            with cols[0]:
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(work['image_url'], use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with cols[1]:
                st.markdown(f"<div class='work-title'>{work['title']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='work-description'>{work['description']}</div>", unsafe_allow_html=True)
                st.link_button("サイトを開く", work['link_url'])
            
            st.markdown('</div>', unsafe_allow_html=True)

def preview_page():
    st.title("サイトプレビュー")
    
    # 選択されたサイトのプレビュー
    selected_work = st.selectbox(
        "サイトを選択",
        options=[work["title"] for work in WORKS],
        index=0
    )
    
    work = next(work for work in WORKS if work["title"] == selected_work)
    
    st.subheader("プレビュー表示")
    with st.container():
        st.image(work['image_url'], use_container_width=True)
        st.markdown(f"### {work['title']}")
        st.write(work['description'])
        st.link_button("サイトを開く", work['link_url'])

# サイドバーでページ選択
page = st.sidebar.radio("ページ選択", ["メインページ", "プレビュー"])

if page == "メインページ":
    main_page()
else:
    preview_page()

# フッター
st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 Developer's Resource Guide")