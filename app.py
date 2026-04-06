from flask import Flask, render_template_string, request, url_for
import os

app = Flask(__name__)

POSTS = [
    {'id': 1, 'title': 'HTML5 Semantic Elements Complete Guide', 'slug': 'html5-semantic-elements', 'author': 'Tech Writer', 'date': '2026-03-24', 'category': 'HTML', 'excerpt': 'Master HTML5 semantic elements for better structure, SEO, and accessibility.', 'content': '<h2>Understanding HTML5 Semantic Elements</h2><p>HTML5 introduced semantic elements that describe their meaning to browsers and developers. They improve SEO, accessibility, and code readability.</p><h3>Common Semantic Elements</h3><ul><li><code>&lt;header&gt;</code> - Introductory content</li><li><code>&lt;nav&gt;</code> - Navigation links</li><li><code>&lt;main&gt;</code> - Main page content</li><li><code>&lt;article&gt;</code> - Self-contained content</li><li><code>&lt;section&gt;</code> - Thematic grouping</li><li><code>&lt;aside&gt;</code> - Sidebar content</li><li><code>&lt;footer&gt;</code> - Footer information</li></ul><h3>Benefits</h3><ul><li><strong>SEO:</strong> Search engines understand content better</li><li><strong>Accessibility:</strong> Screen readers navigate better</li><li><strong>Readability:</strong> Cleaner, maintainable code</li><li><strong>Mobile:</strong> Better rendering on devices</li></ul>'},
    {'id': 2, 'title': 'Flexbox vs Grid: When to Use Each', 'slug': 'flexbox-vs-grid', 'author': 'Tech Writer', 'date': '2026-03-22', 'category': 'CSS', 'excerpt': 'Learn when to use Flexbox vs Grid for optimal layouts.', 'content': '<h2>Flexbox vs CSS Grid</h2><p>Both are powerful layout tools serving different purposes.</p><h3>Flexbox Basics</h3><p>Designed for one-dimensional layouts (rows OR columns).</p><h3>Grid Basics</h3><p>Designed for two-dimensional layouts (rows AND columns).</p><h3>Use Flexbox For:</h3><ul><li>Navigation bars</li><li>Button groups</li><li>Single row/column alignment</li><li>Flexible spacing</li></ul><h3>Use Grid For:</h3><ul><li>Page layouts</li><li>Image galleries</li><li>Complex multi-section designs</li><li>Precise column control</li></ul>'},
    {'id': 3, 'title': 'JavaScript DOM Manipulation Essentials', 'slug': 'javascript-dom-manipulation', 'author': 'Tech Writer', 'date': '2026-03-21', 'category': 'JavaScript', 'excerpt': 'Master DOM manipulation to create interactive experiences.', 'content': '<h2>DOM Manipulation in JavaScript</h2><p>The DOM allows you to dynamically interact with HTML elements.</p><h3>Selecting Elements</h3><p>Use querySelector and querySelectorAll for modern selection.</p><h3>Modifying Elements</h3><p>Change text, HTML, classes, and styles dynamically.</p><h3>Creating Elements</h3><p>Use createElement and appendChild to add elements.</p><h3>Event Listeners</h3><p>addEventListener responds to user interactions.</p>'},
    {'id': 4, 'title': 'CSS Responsive Design: Mobile First Approach', 'slug': 'css-responsive-design', 'author': 'Tech Writer', 'date': '2026-03-19', 'category': 'CSS', 'excerpt': 'Build responsive sites using mobile-first approach.', 'content': '<h2>Responsive Design with Mobile First</h2><p>Build for mobile first, then enhance for larger screens.</p><h3>Viewport Meta Tag</h3><p>Always include for proper responsive behavior.</p><h3>Mobile-First Media Queries</h3><p>Start with mobile styles, add queries for larger screens.</p><h3>Responsive Images</h3><p>Use max-width and height: auto for adaptable images.</p>'},
    {'id': 5, 'title': 'JavaScript Promises and Error Handling', 'slug': 'javascript-promises', 'author': 'Tech Writer', 'date': '2026-03-17', 'category': 'JavaScript', 'excerpt': 'Understand Promises for async operations.', 'content': '<h2>Mastering JavaScript Promises</h2><p>Promises handle eventual completion of async operations.</p><h3>Promise States</h3><ul><li><strong>Pending:</strong> Initial state</li><li><strong>Fulfilled:</strong> Success</li><li><strong>Rejected:</strong> Failure</li></ul><h3>Promise Chaining</h3><p>Use .then() and .catch() for sequential operations.</p><h3>Promise.all() and Promise.race()</h3><p>Wait for all or first promise.</p>'},
    {'id': 6, 'title': 'CSS Animations and Transitions Guide', 'slug': 'css-animations', 'author': 'Tech Writer', 'date': '2026-03-16', 'category': 'CSS', 'excerpt': 'Create smooth animations and transitions.', 'content': '<h2>CSS Animations and Transitions</h2><p>Add polish with smooth, performant effects.</p><h3>CSS Transitions</h3><p>Smoothly change properties over time.</p><h3>Keyframe Animations</h3><p>Define animations with multiple states.</p><h3>Animation Properties</h3><ul><li>animation-name</li><li>animation-duration</li><li>animation-timing-function</li></ul>'},
    {'id': 7, 'title': 'Form Validation in HTML and JavaScript', 'slug': 'form-validation', 'author': 'Tech Writer', 'date': '2026-03-14', 'category': 'HTML', 'excerpt': 'Validate forms for better user experience.', 'content': '<h2>Form Validation Techniques</h2><p>Ensure data quality with proper validation.</p><h3>HTML5 Validation</h3><p>Use required, minlength, pattern attributes.</p><h3>JavaScript Validation</h3><p>Add custom validation logic.</p><h3>Custom Messages</h3><p>Use setCustomValidity for user-friendly errors.</p>'},
    {'id': 8, 'title': 'Web Performance Optimization Best Practices', 'slug': 'web-performance-optimization', 'author': 'Tech Writer', 'date': '2026-03-13', 'category': 'Web Dev', 'excerpt': 'Optimize sites for speed and performance.', 'content': '<h2>Web Performance Optimization</h2><p>Speed is critical for UX and SEO.</p><h3>Image Optimization</h3><p>Use modern formats and lazy loading.</p><h3>CSS Optimization</h3><ul><li>Minify CSS</li><li>Remove unused styles</li><li>Defer non-critical CSS</li></ul><h3>JavaScript Optimization</h3><p>Use defer/async, lazy load libraries.</p>'},
    {'id': 9, 'title': 'JavaScript Event Handling and Delegation', 'slug': 'javascript-event-handling', 'author': 'Tech Writer', 'date': '2026-03-12', 'category': 'JavaScript', 'excerpt': 'Master event handling for DOM interaction.', 'content': '<h2>Event Handling and Delegation</h2><p>Learn to handle user actions efficiently.</p><h3>Basic Event Listeners</h3><p>Use addEventListener for DOM interaction.</p><h3>Event Delegation</h3><p>Listen on parent, handle child events.</p><h3>Stopping Propagation</h3><p>Use preventDefault and stopPropagation.</p>'},
    {'id': 10, 'title': 'CSS Variables (Custom Properties) Guide', 'slug': 'css-variables-guide', 'author': 'Tech Writer', 'date': '2026-03-11', 'category': 'CSS', 'excerpt': 'Use CSS variables for maintainable stylesheets.', 'content': '<h2>CSS Variables and Custom Properties</h2><p>Store and reuse values throughout CSS.</p><h3>Defining Variables</h3><p>Use :root for global variables.</p><h3>Using Variables</h3><p>Reference with var(--variable-name).</p><h3>JavaScript Integration</h3><p>Change variables dynamically with JavaScript.</p>'},
    {'id': 11, 'title': 'HTML Forms Advanced Features', 'slug': 'html-forms-advanced', 'author': 'Tech Writer', 'date': '2026-03-10', 'category': 'HTML', 'excerpt': 'Explore advanced HTML form features.', 'content': '<h2>Advanced HTML Form Features</h2><p>HTML5 provides powerful form enhancements.</p><h3>Input Types</h3><p>Email, password, number, date, color, and more.</p><h3>Datalist (Autocomplete)</h3><p>Provide suggestions without JavaScript.</p><h3>Progress and Meter</h3><p>Display progress and gauge elements.</p>'},
    {'id': 12, 'title': 'Building a Modern Navbar with HTML and CSS', 'slug': 'modern-navbar-guide', 'author': 'Tech Writer', 'date': '2026-03-09', 'category': 'CSS', 'excerpt': 'Create responsive navigation bars.', 'content': '<h2>Building Modern Navigation Bars</h2><p>Essential for website navigation.</p><h3>HTML Structure</h3><p>Use semantic nav and ul elements.</p><h3>CSS Styling</h3><p>Style with flexbox and transitions.</p><h3>Mobile Responsive</h3><p>Implement hamburger menus for mobile.</p>'},
    {'id': 13, 'title': 'Web Accessibility Best Practices (A11y)', 'slug': 'web-accessibility-a11y', 'author': 'Tech Writer', 'date': '2026-03-08', 'category': 'Web Dev', 'excerpt': 'Make websites accessible to everyone.', 'content': '<h2>Web Accessibility (A11y) Best Practices</h2><p>Ensure sites are usable by everyone.</p><h3>Semantic HTML</h3><p>Use proper semantic elements.</p><h3>ARIA Attributes</h3><p>Enhance screen reader support.</p><h3>Color Contrast</h3><p>Ensure sufficient contrast ratios.</p>'},
    {'id': 14, 'title': 'Advanced JavaScript Array Methods: Map, Filter, and Reduce', 'slug': 'javascript-array-methods', 'author': 'Tech Writer', 'date': '2026-03-27', 'category': 'JavaScript', 'excerpt': 'Master array methods for elegant data transformation.', 'content': '<h2>Mastering Advanced Array Methods</h2><p>Array methods like map, filter, and reduce are cornerstone concepts in modern JavaScript development.</p>'},
    {'id': 15, 'title': 'Building Accessible Web Components: ARIA and Inclusive Design', 'slug': 'accessible-web-components', 'author': 'Tech Writer', 'date': '2026-03-26', 'category': 'Web Dev', 'excerpt': 'Create inclusive experiences with ARIA and semantic HTML.', 'content': '<h2>Understanding Web Accessibility and Its Importance</h2><p>Web accessibility ensures that everyone can use your website, regardless of ability.</p>'},
    {'id': 16, 'title': 'CSS Preprocessors: SASS and SCSS for Enterprise-Scale Styling', 'slug': 'css-preprocessors-sass', 'author': 'Tech Writer', 'date': '2026-03-25', 'category': 'CSS', 'excerpt': 'Master SASS and SCSS for scalable CSS at enterprise level.', 'content': '<h2>Understanding CSS Preprocessors and Their Value</h2><p>CSS preprocessors like SASS extend CSS with programming features.</p>'},
]

