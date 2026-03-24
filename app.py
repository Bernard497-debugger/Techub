from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Sample blog posts data
POSTS = [
    {
        'id': 1,
        'title': 'HTML5 Semantic Elements Complete Guide',
        'slug': 'html5-semantic-elements',
        'author': 'Tech Writer',
        'date': '2026-03-24',
        'category': 'HTML',
        'excerpt': 'Master HTML5 semantic elements for better structure, SEO, and accessibility in your web projects.',
        'content': '''
        <h2>Understanding HTML5 Semantic Elements</h2>
        <p>HTML5 introduced semantic elements that clearly describe their meaning to both the browser and developer. They improve SEO, accessibility, and code readability.</p>
        
        <h3>Common Semantic Elements</h3>
        <ul>
            <li><code>&lt;header&gt;</code> - Introductory content or navigation</li>
            <li><code>&lt;nav&gt;</code> - Navigation links</li>
            <li><code>&lt;main&gt;</code> - Main content of the page</li>
            <li><code>&lt;article&gt;</code> - Self-contained content</li>
            <li><code>&lt;section&gt;</code> - Thematic grouping of content</li>
            <li><code>&lt;aside&gt;</code> - Sidebar or related content</li>
            <li><code>&lt;footer&gt;</code> - Footer information</li>
        </ul>
        
        <h3>Semantic Document Structure</h3>
        <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Page Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;nav&gt;Navigation links&lt;/nav&gt;
    &lt;/header&gt;
    &lt;main&gt;
        &lt;article&gt;
            &lt;h1&gt;Article Title&lt;/h1&gt;
            &lt;p&gt;Content...&lt;/p&gt;
        &lt;/article&gt;
    &lt;/main&gt;
    &lt;footer&gt;Footer content&lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        
        <h3>Benefits of Semantic HTML</h3>
        <ul>
            <li><strong>SEO:</strong> Search engines better understand your content</li>
            <li><strong>Accessibility:</strong> Screen readers can navigate better</li>
            <li><strong>Readability:</strong> Cleaner, more maintainable code</li>
            <li><strong>Mobile:</strong> Better rendering on mobile devices</li>
        </ul>
        '''
    },
    {
        'id': 2,
        'title': 'Flexbox vs Grid: When to Use Each',
        'slug': 'flexbox-vs-grid',
        'author': 'Tech Writer',
        'date': '2026-03-22',
        'category': 'CSS',
        'excerpt': 'Learn the differences between Flexbox and CSS Grid, and when to use each one for optimal layouts.',
        'content': '''
        <h2>Flexbox vs CSS Grid</h2>
        <p>Both Flexbox and Grid are powerful layout tools, but they serve different purposes. Understanding when to use each is crucial for modern web design.</p>
        
        <h3>Flexbox Basics</h3>
        <p>Flexbox is designed for one-dimensional layouts (rows or columns).</p>
        <pre><code>.flex-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}</code></pre>
        
        <h3>Grid Basics</h3>
        <p>Grid is designed for two-dimensional layouts (rows AND columns).</p>
        <pre><code>.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1rem;
}</code></pre>
        
        <h3>Use Flexbox When:</h3>
        <ul>
            <li>Building navigation bars</li>
            <li>Creating button groups</li>
            <li>Aligning items in a single row or column</li>
            <li>Need flexible spacing and alignment</li>
        </ul>
        
        <h3>Use Grid When:</h3>
        <ul>
            <li>Building page layouts</li>
            <li>Creating image galleries</li>
            <li>Need both rows AND columns control</li>
            <li>Building complex, multi-section layouts</li>
        </ul>
        '''
    },
    {
        'id': 3,
        'title': 'JavaScript DOM Manipulation Essentials',
        'slug': 'javascript-dom-manipulation',
        'author': 'Tech Writer',
        'date': '2026-03-21',
        'category': 'JavaScript',
        'excerpt': 'Master DOM manipulation in JavaScript to dynamically modify HTML and create interactive web experiences.',
        'content': '''
        <h2>DOM Manipulation in JavaScript</h2>
        <p>The Document Object Model (DOM) allows you to interact with HTML elements dynamically. This is core to building interactive web applications.</p>
        
        <h3>Selecting Elements</h3>
        <pre><code>// Select by ID
const element = document.getElementById('myId');

// Select by class
const elements = document.getElementsByClassName('myClass');

// Modern way: querySelector
const element = document.querySelector('.myClass');
const elements = document.querySelectorAll('.item');</code></pre>
        
        <h3>Modifying Elements</h3>
        <pre><code>// Change text content
element.textContent = 'New text';

// Change HTML
element.innerHTML = '&lt;strong&gt;Bold text&lt;/strong&gt;';

// Add/remove classes
element.classList.add('active');
element.classList.remove('hidden');

// Change styles
element.style.color = 'red';
element.style.fontSize = '20px';</code></pre>
        
        <h3>Creating Elements</h3>
        <pre><code>const newDiv = document.createElement('div');
newDiv.textContent = 'Hello World';
newDiv.classList.add('my-class');

// Append to parent
document.body.appendChild(newDiv);</code></pre>
        
        <h3>Event Listeners</h3>
        <pre><code>const button = document.querySelector('button');

button.addEventListener('click', function() {
    console.log('Button clicked!');
});

// Remove event listener
button.removeEventListener('click', handler);</code></pre>
        '''
    },
    {
        'id': 4,
        'title': 'CSS Responsive Design: Mobile First Approach',
        'slug': 'css-responsive-design',
        'author': 'Tech Writer',
        'date': '2026-03-19',
        'category': 'CSS',
        'excerpt': 'Build responsive websites using the mobile-first approach and media queries for all screen sizes.',
        'content': '''
        <h2>Responsive Design with Mobile First</h2>
        <p>Mobile-first design means building for mobile devices first, then enhancing for larger screens. This improves performance and ensures a great mobile experience.</p>
        
        <h3>Viewport Meta Tag</h3>
        <p>Always include the viewport meta tag in your HTML head:</p>
        <pre><code>&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;</code></pre>
        
        <h3>Mobile-First Media Queries</h3>
        <pre><code>/* Mobile styles (default) */
.container {
    font-size: 14px;
    padding: 10px;
}

/* Tablet and up */
@media (min-width: 768px) {
    .container {
        font-size: 16px;
        padding: 20px;
    }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .container {
        font-size: 18px;
        padding: 30px;
    }
}</code></pre>
        
        <h3>Responsive Images</h3>
        <pre><code>img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* Use srcset for different screen sizes */
&lt;img srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
     sizes="(max-width: 600px) 400px, 800px"
     src="medium.jpg" alt="Responsive image"&gt;</code></pre>
        '''
    },
    {
        'id': 5,
        'title': 'JavaScript Promises and Error Handling',
        'slug': 'javascript-promises',
        'author': 'Tech Writer',
        'date': '2026-03-17',
        'category': 'JavaScript',
        'excerpt': 'Understand JavaScript Promises for handling asynchronous operations and proper error handling.',
        'content': '''
        <h2>Mastering JavaScript Promises</h2>
        <p>Promises represent the eventual completion of an asynchronous operation and its resulting value. They're fundamental to modern JavaScript.</p>
        
        <h3>Promise States</h3>
        <ul>
            <li><strong>Pending:</strong> Initial state, operation hasn't completed yet</li>
            <li><strong>Fulfilled:</strong> Operation completed successfully</li>
            <li><strong>Rejected:</strong> Operation failed</li>
        </ul>
        
        <h3>Creating a Promise</h3>
        <pre><code>const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Success!');
        // or reject(new Error('Failed!'));
    }, 1000);
});

// Consume the promise
myPromise
    .then(result => console.log(result))
    .catch(error => console.error(error))
    .finally(() => console.log('Done'));</code></pre>
        
        <h3>Promise Chaining</h3>
        <pre><code>fetch('/api/users')
    .then(response => response.json())
    .then(data => {
        console.log('Users:', data);
        return data[0].id;
    })
    .then(userId => fetch(`/api/users/${userId}`))
    .then(response => response.json())
    .then(user => console.log('User details:', user))
    .catch(error => console.error('Error:', error));</code></pre>
        
        <h3>Promise.all() and Promise.race()</h3>
        <pre><code>// Wait for all promises
Promise.all([promise1, promise2, promise3])
    .then(results => console.log(results));

// Race: return first settled promise
Promise.race([promise1, promise2])
    .then(winner => console.log(winner));</code></pre>
        '''
    },
    {
        'id': 6,
        'title': 'CSS Animations and Transitions Guide',
        'slug': 'css-animations',
        'author': 'Tech Writer',
        'date': '2026-03-16',
        'category': 'CSS',
        'excerpt': 'Create smooth animations and transitions with CSS to enhance user experience and interactivity.',
        'content': '''
        <h2>CSS Animations and Transitions</h2>
        <p>Animations and transitions add polish to your web design. CSS provides powerful tools to create smooth, performant animations.</p>
        
        <h3>CSS Transitions</h3>
        <p>Transitions smoothly change property values over time.</p>
        <pre><code>.button {
    background-color: blue;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: darkblue;
}</code></pre>
        
        <h3>Transition Properties</h3>
        <pre><code>/* Shorthand */
transition: property duration timing-function delay;

/* Example */
transition: all 0.5s ease-in-out 0.1s;</code></pre>
        
        <h3>CSS Keyframe Animations</h3>
        <pre><code>@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

.element {
    animation: slideIn 1s ease-out forwards;
}</code></pre>
        
        <h3>Animation Properties</h3>
        <ul>
            <li><code>animation-name</code> - Name of the keyframes</li>
            <li><code>animation-duration</code> - How long the animation takes</li>
            <li><code>animation-timing-function</code> - Speed curve (ease, linear, etc.)</li>
            <li><code>animation-delay</code> - Wait before starting</li>
            <li><code>animation-iteration-count</code> - How many times to repeat</li>
            <li><code>animation-direction</code> - Forward, reverse, or alternate</li>
        </ul>
        '''
    },
    {
        'id': 7,
        'title': 'Form Validation in HTML and JavaScript',
        'slug': 'form-validation',
        'author': 'Tech Writer',
        'date': '2026-03-14',
        'category': 'HTML',
        'excerpt': 'Learn to validate HTML forms both on the client-side with HTML5 and JavaScript for better user experience.',
        'content': '''
        <h2>Form Validation Techniques</h2>
        <p>Proper form validation ensures data quality and improves user experience. Use both HTML5 validation and JavaScript for robust forms.</p>
        
        <h3>HTML5 Validation</h3>
        <pre><code>&lt;form&gt;
    &lt;input type="email" required&gt;
    &lt;input type="password" minlength="8" required&gt;
    &lt;input type="number" min="1" max="100"&gt;
    &lt;input type="url" required&gt;
    &lt;textarea minlength="10" maxlength="500"&gt;&lt;/textarea&gt;
    &lt;button type="submit"&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        
        <h3>JavaScript Form Validation</h3>
        <pre><code>const form = document.querySelector('form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = form.querySelector('input[type="email"]').value;
    const password = form.querySelector('input[type="password"]').value;
    
    if (!email.includes('@')) {
        alert('Invalid email address');
        return;
    }
    
    if (password.length < 8) {
        alert('Password must be at least 8 characters');
        return;
    }
    
    // Form is valid, submit
    form.submit();
});</code></pre>
        
        <h3>Custom Error Messages</h3>
        <pre><code>const input = document.querySelector('input[type="email"]');

input.addEventListener('invalid', function(e) {
    e.preventDefault();
    input.setCustomValidity('Please enter a valid email address');
});

input.addEventListener('input', function() {
    if (this.validity.valid) {
        this.setCustomValidity('');
    }
});</code></pre>
        '''
    },
    {
        'id': 8,
        'title': 'Web Performance Optimization Best Practices',
        'slug': 'web-performance-optimization',
        'author': 'Tech Writer',
        'date': '2026-03-13',
        'category': 'Web Dev',
        'excerpt': 'Optimize your websites for speed and performance using proven techniques and best practices.',
        'content': '''
        <h2>Web Performance Optimization</h2>
        <p>Website speed is critical for user experience and SEO. Here are proven techniques to optimize your web applications.</p>
        
        <h3>Image Optimization</h3>
        <pre><code>/* Use modern image formats */
&lt;picture&gt;
    &lt;source srcset="image.webp" type="image/webp"&gt;
    &lt;source srcset="image.jpg" type="image/jpeg"&gt;
    &lt;img src="image.jpg" alt="Description"&gt;
&lt;/picture&gt;

/* Lazy loading */
&lt;img src="image.jpg" loading="lazy" alt="Description"&gt;</code></pre>
        
        <h3>CSS Optimization</h3>
        <ul>
            <li>Minify CSS files</li>
            <li>Remove unused CSS with PurgeCSS or Tailwind</li>
            <li>Defer non-critical CSS</li>
            <li>Use CSS variables for reusability</li>
            <li>Avoid inline styles</li>
        </ul>
        
        <h3>JavaScript Optimization</h3>
        <pre><code>/* Defer non-critical scripts */
&lt;script defer src="analytics.js"&gt;&lt;/script&gt;

/* Lazy load heavy libraries */
if ('IntersectionObserver' in window) {
    // Use Intersection Observer to load components on demand
}</code></pre>
        
        <h3>Caching Strategies</h3>
        <ul>
            <li><strong>Browser Caching:</strong> Set proper cache headers</li>
            <li><strong>CDN:</strong> Use a Content Delivery Network</li>
            <li><strong>Service Workers:</strong> Cache assets for offline support</li>
            <li><strong>HTTP/2:</strong> Multiplexing for faster requests</li>
        </ul>
        
        <h3>Performance Metrics</h3>
        <ul>
            <li><strong>FCP:</strong> First Contentful Paint</li>
            <li><strong>LCP:</strong> Largest Contentful Paint</li>
            <li><strong>CLS:</strong> Cumulative Layout Shift</li>
            <li><strong>FID:</strong> First Input Delay</li>
        </ul>
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
