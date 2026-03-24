from flask import Flask, render_template_string
import os

app = Flask(__name__)

POSTS = [
    {
        'id': 1,
        'title': 'HTML5 Semantic Elements Complete Guide',
        'slug': 'html5-semantic-elements',
        'author': 'Tech Writer',
        'date': '2026-03-24',
        'category': 'HTML',
        'excerpt': 'Master HTML5 semantic elements for better structure, SEO, and accessibility in your web projects.',
        'content': '<h2>Understanding HTML5 Semantic Elements</h2><p>HTML5 introduced semantic elements that clearly describe their meaning to both the browser and developer. They improve SEO, accessibility, and code readability.</p><h3>Common Semantic Elements</h3><ul><li><code>&lt;header&gt;</code> - Introductory content or navigation</li><li><code>&lt;nav&gt;</code> - Navigation links</li><li><code>&lt;main&gt;</code> - Main content of the page</li><li><code>&lt;article&gt;</code> - Self-contained content</li><li><code>&lt;section&gt;</code> - Thematic grouping of content</li><li><code>&lt;aside&gt;</code> - Sidebar or related content</li><li><code>&lt;footer&gt;</code> - Footer information</li></ul><h3>Benefits of Semantic HTML</h3><ul><li><strong>SEO:</strong> Search engines better understand your content</li><li><strong>Accessibility:</strong> Screen readers can navigate better</li><li><strong>Readability:</strong> Cleaner, more maintainable code</li><li><strong>Mobile:</strong> Better rendering on mobile devices</li></ul>'
    },
    {
        'id': 2,
        'title': 'Flexbox vs Grid: When to Use Each',
        'slug': 'flexbox-vs-grid',
        'author': 'Tech Writer',
        'date': '2026-03-22',
        'category': 'CSS',
        'excerpt': 'Learn the differences between Flexbox and CSS Grid, and when to use each one for optimal layouts.',
        'content': '<h2>Flexbox vs CSS Grid</h2><p>Both Flexbox and Grid are powerful layout tools, but they serve different purposes. Understanding when to use each is crucial for modern web design.</p><h3>Flexbox Basics</h3><p>Flexbox is designed for one-dimensional layouts (rows or columns).</p><h3>Grid Basics</h3><p>Grid is designed for two-dimensional layouts (rows AND columns).</p><h3>Use Flexbox When:</h3><ul><li>Building navigation bars</li><li>Creating button groups</li><li>Aligning items in a single row or column</li><li>Need flexible spacing and alignment</li></ul><h3>Use Grid When:</h3><ul><li>Building page layouts</li><li>Creating image galleries</li><li>Need both rows AND columns control</li><li>Building complex, multi-section layouts</li></ul>'
    },
    {
        'id': 3,
        'title': 'JavaScript DOM Manipulation Essentials',
        'slug': 'javascript-dom-manipulation',
        'author': 'Tech Writer',
        'date': '2026-03-21',
        'category': 'JavaScript',
        'excerpt': 'Master DOM manipulation in JavaScript to dynamically modify HTML and create interactive web experiences.',
        'content': '<h2>DOM Manipulation in JavaScript</h2><p>The Document Object Model (DOM) allows you to interact with HTML elements dynamically. This is core to building interactive web applications.</p><h3>Selecting Elements</h3><p>Modern ways to select elements include querySelector and querySelectorAll.</p><h3>Modifying Elements</h3><p>Change text content, HTML, classes, and styles dynamically.</p><h3>Creating Elements</h3><p>Use document.createElement to create new DOM elements and appendChild to add them to the page.</p><h3>Event Listeners</h3><p>addEventListener allows you to respond to user interactions like clicks and form submissions.</p>'
    },
    {
        'id': 4,
        'title': 'CSS Responsive Design: Mobile First Approach',
        'slug': 'css-responsive-design',
        'author': 'Tech Writer',
        'date': '2026-03-19',
        'category': 'CSS',
        'excerpt': 'Build responsive websites using the mobile-first approach and media queries for all screen sizes.',
        'content': '<h2>Responsive Design with Mobile First</h2><p>Mobile-first design means building for mobile devices first, then enhancing for larger screens.</p><h3>Viewport Meta Tag</h3><p>Always include the viewport meta tag in your HTML head for proper responsive behavior.</p><h3>Mobile-First Media Queries</h3><p>Start with mobile styles, then add media queries for larger screens using min-width.</p><h3>Responsive Images</h3><p>Use max-width: 100% and height: auto to make images responsive across all devices.</p>'
    },
    {
        'id': 5,
        'title': 'JavaScript Promises and Error Handling',
        'slug': 'javascript-promises',
        'author': 'Tech Writer',
        'date': '2026-03-17',
        'category': 'JavaScript',
        'excerpt': 'Understand JavaScript Promises for handling asynchronous operations and proper error handling.',
        'content': '<h2>Mastering JavaScript Promises</h2><p>Promises represent the eventual completion of an asynchronous operation and its resulting value.</p><h3>Promise States</h3><ul><li><strong>Pending:</strong> Initial state</li><li><strong>Fulfilled:</strong> Operation completed successfully</li><li><strong>Rejected:</strong> Operation failed</li></ul><h3>Promise Chaining</h3><p>Chain promises using .then() and .catch() for sequential async operations.</p><h3>Promise.all() and Promise.race()</h3><p>Use Promise.all to wait for all promises or Promise.race for the first one.</p>'
    },
    {
        'id': 6,
        'title': 'CSS Animations and Transitions Guide',
        'slug': 'css-animations',
        'author': 'Tech Writer',
        'date': '2026-03-16',
        'category': 'CSS',
        'excerpt': 'Create smooth animations and transitions with CSS to enhance user experience and interactivity.',
        'content': '<h2>CSS Animations and Transitions</h2><p>Animations and transitions add polish to your web design with smooth, performant effects.</p><h3>CSS Transitions</h3><p>Transitions smoothly change property values over time with the transition property.</p><h3>CSS Keyframe Animations</h3><p>Use @keyframes to define animations with multiple states and apply them to elements.</p><h3>Animation Properties</h3><ul><li><code>animation-name</code> - Name of the keyframes</li><li><code>animation-duration</code> - How long the animation takes</li><li><code>animation-timing-function</code> - Speed curve</li></ul>'
    },
    {
        'id': 7,
        'title': 'Form Validation in HTML and JavaScript',
        'slug': 'form-validation',
        'author': 'Tech Writer',
        'date': '2026-03-14',
        'category': 'HTML',
        'excerpt': 'Learn to validate HTML forms both on the client-side with HTML5 and JavaScript for better user experience.',
        'content': '<h2>Form Validation Techniques</h2><p>Proper form validation ensures data quality and improves user experience.</p><h3>HTML5 Validation</h3><p>Use built-in HTML5 attributes like required, minlength, and pattern for client-side validation.</p><h3>JavaScript Form Validation</h3><p>Add custom validation logic with JavaScript for more complex requirements.</p><h3>Custom Error Messages</h3><p>Use setCustomValidity() to provide user-friendly error messages.</p>'
    },
    {
        'id': 8,
        'title': 'Web Performance Optimization Best Practices',
        'slug': 'web-performance-optimization',
        'author': 'Tech Writer',
        'date': '2026-03-13',
        'category': 'Web Dev',
        'excerpt': 'Optimize your websites for speed and performance using proven techniques and best practices.',
        'content': '<h2>Web Performance Optimization</h2><p>Website speed is critical for user experience and SEO. Here are proven techniques.</p><h3>Image Optimization</h3><p>Use modern formats like WebP and implement lazy loading for better performance.</p><h3>CSS Optimization</h3><ul><li>Minify CSS files</li><li>Remove unused CSS</li><li>Defer non-critical CSS</li></ul><h3>JavaScript Optimization</h3><p>Use defer and async attributes, and lazy load heavy libraries when needed.</p>'
    },
    {
        'id': 9,
        'title': 'JavaScript Event Handling and Delegation',
        'slug': 'javascript-event-handling',
        'author': 'Tech Writer',
        'date': '2026-03-12',
        'category': 'JavaScript',
        'excerpt': 'Master event handling and event delegation in JavaScript for efficient DOM interaction.',
        'content': '<h2>Event Handling and Delegation</h2><p>Events are user actions like clicks and key presses. Learn to handle them efficiently.</p><h3>Basic Event Listeners</h3><p>Use addEventListener to respond to events on DOM elements.</p><h3>Event Delegation</h3><p>Add listeners to parent elements and use event.target to handle child events efficiently.</p><h3>Stopping Event Propagation</h3><p>Use preventDefault() and stopPropagation() to control event behavior.</p>'
    },
    {
        'id': 10,
        'title': 'CSS Variables (Custom Properties) Guide',
        'slug': 'css-variables-guide',
        'author': 'Tech Writer',
        'date': '2026-03-11',
        'category': 'CSS',
        'excerpt': 'Learn to use CSS variables for dynamic, maintainable, and reusable stylesheets.',
        'content': '<h2>CSS Variables and Custom Properties</h2><p>CSS variables allow you to store and reuse values throughout your stylesheets.</p><h3>Defining Variables</h3><p>Use the :root selector to define global variables accessible throughout your site.</p><h3>Using Variables</h3><p>Reference variables with var(--variable-name) in any CSS property.</p><h3>JavaScript Integration</h3><p>Change CSS variables dynamically with JavaScript for theme switching.</p>'
    },
    {
        'id': 11,
        'title': 'HTML Forms Advanced Features',
        'slug': 'html-forms-advanced',
        'author': 'Tech Writer',
        'date': '2026-03-10',
        'category': 'HTML',
        'excerpt': 'Explore advanced HTML form features like datalists, progress bars, and input types.',
        'content': '<h2>Advanced HTML Form Features</h2><p>HTML5 introduced many powerful form features that improve user experience and validation.</p><h3>Input Types</h3><p>HTML5 provides specialized input types for email, password, number, date, color, and more.</p><h3>Datalist (Autocomplete)</h3><p>Use datalist elements to provide autocomplete suggestions without JavaScript.</p><h3>Progress and Meter</h3><p>Display progress bars and gauges with native HTML elements.</p>'
    },
    {
        'id': 12,
        'title': 'Building a Modern Navbar with HTML and CSS',
        'slug': 'modern-navbar-guide',
        'author': 'Tech Writer',
        'date': '2026-03-09',
        'category': 'CSS',
        'excerpt': 'Create a responsive navigation bar with HTML and CSS that works on all devices.',
        'content': '<h2>Building Modern Navigation Bars</h2><p>A well-designed navbar is essential for website navigation and user experience.</p><h3>Basic HTML Structure</h3><p>Use semantic HTML with nav and ul elements for accessible navigation.</p><h3>CSS Styling</h3><p>Style with flexbox for alignment and smooth transitions for hover effects.</p><h3>Mobile Responsive</h3><p>Implement hamburger menus for mobile using CSS and media queries.</p>'
    },
    {
        'id': 13,
        'title': 'Web Accessibility Best Practices (A11y)',
        'slug': 'web-accessibility-a11y',
        'author': 'Tech Writer',
        'date': '2026-03-08',
        'category': 'Web Dev',
        'excerpt': 'Make your websites accessible to everyone with proper semantic HTML and ARIA attributes.',
        'content': '<h2>Web Accessibility (A11y) Best Practices</h2><p>Accessibility ensures your website is usable by everyone, including people with disabilities.</p><h3>Semantic HTML</h3><p>Use proper semantic elements instead of generic divs for better accessibility.</p><h3>ARIA Attributes</h3><p>Add aria-label and aria-live to enhance screen reader support.</p><h3>Color Contrast</h3><p>Ensure sufficient contrast ratios for readability.</p>'
    }
]

