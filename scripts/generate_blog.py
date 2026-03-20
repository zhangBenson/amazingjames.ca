import os
from datetime import datetime

def generate_post():
    title = "My Latest Genshin Impact Adventure in Toronto!"
    content = """
    <h2>A Weekend Well Spent</h2>
    <p>Hey everyone, it's James! This weekend was amazing. I spent Saturday morning playing the piano and finally nailed that tricky piece I've been practicing for weeks.</p>
    <h2>Exploring Teyvat</h2>
    <p>After that, it was straight into Genshin Impact! I explored some new areas and completed a few challenging quests. It's so cool how the architecture in the game is so detailed.</p>
    <ul>
        <li>Beat a difficult boss</li>
        <li>Leveled up my favorite characters</li>
        <li>Built a new house in the Serenitea Pot</li>
    </ul>
    <p>Later, I went outside to play some basketball with my friends. The weather in Toronto is finally getting a bit warmer, even though we still have some snow!</p>
    <h2>Looking Forward</h2>
    <p>Can't wait to see what next week brings. Maybe I'll work on a new Minecraft build or learn a bit more about polar bears. See you next time!</p>
    """
    return title, content

def update_files(title, content):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-post.html"
    filepath = f"/Users/benson/websites/amazingjames.ca/blog/posts/{filename}"
    
    # AdSense Script for Head
    adsense_head = """
    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2574798161475025"
        crossorigin="anonymous"></script>
    """

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
                {content}
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
    
    os.makedirs("/Users/benson/websites/amazingjames.ca/blog/posts", exist_ok=True)
    with open(filepath, "w") as f:
        f.write(template)
    
    with open("/Users/benson/websites/amazingjames.ca/blog/index.html", "r") as f:
        index_content = f.read()
    
    new_card = f"""
                    <!-- Article Auto-Generated -->
                    <article class="blog-card fade-in-up delay-2">
                        <div class="blog-content">
                            <div class="blog-meta">{datetime.now().strftime("%b %d, %Y")} • Personal</div>
                            <h2 class="blog-title">{title}</h2>
                            <p class="blog-excerpt">{content[:150].replace('<p>', '').replace('</p>', '').replace('<h2>', '')}...</p>
                        </div>
                        <a href="posts/{filename}" class="read-more">Read Article →</a>
                    </article>
"""
    
    marker = "<!-- Article 1 -->"
    if marker in index_content:
        updated_index = index_content.replace(marker, new_card + "\n" + marker)
        with open("../blog/index.html", "w") as f:
            f.write(updated_index)

if __name__ == "__main__":
    t, c = generate_post()
    update_files(t, c)
    print(f"Generated: {t}")
