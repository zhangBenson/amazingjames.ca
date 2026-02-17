import os

# Project configuration
ROOT_DIR = "/Users/benson/websites/amazingjames.ca"
TEMPLATE_PATH = os.path.join(ROOT_DIR, "templates/layout.html")

def build_page(title, description, content, output_path, depth=0):
    with open(TEMPLATE_PATH, 'r') as f:
        template = f.read()
    
    root_path = "../" * depth
    
    # Simple template replacement
    html = template.replace("{{title}}", title)
    html = html.replace("{{description}}", description)
    html = html.replace("{{content}}", content)
    html = html.replace("{{root_path}}", root_path)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"✅ Built {output_path}")

# --- Blog Posts Reconstruction ---
# Content extracted from session history to fix broken files

GENSHIN_PIANO_CONTENT = """
        <article class="blog-post container">
            <header class="post-header">
                <span class="post-date">February 11, 2026</span>
                <h1 class="post-title">Why Genshin Impact Music is Amazing on Piano</h1>
                <div class="post-tags">
                    <span class="tag">Music</span>
                    <span class="tag">Piano</span>
                    <span class="tag">Genshin Impact</span>
                </div>
            </header>

            <div class="post-content text-block">
                <p>Most people play Genshin Impact for the characters (like Zhongli!) or the exploration. But honestly? I stay for the music. And since I play piano, I've started trying to learn the soundtrack myself.</p>

                <h2>It's Harder Than It Sounds!</h2>
                <p>I thought, "It's video game music, how hard can it be?" Wrong. The composers at HOYO-MiX are geniuses. The songs are full of crazy fast arpeggios and complex chords.</p>
                <p>Right now, I'm practicing the Inazuma battle theme. It's super fast and intense. My fingers get tangled sometimes, but when you finally nail that one fast run, it feels epic—like you just defeated a boss in real life.</p>

                <h2>Why I Love It</h2>
                <p>Classical piano (like Mozart or Beethoven) is cool and all, but playing songs you recognize from a game you love hits different. It connects two of my favorite things: gaming and music.</p>
                <ul>
                    <li><strong>Emotion:</strong> The music tells a story without words. The Dragonspine music makes you feel cold and lonely, while Liyue's music feels busy and grand.</li>
                    <li><strong>Challenge:</strong> It pushes me to practice more than my regular lessons do. I actually <em>want</em> to sit at the piano.</li>
                </ul>

                <h2>My Goal</h2>
                <p>I want to be able to play the entire Inazuma soundtrack eventually. Maybe one day I'll record it and put it here! For now, I'll keep practicing scales so my fingers can keep up.</p>
                <p>If you play an instrument, try learning a song from your favorite game. Trust me, it makes practice way more fun.</p>

                <div class="post-footer">
                    <p>Keep practicing!</p>
                    <p>- James</p>
                </div>
            </div>
            
            <div class="post-navigation">
                <a href="roblox-obby-design.html" class="nav-link prev">← Previous: The Art of the Roblox Obby</a>
                <a href="../index.html" class="nav-link back">Back to Blog</a>
            </div>
        </article>
"""

ROBLOX_OBBY_CONTENT = """
        <article class="blog-post container">
            <header class="post-header">
                <span class="post-date">February 9, 2026</span>
                <h1 class="post-title">The Art of the Roblox Obby: Why Design Matters</h1>
                <div class="post-tags">
                    <span class="tag">Roblox</span>
                    <span class="tag">Gaming</span>
                    <span class="tag">Game Design</span>
                </div>
            </header>

            <div class="post-content text-block">
                <p>If you've spent any time on Roblox, you've definitely played an <strong>Obby</strong> (Obstacle Course). Some are simple, some are "mega" long, and some are just plain impossible. But after playing hundreds of them, I've realized that the best ones aren't just about jumping—they're about <em>design</em>.</p>

                <h2>Fairness vs. Frustration</h2>
                <p>There's a big difference between a challenge and a chore. A well-designed Obby gives you a fair chance. You can see where you need to go, the jumps feel natural, and the checkpoints are spaced out just right.</p>
                <p>When an Obby is just "kill parts" (lasers) everywhere with no logic, it's not fun. It's just frustrating. Good design means thinking about the player's experience. Does this jump feel rewarding? Is the path clear? This is basically what real game designers do!</p>

                <h2>The "Vibe" of the Course</h2>
                <p>The best Obbies have a theme. Instead of just floating neon blocks, maybe you're escaping a giant bakery or climbing a futuristic tower. Since I love architecture, I always appreciate when a creator uses colors and shapes to tell a story.</p>
                <p>In Roblox Studio, I've been experimenting with building my own courses. I try to focus on "Flow"—the way a player moves through the level. If you can keep a steady rhythm without stopping every two seconds, that's a masterpiece.</p>

                <h2>My Top Tips for Obby Creators</h2>
                <ul>
                    <li><strong>Test your jumps:</strong> If you can't make it 10 times in a row, it's too hard.</li>
                    <li><strong>Use lighting:</strong> A little bit of glow and atmosphere goes a long way.</li>
                    <li><strong>Respect the player:</strong> Checkpoints are your friend. Don't make people redo 10 minutes of work because of one lag spike!</li>
                </ul>

                <h2>What's Next?</h2>
                <p>I'm working on a "Classic Architecture" themed Obby right now. It's going to have columns, arches, and maybe some Redstone-like logic (using Luau scripts) to make things move. Stay tuned!</p>

                <div class="post-footer">
                    <p>What's the hardest Obby you've ever beaten? Let me know!</p>
                    <p>- James</p>
                </div>
            </div>
            
            <div class="post-navigation">
                <a href="minecraft-architecture.html" class="nav-link prev">← Previous: Building Dreams: Why Minecraft is My Architecture School</a>
                <a href="../index.html" class="nav-link back">Back to Blog</a>
            </div>
        </article>
"""

MINECRAFT_CONTENT = """
        <article class="blog-post container">
            <header class="post-header">
                <span class="post-date">February 8, 2026</span>
                <h1 class="post-title">Building Dreams: Why Minecraft is My Architecture School</h1>
                <div class="post-tags">
                    <span class="tag">Minecraft</span>
                    <span class="tag">Architecture</span>
                    <span class="tag">Design</span>
                </div>
            </header>
            <div class="post-content text-block">
                <p>I want to be an architect. Minecraft Creative Mode is my training ground. Here's what Redstone taught me about engineering.</p>
                <p>Building in Minecraft is not just about blocks. It's about scale, lighting, and how a space feels when you walk through it. I spend hours designing modern villas and futuristic skyscrapers.</p>
            </div>
            <div class="post-navigation">
                <a href="../index.html" class="nav-link back">Back to Blog</a>
            </div>
        </article>
"""

# Build the posts
build_page("Genshin Piano", "Music & Piano", GENSHIN_PIANO_CONTENT, os.path.join(ROOT_DIR, "blog/posts/genshin-piano-music.html"), depth=2)
build_page("Roblox Obby", "Game Design", ROBLOX_OBBY_CONTENT, os.path.join(ROOT_DIR, "blog/posts/roblox-obby-design.html"), depth=2)
build_page("Minecraft Architecture", "Design & Engineering", MINECRAFT_CONTENT, os.path.join(ROOT_DIR, "blog/posts/minecraft-architecture.html"), depth=2)

print("\n🚀 All broken pages restored using the new master template!")
