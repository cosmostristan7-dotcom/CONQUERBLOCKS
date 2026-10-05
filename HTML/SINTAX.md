# CLASS 0
```html
<body>
    <div>
        <p>INTRODUCTION TO HTML</p>

        <p>Rule: A webpage can only have ONE `<body>` tag. Just like a human body, a webpage has one body, not two.</p>

        <p>Why only one `<body>`?<br>
        Because the `<body>` represents all visible content of the page.<br>
        Everything the user sees must be inside that single `<body>`.<br>
        If you need more space, more sections, more content, more layout…<br>
        👉 You use more `<div>`, `<section>`, `<article>`, `<header>`, etc. /// NOT another `<body>`.</p>

        <p>Example:</p>
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>My Page</title>
        </head>
        <body>
            <div>
                <!-- Your visible content goes here -->
            </div>
        </body>
        </html>
        ```
    </div>

    <!-- -- --- ------------------------------------------ -- -->

    <article>
        <h2>HTML is responsible to build up all the web elements.</h2>
        <h2>It is the base for any web or webapp.</h2>
        <h2>It works with plain text only.</h2>
        <h2>It can be edited with any text editor.</h2>
        
        <!-- NEW CONCEPTS -->

        <h1>STATIC PAGES</h1>

        <p>It has not a database.</p>
        <p>It only has HTML, CSS, and JS text files.</p>
        <p>It can be updated only by 1 developer.</p>
        <p>There is no registration or login option.</p>
        <p>It will show the same display for all the users.</p>

        <pre>
    _______               ______
  |  ***  |              | ### |
  | *** |............>>  |  ## |
  |  ***  |              | ### |
  ---------             ---------
  THE SERVER         CLIENT / BROWSER
        </pre>

        <strong>DYNAMIC PAGES</strong>

        <p>It has a database engine.</p>
        <p>It has a programming language coming from the server.</p>
        <p>It has logic related to the contents.</p>
        <p>It will have a registration and login session.</p>
        <p>It also has programming languages as in the static pages.</p>
        <p>It will have unique content per user.</p>

        <pre>
   _______                                    ______
  |  ***  | <  >   [##***]                    | ### |
  | *** |         [*#*#*]   <<.........>>     |  ## |
  |  ***  |        [**#**]                    | ### |
  ---------        --------                 ---------
  THE SERVER     DATABASE SERVER         CLIENT / BROWSER 
        </pre>
<!-- ---------------------------------------------- ------- -->
       
       <p>BACKEND: 
        Works with THE SERVER & DATABASE SERVER, 
        also it will work on the response with the user, and 
        on the communication with the DATABASE.</p>

        <p>FRONTEND: 
        It will work with the style and design (the user supported by the A.I. will work on this part).</p>

        <h1 style="color: RED; text-align: center;">FRONTEND</h1>

        <p>It keeps all the elements that work in the visual part of a webpage.</p> 
        <p>There are only 3 main technologies (HTML, CSS, JS).</p>
        <p>Based on what device is used, it will adapt what must be shown.</p>
        <p>It will send information to the BACKEND.</p>

        <!-- JAVASCRIPT -->
        <h1 style="color: RED; text-align: center;">JAVASCRIPT</h1>

        <p>It is the only programming language that understands the web.</p>
        <p>It is a full programming language able to communicate with the DOM (...).</p>
        <p>It evolves fast due to its useful demand.</p>
        <p>All navigators know how to work with it.</p>

        <strong>Not only HTML, CSS and JAVASCRIPT live in the FRONTEND</strong>
        <p>There are also: BABEL / HTML(5) / CSS (3...) / JS / Bootstrap / GitHub / Webpack / React / Git / Angular</p>
    </article>

    <!--FRONTEND: CSS FRAMEWORKS AND PREPROCESSORS -->
    <section>
        <h2>FRONTEND</h2>
        <p>must also know how to work with the different</p> 

        <h5>CSS frameworks:</h5>
        <p>Pure / MDB / Bulma / etc.</p>

        <h5>Preprocessors for CSS:</h5>
        <p>SASS / LESS / SCSS</p>

        <!-- JAVASCRIPT FRAMEWORKS -->
        <h1>Frameworks JS:</h1>
        <p>Meteor JS / Ember JS / React JS / Polymer JS / Angular JS / etc.</p>

        <p>COMING BACK TO HTML:</p>

        <strong><span style="color: red;">LINKS - ENLACES</span></strong>
    </section>

    <!-- CLASS 05 -->
    <div>
        <h1>`<hx>` TAGS</h1>
        <p>Function: They are used to highlight a title, word, phrase, or a whole paragraph. They are the [h1 - h6] tags. They have closing tags. They are known as Block Tags.</p> 

        <p>They can divide our content into chapters (if that's what we need to do). Either by using the <h1> - <h6> tags or using the <hr color="red" width="50%"> lines format.</p>

        <em>"hr" TAGS</em>
        <h1 style="color: red;">Function:</h1> 
        <p>Make lines appear below or above a title, phrase, or even a paragraph. They have no closing tag. Example:</p>

        ```html 
        <!DOCTYPE html>
        <html>
            <head>
                <title>Horizontal LINE rule</title>
            </head>
            <body>
                Hello World
                <hr color="green" width="50%">
                <hr color="navy" width="70%">
            </body>
        </html> 
        ```

        <blockquote>It shows a short paragraph and includes a link from where the paragraph has been taken.</blockquote>

        <code>It is an inline tag. It gives a different emphasis to a word or set of words within a paragraph.</code>

        <p><a>...</a><br>
        This tag links internal/external documents from other webs to ours; besides that, it allows us to connect information within the same document so they can work in our web.</p>

        <em>It has basic and event attributes:</em>

        <em>And it also has Specific Attributes:</em>
        
        <h1 style="color: green;">href</h1>
        <p>The value for this attribute will be a URL or a segment of it.</p>

        <h1 style="color: gray;">download</h1>
        <p>It can be an empty tag or it can keep the file name used to download the file.</p>

        <h1 style="color: black;">hreflang</h1>
        <p>Sets the language in which the webpage will appear.</p>
    </div>

    <article>
        <em style="color: purple;">RELATIVE ROUTES</em>
        <p>It departs from the very directory where you are.<br>
        Examples:<br>
        • images/photo.jpg<br>
        • ../assets/styles.css<br>
        • ./script.js<br>
        Relative routes change depending on where your file is located.</p>

        <hr color="marble" width="80%">

        <em style="color: red;">ABSOLUTE ROUTES</em>
        <p>It has its path from the root of the system (or full URL).<br>
        Examples:<br>
        • In a website: https://example.com/images/photo.jpg<br>
        • In a computer: C:/Users/David/Documents/project/index.html<br>
        It always starts from the root, so it works no matter where your current file is located.</p>
    </article>

    <!-- CLASS 06 HTML: Semantic Tags -->
    <div>
        <h1 style="color: red;">SEMANTIC TAGS</h1>
        <p>With or without them our HTML information can look just equal. However, if we use them, our HTML code will be more specific and detailed. They always have to be included within the `<body></body>` tags.</p>

        <h1>They can be:</h1>
        <p>
            1. GROUPING TAGS.<br>
            2. BLOCK-LEVEL GROUPING TAGS.<br>
            3. CONTAINER TAGS.<br>
            4. STRUCTURAL GROUPING TAGS.
        </p>
    </div>

    <h1>1. GROUPING TAGS</h1>
    <p>Grouping tags are HTML elements whose main purpose is to organize content. They don’t necessarily describe meaning; they simply help you group related items together so your page is easier to structure and style.</p>
    <p>
        Examples:<br>
        • &lt;div&gt; — generic grouping<br>
        • &lt;span&gt; — inline grouping<br>
        • &lt;p&gt; — paragraph grouping<br>
        • &lt;ul&gt; / &lt;ol&gt; — list grouping<br>
        • &lt;li&gt; — list item grouping
    </p>
    <p>Use grouping tags whenever you need to collect elements into a single unit.</p>

    <h1>2. BLOCK-LEVEL GROUPING TAGS (&lt;div&gt; - &lt;section&gt; - &lt;article&gt; - and so on)</h1>
    <p>Block‑level grouping tags create large structural blocks in your layout. They always start on a new line and expand to the full width available.</p>
    <div>
        <article>
            `<div>`<br>
            <p>A generic block container with no semantic meaning. Use it for layout, wrappers, and when no other tag fits.</p><br><br>
            `<section>`<br>
            <p>A thematic block of content. Use it when your content has a topic, heading, or theme.</p><br><br>
            `<article>`<br>
            <p>A self‑contained block that can stand alone outside the page. Use it for blog posts, news, product descriptions, etc.</p><br><br>
            `<nav>`<br>
            <p>A block containing major navigation links.</p><br><br>
            `<header>` / `<footer>`<br>
            <p>Introductory and closing blocks for a page or section.</p><br><br>
            <p>Block‑level grouping tags help you build the structure of your webpage.</p>
<!-- ------------------------------------------------------ -->
            `<span>`
                <p>Stands for a generic inline container used in HTML to group text or elements for styling or scripting purposes.</p>
                <p>Display Behavior: `<span>` is an inline element, meaning it flows naturally within a line of text without forcing line breaks. Both `<section>` and `<article>` are block-level elements that break to a new line and take up the full available width of their container.</p>
```html
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Span Example</title>
    <style>
        .highlight {
            color: darkgreen;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <p>Welcome back, <span class="highlight">Developer</span>! Your workspace is ready.</p>
</body>
</html>
<!-- ----------------------------------------------------- --->

        </article>
    </div>

    <h1>3. CONTAINER TAGS</h1>
    <p>Container tags are elements whose main job is to hold other elements inside them. They may be semantic or non‑semantic.</p>
    <p>
        Examples:<br>
        • `<div>` — generic container<br>
        • `<section>` — thematic container<br>
        • `<article>` — content container<br>
        • `<form>` — container for inputs<br>
        • `<table>` — container for tabular data<br>
        A container tag is used when you need a box to place multiple elements inside and treat them as one unit.
    </p>

    <em>Examples per each tag:</em>

    <h1>4. STRUCTURAL GROUPING TAGS</h1>
    <p>Structural grouping tags define the architecture of your webpage. They give meaning to the layout so browsers, search engines, and screen readers understand the structure.</p>
    <p>
        Examples:<br>
        • `<header>` — top section<br>
        • `<footer>` — bottom section<br>
        • `<nav>` — navigation<br>
        • `<main>` — main content<br>
        • `<aside>` — complementary content<br>
        • `<section>` — thematic block<br>
        • `<article>` — independent content<br>
        These tags make your HTML semantic, accessible, and easier to maintain.
    </p>

    <h2 style="color: red;">Structural Grouping Tags, continue...</h2> 
    <p>&lt;div&gt; is a block‑level container.<br>
    Its job is to group elements together so you can treat them as one unit.<br>
    Think of it like a box you put things inside.<br>
    You can put inside a <code>&lt;div&gt;</code>:<br>
    • text<br>
    • images<br>
    • paragraphs<br>
    • headings<br>
    • other divs<br>
    • entire sections of layout<br>
    It doesn’t add meaning by itself — it’s non‑semantic.<br>
    It’s mainly used for layout, structure, and styling with CSS.</p>
    <em style="color: blue;">Example:</em>

    <article>
        `<article>` represents a self‑contained piece of content that can stand on its own, independent from the rest of the page.<br>
        It’s used for things like <code style="color: blue;">blog posts, news stories, tutorials, forum entries, or any section that could be reused or distributed by itself.</code>
    </article>
<!-- ------------------------------------------------------ -->

<div>
    <aside>
        <em>&lt;nav&gt; TAG:</em>
    
        <p>It is an HTML semantic element used to define a major section of navigation links on a webpage.</p>

        <p>Primary Purpose: It tells browsers, search engines, and screen readers that the links inside it are the core navigation menu (such as home, about, services, or contact links) rather than just random links scattered across the page.</p>

        <h1>Example:</h1>
        <nav>
            <a href="/MYSQL/NOTEbook/server.py">PYTHON</a>
            <a href="/MOVIE_site/index.html">MOVIES</a>
            <a href="/ADAMANTIO/WEBpages/index.html">HISTORY</a>
        </nav>
    </aside><br>

<!-- ---------------------------------- ------------------- -->
     <p>&lt;header&gt;PSUDIUM LOREN ETEREIUM&lt;/header&gt;</p>
    <br>
     <p>It keeps the information on top in our webpage. Moreover, it is possible to fing this `<header>` tag within an article or block tag. For example at the beginning of an post block. </p>
    <br>
    <p>Do not miss this tag with `<head>...</head>` tag (This one isn't a content tag). Since they are two different things.
    </p><br>

    <article>
        <header>
            <h1>This is an HEADER example</h1>
            <p>Written by David Trinidad</p>
        </header>
        <p>LORIUM POSIUM ITERIUM</p>
    </article>
    <!-- ------------------------------------------------ -->

    <div>
        <section> 
     <h2>`<footer>...</footer>`</h2>
     <p>This HTML tag defines a footer for a document or a section. It typically contains information about the author, copyright data, links to terms of use, contact information, or related documents.</p>

     <p>Context: Usually placed at the bottom of a webpage (<body>) or at the end of a specific section/article (<article>, <section>).</p>

     <p>Note: A <footer> does not automatically mean "at the very bottom of the browser window"—it simply represents the footer of the nearest sectioning content or root element.</p>
     <p>Example:</p>
        <footer>
            <p>Author: David Lorem.</p>
            <p><a href:"https://cndstore.onrender.com"></a></p>
        </footer>
        </section>
    </div>
<!-- ------------------------------------------------------- -->

    <div>
        <article>
            <header>
                <h2>`<section>`...`</section>` TAGS.</h2>
                <p>Conquer Blocks, class06, my notes.</p>
            </header>

            <p>The HTML tag defines a standalone section of a document, typically containing a thematic grouping of content usually with a heading.</p>
            
            <p>Purpose: Used to break up a page into logical, thematic pieces (like chapters, tabbed content, or distinct subject areas) rather than purely stylistic wrappers (like <div>).</p>
        </article>
    </div>
<!-- ------------------------------------------------------- -->

    <div>
        <article>
            <header>
                <h2>`<main>`...`</main> TAG.</h2>
                <p>Conquer Block class06, my notes.</p>
            </header>

            <p>The `<main>` tag specifies the dominant, central content of a document's body, directly related to the central topic or application functionality. It acts as a structural landmark for screen readers and search engines, ensuring that repetitive elements like navigation menus, headers, footers, and sidebars are excluded from the primary narrative. Only one unique `<main>` element should exist per page, and it cannot be a descendant of an `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>` element.</p>

            <h2>Example:</h2>
```html
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example Page</title>
</head>
<body>
    <header>
        <nav>
            <a href="#home">Home</a> | <a href="#about">About</a>
        </nav>
    </header>

    <main>
        <h1>Welcome to My Website</h1>
        <p>This is the unique, central content of the webpage.</p>
    </main>

    <footer>
        <p>&copy; 2026 Example Corp</p>
    </footer>
</body>
</html>    
```html
<em>CONCLUSION</em>
    <p>A `<main>` tag enclosures the core of the information, it acts as an `<article>` tag.
        </article>
    </div>

<!-- ------------------------------------------------------- -->

    <div>
        <aside>
            <h2>
                <p>...</p>
        </aside>
    </div>
<!-- ------------------------------------------------------ -->
    <div>
        <article>
            <p>Always remember to place this within your `<head>` information, below `<meta charset="UTF-8">`,
            `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. By doing so, you your project will be able to be displayed on a any device without a problem.</p>
        </article>
    </div>
<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->

 <div>
    <section>
        <h1>IF YOU NEED TO CREATE A SEARCH BOX, include the following instruction:</h1>
        <form action="/search-results" method="get">
            <input type="search" name="q" placeholder="Search..." required>
            <button type="submit">Search</button>
        </form>
    </section>
</div>
<!-- ------------------------------------------------------- -->
<!-- ------------------------------------------------------- -->
<div class="article">
    <section>
        <header>
            <h1>CLASS 07.</h1>
            <h2>GROUPING TAGS</h2>
                <p>They add an extra bonus to the semantic tags. Yet, they cannot stand alone.</p>
            <h2>LINE TAGS</h2>
                <p>They are stored within a semantic tag such as <div class="article">, 
                    <p> lorem spiron lerna <span>trenium terem itsan lerum erum kerum</span>.Lorem remune eterm lerum leram.</p>
                </div>
                    <p>The `class=" - "` type stored at `<div>` tag can be: blog, article, section, news.
        </header>
    </section>
</div>
<!-- -------------------------------------------- -------- -- -->
 
 <div class="article">
    <h1 color="darkgreen">`<span>` tag</h1>
    <p>The `<span> ... `</span>` tag is a grouping tag, however, it doesn't contain information by itlsef. It works within a grouping tag, <span>like in this example.</span>Remember that it cannot act by its own.</p>
</div>
<!-- -------------------------------------------- -------- -- -->
<!-- -------------------------------------------- -------- -- -->
<h1>'<hr>'</h1>
<p>It is a line tag. It's an empty tag. It is used to to separates topics, it's similar to `<br>` tag.

<!-- -------------------------------------------- -------- -- -->
<!-- -------------------------------------------- -------- -- -->
<h1>LIST TAGS: ul // ol // dl.</h1>
<hr>
<div>
    <article>
    <p><strong>ul</strong></p>
    <p>`<ul>` ... `</ul>` it stands for un orden list. It means it contains a set of lines, words which do not require to be in alphabetical order or levels. This tag will have `vinetas`</p>
    <hr>
    <p>This `<ul>` ... `</ul> tag will have as many `<li>` ... `</li>` sub tags as containers (words or list of words) the actual list needs. Same thing will happen on `<ol>` ... `</ol>`.</p>
    </article>
</div>
<hr>
<div>
    <article>
        <p><strong>`<ol>` ... `</ol>` it stands for order list. As its name says this tag works for those set of words, phrases or lines which requires an order while listed. This tag will have numbers instead.</p>
        <h2>EXAMPLE:</h2>

        <div>
            <p>This is an example of how the `<ol>` ... `</ol>` tag will actually work. Even though we won't see the actual numbers which sets the order, they will be displayed on the web:</p>
            <ol>
                <li>First, save your money every paycheck.</li>
                <li>Second, set apart your tith and peace offerings.</li>
                <li>Third, Add some money to your physical savings.</li>
            </ol>
        </div>
    </article>
</div>
<hr>
<div>
    <article>
        <p><strong>`<dl>` ... `</dl>`, stands for detailed list.
</body>
```html