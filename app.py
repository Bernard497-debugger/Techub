from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Sample blog posts data
POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Python Flask',
        'slug': 'python-flask-intro',
        'author': 'Tech Writer',
        'date': '2026-03-20',
        'category': 'Python',
        'excerpt': 'Learn how to build web applications with Flask, the lightweight Python web framework.',
        'content': '''
        <h2>Introduction to Flask</h2>
        <p>Flask is a popular Python web framework that makes it easy to build web applications. It's lightweight, flexible, and perfect for both beginners and experienced developers.</p>
        
        <h3>Why Choose Flask?</h3>
        <ul>
            <li><strong>Lightweight:</strong> Minimal overhead, maximum flexibility</li>
            <li><strong>Flexible:</strong> Choose your own tools and libraries</li>
            <li><strong>Great Documentation:</strong> Community support is excellent</li>
            <li><strong>Easy to Learn:</strong> Perfect for beginners</li>
        </ul>
        
        <h3>Installation</h3>
        <pre><code>pip install flask</code></pre>
        
        <h3>Your First Flask App</h3>
        <pre><code>from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)</code></pre>
        
        <p>That's it! You now have a working Flask application. Run it with <code>python app.py</code> and visit <code>http://localhost:5000</code>.</p>
        '''
    },
    {
        'id': 2,
        'title': 'JavaScript Async/Await Explained',
        'slug': 'javascript-async-await',
        'author': 'Tech Writer',
        'date': '2026-03-18',
        'category': 'JavaScript',
        'excerpt': 'Master asynchronous programming in JavaScript with async/await syntax.',
        'content': '''
        <h2>Understanding Async/Await</h2>
        <p>Async/await is a modern way to handle asynchronous operations in JavaScript, making your code cleaner and easier to read.</p>
        
        <h3>What is Async/Await?</h3>
        <p>Async/await allows you to write asynchronous code that looks and behaves more like synchronous code, making it easier to understand and debug.</p>
        
        <h3>Basic Syntax</h3>
        <pre><code>async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}</code></pre>
        
        <h3>Key Points</h3>
        <ul>
            <li>Use <code>async</code> keyword to declare an async function</li>
            <li>Use <code>await</code> to wait for a Promise to resolve</li>
            <li>Always use try/catch for error handling</li>
            <li>Async functions always return a Promise</li>
        </ul>
        '''
    },
    {
        'id': 3,
        'title': 'CSS Grid Layout Masterclass',
        'slug': 'css-grid-layout',
        'author': 'Tech Writer',
        'date': '2026-03-15',
        'category': 'CSS',
        'excerpt': 'Create responsive layouts with CSS Grid, the modern way to build web layouts.',
        'content': '''
        <h2>Mastering CSS Grid</h2>
        <p>CSS Grid is a powerful layout system that lets you create complex, responsive layouts with ease.</p>
        
        <h3>Grid Basics</h3>
        <p>A grid container holds grid items arranged in rows and columns.</p>
        
        <h3>Creating a Grid</h3>
        <pre><code>.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: auto;
    gap: 20px;
}</code></pre>
        
        <h3>Responsive Grids</h3>
        <pre><code>@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr;
    }
}</code></pre>
        
        <p>CSS Grid makes building responsive layouts straightforward and maintainable.</p>
        '''
    }
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechBlog - Coding Tutorials & Guides</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #0f172a;
            --secondary: #1e293b;
            --accent: #3b82f6;
            --accent-dark: #1d4ed8;
            --text: #f1f5f9;
            --text-muted: #cbd5e1;
            --border: #334155;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--primary) 0%, #1a202c 100%);
            color: var(--text);
            line-height: 1.6;
            min-height: 100vh;
        }

        /* Header */
        header {
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
            padding: 1.5rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent) 0%, #60a5fa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            margin-left: 2rem;
            transition: color 0.3s;
            font-size: 0.95rem;
        }

        nav a:hover {
            color: var(--accent);
        }

        /* Main Content */
        main {
            max-width: 1200px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 4rem;
            animation: fadeIn 0.8s ease-out;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            letter-spacing: -1px;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto;
        }

        /* Grid Layout */
        .posts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .post-card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1);
            cursor: pointer;
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(5px);
        }

        .post-card:hover {
            background: rgba(30, 41, 59, 0.8);
            border-color: var(--accent);
            transform: translateY(-4px);
            box-shadow: 0 20px 50px rgba(59, 130, 246, 0.1);
        }

        .post-category {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: rgba(59, 130, 246, 0.15);
            color: var(--accent);
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 1rem;
            width: fit-content;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .post-card h3 {
            font-size: 1.4rem;
            margin-bottom: 0.8rem;
            color: var(--text);
        }

        .post-meta {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }

        .post-excerpt {
            color: var(--text-muted);
            margin-bottom: 1.5rem;
            flex-grow: 1;
        }

        .read-more {
            color: var(--accent);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: gap 0.3s;
        }

        .read-more:hover {
            gap: 0.8rem;
        }

        /* Post Page */
        .post-full {
            max-width: 800px;
            margin: 0 auto;
            animation: fadeIn 0.8s ease-out;
        }

        .post-header {
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border);
        }

        .post-header h1 {
            font-size: 2.8rem;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .post-header .post-meta {
            display: flex;
            gap: 2rem;
            flex-wrap: wrap;
        }

        .post-content {
            font-size: 1.05rem;
            line-height: 1.8;
        }

        .post-content h2 {
            font-size: 1.8rem;
            margin: 2rem 0 1rem 0;
        }

        .post-content h3 {
            font-size: 1.3rem;
            margin: 1.5rem 0 0.8rem 0;
        }

        .post-content p {
            margin-bottom: 1.5rem;
        }

        .post-content ul, .post-content ol {
            margin-left: 2rem;
            margin-bottom: 1.5rem;
        }

        .post-content li {
            margin-bottom: 0.8rem;
        }

        .post-content pre {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem;
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }

        .post-content code {
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            color: #a5f3fc;
        }

        .post-content pre code {
            color: #a5f3fc;
        }

        /* AdSense Placeholder */
        .ad-container {
            background: rgba(30, 41, 59, 0.5);
            border: 1px dashed var(--border);
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
            margin: 2rem 0;
            min-height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 1rem;
        }

        .ad-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* Back Button */
        .back-button {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--accent);
            text-decoration: none;
            margin-bottom: 2rem;
            transition: gap 0.3s;
        }

        .back-button:hover {
            gap: 1rem;
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.95);
            border-top: 1px solid var(--border);
            padding: 3rem 2rem;
            margin-top: 4rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            color: var(--text-muted);
        }

        .footer-content p {
            margin-bottom: 0.5rem;
        }

        /* Animations */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.2rem;
            }

            .header-content {
                flex-direction: column;
                gap: 1rem;
            }

            nav a {
                margin-left: 1rem;
            }

            .post-card {
                padding: 1.5rem;
            }

            .post-header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">TechBlog</div>
            <nav>
                <a href="/">Home</a>
                <a href="#about">About</a>
                <a href="#contact">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        {% if current_page == 'home' %}
            <section class="hero">
                <h1>Coding Tutorials & Tech Guides</h1>
                <p>Master web development, programming, and modern web technologies. Learn from detailed tutorials and best practices.</p>
            </section>

            <div class="ad-container">
                <div class="ad-label">Advertisement</div>
                <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926"
                     crossorigin="anonymous"></script>
                <ins class="adsbygoogle"
                     style="display:block"
                     data-ad-client="ca-pub-5573963043624926"
                     data-ad-format="auto"
                     data-full-width-responsive="true"></ins>
                <script>
                     (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
            </div>

            <div class="posts-grid">
                {% for post in posts %}
                    <div class="post-card" onclick="window.location='/post/{{ post.slug }}'">
                        <span class="post-category">{{ post.category }}</span>
                        <h3>{{ post.title }}</h3>
                        <div class="post-meta">{{ post.date }} • By {{ post.author }}</div>
                        <p class="post-excerpt">{{ post.excerpt }}</p>
                        <a href="/post/{{ post.slug }}" class="read-more">Read More →</a>
                    </div>
                {% endfor %}
            </div>

            <div class="ad-container">
                <div class="ad-label">Advertisement</div>
                <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926"
                     crossorigin="anonymous"></script>
                <ins class="adsbygoogle"
                     style="display:block"
                     data-ad-client="ca-pub-5573963043624926"
                     data-ad-format="auto"
                     data-full-width-responsive="true"></ins>
                <script>
                     (adsbygoogle = window.adsbygoogle || []).push({});
                </script>
            </div>

        {% else %}
            <a href="/" class="back-button">← Back to Posts</a>
            <div class="post-full">
                <div class="post-header">
                    <span class="post-category">{{ current_post.category }}</span>
                    <h1>{{ current_post.title }}</h1>
                    <div class="post-meta">
                        <span>{{ current_post.date }}</span>
                        <span>By {{ current_post.author }}</span>
                    </div>
                </div>

                <div class="ad-container">
                    <div class="ad-label">Advertisement</div>
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926"
                         crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-client="ca-pub-5573963043624926"
                         data-ad-format="auto"
                         data-full-width-responsive="true"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>

                <div class="post-content">
                    {{ current_post.content|safe }}
                </div>

                <div class="ad-container">
                    <div class="ad-label">Advertisement</div>
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926"
                         crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-client="ca-pub-5573963043624926"
                         data-ad-format="auto"
                         data-full-width-responsive="true"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>
            </div>
        {% endif %}
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2026 TechBlog. All rights reserved.</p>
            <p>Building amazing tech content for developers everywhere.</p>
        </div>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, current_page='home', posts=POSTS)

@app.route('/post/<slug>')
def post(slug):
    post = next((p for p in POSTS if p['slug'] == slug), None)
    if not post:
        return "Post not found", 404
    return render_template_string(HTML_TEMPLATE, current_page='post', current_post=post)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