# Base HTML template with canonical tags
BASE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TechHub - Tech Blog{% endblock %}</title>
    <meta name="description" content="{% block description %}Learn web development, HTML, CSS, and JavaScript{% endblock %}">
    <!-- CANONICAL TAG - FIXES GOOGLE SEARCH CONSOLE DUPLICATE CONTENT WARNING -->
    <link rel="canonical" href="{{ canonical_url }}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pico-css/css/pico.min.css">
    <style>
        :root {
            --form-element-valid-border-color: #10b981;
            --transition: all 0.3s ease;
        }
        
        * {
            scroll-behavior: smooth;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 2rem 0;
            margin-bottom: 3rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        nav {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }
        
        nav a {
            padding: 0.5rem 1rem;
            background: #f0f0f0;
            text-decoration: none;
            border-radius: 8px;
            transition: var(--transition);
            color: #333;
            font-weight: 500;
        }
        
        nav a:hover {
            background: #667eea;
            color: white;
        }
        
        nav a.active {
            background: #764ba2;
            color: white;
        }
        
        .posts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }
        
        article {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: var(--transition);
            cursor: pointer;
            border: 2px solid transparent;
        }
        
        article:hover {
            transform: translateY(-5px);
            border-color: #667eea;
            box-shadow: 0 12px 48px rgba(102, 126, 234, 0.3);
        }
        
        .post-meta {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
            font-size: 0.9rem;
            color: #666;
        }
        
        .category-tag {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .post-title {
            font-size: 1.5rem;
            margin: 1rem 0;
            color: #333;
            text-decoration: none;
        }
        
        .post-title:hover {
            color: #667eea;
        }
        
        .excerpt {
            color: #555;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        .read-more {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }
        
        .read-more:hover {
            color: #764ba2;
        }
        
        .full-post {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            line-height: 1.8;
        }
        
        .full-post h2 {
            color: #667eea;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        
        .full-post h3 {
            color: #764ba2;
            margin-top: 1.5rem;
        }
        
        .back-link {
            display: inline-block;
            margin-bottom: 2rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: var(--transition);
        }
        
        .back-link:hover {
            transform: translateX(-5px);
        }
        
        footer {
            text-align: center;
            padding: 2rem;
            color: white;
            margin-top: 3rem;
        }
        
        .carousel-container {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 3rem;
            overflow-x: auto;
        }
        
        .carousel {
            display: flex;
            gap: 1rem;
            min-width: 100%;
        }
        
        .carousel-item {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            min-width: 300px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 TechHub</h1>
            <p>Master web development with in-depth tutorials and guides</p>
            <nav>
                <a href="/" {% if current_page == 'home' %}class="active"{% endif %}>Home</a>
                <a href="/?category=HTML" {% if current_category == 'HTML' %}class="active"{% endif %}>HTML</a>
                <a href="/?category=CSS" {% if current_category == 'CSS' %}class="active"{% endif %}>CSS</a>
                <a href="/?category=JavaScript" {% if current_category == 'JavaScript' %}class="active"{% endif %}>JavaScript</a>
                <a href="/?category=Web Dev" {% if current_category == 'Web Dev' %}class="active"{% endif %}>Web Dev</a>
            </nav>
        </header>
        
        {% block content %}{% endblock %}
        
        <footer>
            <p>&copy; 2026 TechHub. All rights reserved. | Powered by Flask</p>
        </footer>
    </div>
</body>
</html>
'''

# Homepage template
HOME_TEMPLATE = BASE_TEMPLATE + '''
{% block title %}TechHub - Learn Web Development{% endblock %}
{% block description %}Master HTML, CSS, JavaScript, and web development with comprehensive tutorials from TechHub{% endblock %}
{% block content %}
<section class="carousel-container">
    <div class="carousel">
        <div class="carousel-item">
            <h3>📚 Latest Articles</h3>
            <p>Stay updated with fresh web development content every week</p>
        </div>
        <div class="carousel-item">
            <h3>🎯 Skill Progression</h3>
            <p>Learn from beginner to advanced concepts systematically</p>
        </div>
        <div class="carousel-item">
            <h3>💡 Practical Examples</h3>
            <p>Real-world code examples you can use in your projects</p>
        </div>
        <div class="carousel-item">
            <h3>🔧 Best Practices</h3>
            <p>Industry-standard techniques and patterns explained</p>
        </div>
    </div>
</section>

<main>
    <section class="posts-grid">
        {% for post in posts %}
        <article onclick="window.location='/post/{{ post.slug }}'">
            <div class="post-meta">
                <span>{{ post.date }}</span>
                <span class="category-tag">{{ post.category }}</span>
            </div>
            <a href="/post/{{ post.slug }}" class="post-title">{{ post.title }}</a>
            <p class="excerpt">{{ post.excerpt }}</p>
            <a href="/post/{{ post.slug }}" class="read-more">Read More →</a>
        </article>
        {% endfor %}
    </section>
</main>
{% endblock %}
'''

# Post template
POST_TEMPLATE = BASE_TEMPLATE + '''
{% block title %}{{ post.title }} - TechHub{% endblock %}
{% block description %}{{ post.excerpt }}{% endblock %}
{% block content %}
<a href="/" class="back-link">← Back to Home</a>

<article class="full-post">
    <div class="post-meta">
        <span>{{ post.date }}</span>
        <span>By {{ post.author }}</span>
        <span class="category-tag">{{ post.category }}</span>
    </div>
    <h1>{{ post.title }}</h1>
    {{ post.content | safe }}
</article>
{% endblock %}
'''

@app.route('/')
def home():
    current_category = request.args.get('category', None)
    posts = POSTS
    
    if current_category:
        posts = [p for p in POSTS if p['category'] == current_category]
    
    # Sort by date descending
    posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    
    # Build canonical URL (no query params for consistency)
    canonical_url = url_for('home', _external=True)
    
    return render_template_string(
        HOME_TEMPLATE,
        posts=posts,
        current_page='home',
        current_category=current_category,
        canonical_url=canonical_url
    )

@app.route('/post/<slug>')
def post(slug):
    post_item = next((p for p in POSTS if p['slug'] == slug), None)
    
    if not post_item:
        return "Post not found", 404
    
    # Build canonical URL for this specific post
    canonical_url = url_for('post', slug=slug, _external=True)
    
    return render_template_string(
        POST_TEMPLATE,
        post=post_item,
        current_page='post',
        current_category=post_item['category'],
        canonical_url=canonical_url
    )

# Google AdSense integration (if you have an AdSense account)
@app.route('/robots.txt')
def robots():
    return '''User-agent: *
Allow: /
Disallow: /admin

Sitemap: https://yourdomain.com/sitemap.xml
'''

@app.route('/sitemap.xml')
def sitemap():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Homepage
    xml += f'  <url>\n'
    xml += f'    <loc>{url_for("home", _external=True)}</loc>\n'
    xml += f'    <lastmod>2026-03-27</lastmod>\n'
    xml += f'    <changefreq>weekly</changefreq>\n'
    xml += f'  </url>\n'
    
    # Individual posts
    for post in POSTS:
        xml += f'  <url>\n'
        xml += f'    <loc>{url_for("post", slug=post["slug"], _external=True)}</loc>\n'
        xml += f'    <lastmod>{post["date"]}</lastmod>\n'
        xml += f'    <changefreq>monthly</changefreq>\n'
        xml += f'  </url>\n'
    
    xml += '</urlset>'
    return xml, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(debug=True),port5000)
