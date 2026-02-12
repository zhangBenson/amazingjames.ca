import os
import google.generativeai as genai
from datetime import datetime

# 配置 Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    prompt = """
    You are James, a 12-year-old boy living in Toronto, Canada. 
    You were born in Changsha, China and moved to Canada in 2018.
    Interests: Genshin Impact, Roblox, Minecraft, Architecture, Piano, Basketball, Polar Bears.
    Goal: Write a blog post for your website 'amazingjames.ca'.
    Tone: Fun, positive, enthusiastic, slightly humorous, typical for a smart 12-year-old.
    Language: English.
    Requirement: 
    - Choose a specific topic from your interests or daily life in Canada.
    - Do NOT use the surname "Zhang". Just refer to yourself as James.
    - Output ONLY the HTML content that would go inside a <div> with class 'article-content'.
    - Use <h2> for subheaders, <p> for paragraphs, and <ul>/<li> for lists.
    - Include a short introduction and a conclusion.
    """
    
    response = model.generate_content(prompt)
    content = response.text
    
    # 获取标题（从第一行提取或让 AI 生成）
    title_prompt = f"Based on this blog content, provide a short, catchy title (max 60 chars): {content}"
    title_response = model.generate_content(title_prompt)
    title = title_response.text.strip().replace('"', '')
    
    return title, content

def update_files(title, content):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-post.html"
    filepath = f"blog/posts/{filename}"
    
    # 1. 创建文章 HTML
    # AdSense Script for Head
    adsense_head = """
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2574798161475025"
        crossorigin="anonymous"></script>
    """

    # Manual Ad Unit to insert
    ad_unit = """
    <!-- In-content Ad -->
    <div class="content-ad">
        <ins class="adsbygoogle"
            style="display:block"
            data-ad-client="ca-pub-2574798161475025"
            data-ad-slot="auto"
            data-ad-format="fluid"
            data-full-width-responsive="true"></ins>
        <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>
    """

    # Insert Ad Unit after the first paragraph (simple injection)
    if "</p>" in content:
        content_with_ad = content.replace("</p>", "</p>" + ad_unit, 1)
    else:
        content_with_ad = content + ad_unit

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - James's Blog</title>
    {adsense_head}
    <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
    <nav class="main-nav">
        <div class="logo">MEMOIR</div>
        <ul class="nav-links">
            <li><a href="../../index.html">Home</a></li>
            <li><a href="../index.html">Blog</a></li>
        </ul>
    </nav>
    <main class="main-content">
        <article class="blog-post container">
            <header class=\"post-header\">
                <span class=\"post-date\">{datetime.now().strftime("%B %d, %Y")}</span>
                <h1 class=\"post-title\">{title}</h1>
            </header>
            <div class=\"post-content text-block\">
                {content_with_ad}
            </div>
            <div class=\"post-navigation\">
                <a href=\"../index.html\" class=\"nav-link back\">Back to Blog</a>
            </div>
        </article>
    </main>
    <footer>
        <div class=\"container\">
            <p>&copy; 2024 James. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    os.makedirs("blog/posts", exist_ok=True)
    with open(filepath, "w") as f:
        f.write(template)
    
    # 2. 更新 Blog Index (简单实现：在第一个文章前插入)
    with open("blog/index.html", "r") as f:
        index_content = f.read()
    
    new_card = f"""
                    <!-- Article Auto-Generated -->
                    <article class="blog-card fade-in-up delay-2">
                        <div class="blog-content">
                            <div class="blog-meta">{datetime.now().strftime("%b %d, %Y")} • Personal</div>
                            <h2 class="blog-title">{title}</h2>
                            <p class="blog-excerpt">{content[:150].replace('<p>', '').replace('</p>', '')}...</p>
                        </div>
                        <a href="posts/{filename}" class="read-more">Read Article →</a>
                    </article>
"""
    
    marker = "<!-- Article 1 -->"
    if marker in index_content:
        updated_index = index_content.replace(marker, new_card + "\n" + marker)
        with open("blog/index.html", "w") as f:
            f.write(updated_index)

if __name__ == "__main__":
    t, c = generate_post()
    update_files(t, c)
    print(f"Generated: {t}")