HTML_TEMPLATE = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="google-site-verification" content="add-your-verification-code-here"><title>TechBlog - Coding Tutorials & Guides</title><style>*{margin:0;padding:0;box-sizing:border-box}:root{--primary:#0f172a;--secondary:#1e293b;--accent:#3b82f6;--text:#f1f5f9;--text-muted:#cbd5e1;--border:#334155}body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:linear-gradient(135deg,var(--primary) 0%,#1a202c 100%);color:var(--text);line-height:1.6;min-height:100vh}header{background:rgba(15,23,42,0.95);backdrop-filter:blur(10px);border-bottom:1px solid var(--border);padding:1.5rem 0;position:sticky;top:0;z-index:1000}.header-content{max-width:1200px;margin:0 auto;padding:0 2rem;display:flex;justify-content:space-between;align-items:center}.logo{font-size:1.8rem;font-weight:700;background:linear-gradient(135deg,var(--accent) 0%,#60a5fa 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}nav a{color:var(--text-muted);text-decoration:none;margin-left:2rem;transition:color 0.3s;font-size:0.95rem}nav a:hover{color:var(--accent)}main{max-width:1200px;margin:0 auto;padding:3rem 2rem}.hero{text-align:center;margin-bottom:4rem;animation:fadeIn 0.8s ease-out}.hero h1{font-size:3.5rem;font-weight:800;margin-bottom:1rem;line-height:1.2}.hero p{font-size:1.2rem;color:var(--text-muted);max-width:600px;margin:0 auto}.posts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:2rem;margin-bottom:3rem}.post-card{background:rgba(30,41,59,0.5);border:1px solid var(--border);border-radius:12px;padding:2rem;transition:all 0.3s;cursor:pointer;display:flex;flex-direction:column;backdrop-filter:blur(5px)}.post-card:hover{background:rgba(30,41,59,0.8);border-color:var(--accent);transform:translateY(-4px);box-shadow:0 20px 50px rgba(59,130,246,0.1)}.post-category{display:inline-block;padding:0.4rem 0.8rem;background:rgba(59,130,246,0.15);color:var(--accent);border-radius:20px;font-size:0.75rem;font-weight:600;margin-bottom:1rem;width:fit-content;text-transform:uppercase}.post-card h3{font-size:1.4rem;margin-bottom:0.8rem}.post-meta{font-size:0.85rem;color:var(--text-muted);margin-bottom:1rem}.post-excerpt{color:var(--text-muted);margin-bottom:1.5rem;flex-grow:1}.read-more{color:var(--accent);text-decoration:none;font-weight:600}.post-full{max-width:800px;margin:0 auto;animation:fadeIn 0.8s ease-out}.post-header{margin-bottom:3rem;padding-bottom:2rem;border-bottom:1px solid var(--border)}.post-header h1{font-size:2.8rem;margin-bottom:1rem;line-height:1.2}.post-content{font-size:1.05rem;line-height:1.8}.post-content h2{font-size:1.8rem;margin:2rem 0 1rem 0}.post-content h3{font-size:1.3rem;margin:1.5rem 0 0.8rem 0}.post-content p{margin-bottom:1.5rem}.post-content ul{margin-left:2rem;margin-bottom:1.5rem}.post-content li{margin-bottom:0.8rem}.ad-container{background:rgba(30,41,59,0.5);border:1px dashed var(--border);border-radius:8px;padding:2rem;text-align:center;margin:2rem 0;min-height:250px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1rem}.ad-label{font-size:0.75rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px}.back-button{display:inline-flex;align-items:center;gap:0.5rem;color:var(--accent);text-decoration:none;margin-bottom:2rem}footer{background:rgba(15,23,42,0.95);border-top:1px solid var(--border);padding:3rem 2rem;margin-top:4rem}.footer-content{max-width:1200px;margin:0 auto;text-align:center;color:var(--text-muted)}.footer-content p{margin-bottom:0.5rem}.footer-links{margin-top:1.5rem;display:flex;gap:2rem;justify-content:center;flex-wrap:wrap}@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}@media(max-width:768px){.hero h1{font-size:2.2rem}.post-card{padding:1.5rem}}</style></head><body><header><div class="header-content"><div class="logo">TechBlog</div><nav><a href="/">Home</a></nav></div></header><main>{% if current_page == 'home' %}<section class="hero"><h1>Coding Tutorials & Tech Guides</h1><p>Master web development with detailed tutorials and best practices.</p></section><div class="ad-container"><div class="ad-label">Advertisement</div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926" crossorigin="anonymous"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5573963043624926" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div><div class="posts-grid">{% for post in posts %}<div class="post-card" onclick="window.location=\'/post/{{ post.slug }}\'"><span class="post-category">{{ post.category }}</span><h3>{{ post.title }}</h3><div class="post-meta">{{ post.date }} • By {{ post.author }}</div><p class="post-excerpt">{{ post.excerpt }}</p><a href="/post/{{ post.slug }}" class="read-more">Read More →</a></div>{% endfor %}</div><div class="ad-container"><div class="ad-label">Advertisement</div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926" crossorigin="anonymous"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5573963043624926" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>{% elif legal_type %}<a href="/" class="back-button">← Back to Home</a><div class="post-full"><div class="post-header">{% if legal_type == 'privacy' %}<h1>Privacy Policy</h1><div class="post-meta"><span>Last updated: 2026-03-24</span></div>{% elif legal_type == 'terms' %}<h1>Terms of Service</h1><div class="post-meta"><span>Last updated: 2026-03-24</span></div>{% elif legal_type == 'about' %}<h1>About Us</h1>{% endif %}</div><div class="post-content">{% if legal_type == 'privacy' %}<h2>Introduction</h2><p>TechBlog operates this website and respects your privacy. This policy explains how we collect and use information.</p><h2>Information Collection</h2><ul><li><strong>Usage Data:</strong> Browser type, pages visited, time spent</li><li><strong>Cookies:</strong> Track preferences and activity</li><li><strong>Google Analytics:</strong> Understand user interaction</li><li><strong>Google AdSense:</strong> Personalized ads</li></ul><h2>Use of Data</h2><ul><li>Provide and maintain our Service</li><li>Improve our Service</li><li>Detect and address issues</li></ul><h2>Security</h2><p>We protect your data with commercially acceptable means, but no method is 100% secure.</p><h2>Changes</h2><p>We may update this policy. Changes will be posted here.</p><h2>Contact</h2><p>Questions? Email: botsile55@gmail.com</p>{% elif legal_type == 'terms' %}<h2>1. Terms</h2><p>By using TechBlog, you agree to these terms. If you disagree, do not use this service.</p><h2>2. Use License</h2><p>Personal, non-commercial use only. You may not modify, copy, or use materials commercially.</p><h2>3. Disclaimer</h2><p>Materials are provided "as is". We make no warranties, expressed or implied.</p><h2>4. Limitations</h2><p>We are not liable for damages from use or inability to use materials.</p><h2>5. Accuracy</h2><p>Materials may contain errors. We do not warrant accuracy or completeness.</p><h2>6. Links</h2><p>We are not responsible for linked sites.</p><h2>7. Modifications</h2><p>These terms may be revised anytime. Continued use means acceptance.</p><h2>Contact</h2><p>Questions? Email: botsile55@gmail.com</p>{% elif legal_type == 'about' %}<h2>Welcome to TechBlog</h2><p>We provide high-quality web development tutorials for all skill levels.</p><h2>Our Mission</h2><p>Empower developers with clear, practical knowledge about modern web technologies.</p><h2>What We Cover</h2><ul><li><strong>HTML:</strong> Semantic markup and HTML5</li><li><strong>CSS:</strong> Layouts, animations, responsive design</li><li><strong>JavaScript:</strong> DOM, async programming, best practices</li><li><strong>Web Dev:</strong> Performance, accessibility</li></ul><h2>Our Values</h2><ul><li><strong>Quality:</strong> Well-researched content</li><li><strong>Clarity:</strong> Easy to understand</li><li><strong>Practicality:</strong> Real code examples</li><li><strong>Accessibility:</strong> Tech for everyone</li></ul><h2>Contact Us</h2><p>Email: botsile55@gmail.com | We'd love to hear from you!</p>{% endif %}</div></div>{% else %}<a href="/" class="back-button">← Back to Posts</a><div class="post-full"><div class="post-header"><span class="post-category">{{ current_post.category }}</span><h1>{{ current_post.title }}</h1><div class="post-meta"><span>{{ current_post.date }}</span><span>By {{ current_post.author }}</span></div></div><div class="ad-container"><div class="ad-label">Advertisement</div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926" crossorigin="anonymous"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5573963043624926" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div><div class="post-content">{{ current_post.content|safe }}</div><div class="ad-container"><div class="ad-label">Advertisement</div><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5573963043624926" crossorigin="anonymous"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5573963043624926" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div></div>{% endif %}</main><footer><div class="footer-content"><p>&copy; 2026 TechBlog. All rights reserved.</p><p>Quality web development tutorials for developers everywhere.</p><div class="footer-links"><a href="/privacy-policy" style="color:var(--accent);text-decoration:none;">Privacy Policy</a><a href="/terms-of-service" style="color:var(--accent);text-decoration:none;">Terms of Service</a><a href="/about" style="color:var(--accent);text-decoration:none;">About Us</a></div></div></footer></body></html>'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, current_page='home', posts=POSTS, legal_type=None)

@app.route('/post/<slug>')
def post(slug):
    post = next((p for p in POSTS if p['slug'] == slug), None)
    if not post:
        return "Post not found", 404
    return render_template_string(HTML_TEMPLATE, current_page='post', current_post=post, legal_type=None)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template_string(HTML_TEMPLATE, current_page='legal', legal_type='privacy', posts=POSTS)

@app.route('/terms-of-service')
def terms_of_service():
    return render_template_string(HTML_TEMPLATE, current_page='legal', legal_type='terms', posts=POSTS)

@app.route('/about')
def about():
    return render_template_string(HTML_TEMPLATE, current_page='legal', legal_type='about', posts=POSTS)

@app.route('/robots.txt')
def robots():
    return '''User-agent: *
Allow: /
Disallow: /admin

Sitemap: https://techub-l5vk.onrender.com/sitemap.xml
''', 200, {'Content-Type': 'text/plain'}

@app.route('/sitemap.xml')
def sitemap():
    sitemap_urls = [
        ('https://techub-l5vk.onrender.com/', '2026-03-24', 'weekly', '1.0'),
    ]
    for post in POSTS:
        sitemap_urls.append((f'https://techub-l5vk.onrender.com/post/{post["slug"]}', post['date'], 'monthly', '0.8'))
    
    sitemap_urls.extend([
        ('https://techub-l5vk.onrender.com/privacy-policy', '2026-03-24', 'yearly', '0.5'),
        ('https://techub-l5vk.onrender.com/terms-of-service', '2026-03-24', 'yearly', '0.5'),
        ('https://techub-l5vk.onrender.com/about', '2026-03-24', 'monthly', '0.6'),
    ])
    
    xml = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for url, date, freq, priority in sitemap_urls:
        xml += f'<url><loc>{url}</loc><lastmod>{date}</lastmod><changefreq>{freq}</changefreq><priority>{priority}</priority></url>'
    xml += '</urlset>'
    
    return xml, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
