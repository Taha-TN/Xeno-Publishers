import glob

# Your Adsterra codes
social_bar = '<script src="https://pl31489763.profitableratecpmnetwork.com/cd/c6/7d/cdc67d75d32d232039e77759c82a81d5.js"></script>'

native_banner = '''
<div style="display:flex; justify-content:center; width: 100%; margin: 25px 0; z-index: 50;">
    <script async="async" data-cfasync="false" src="https://pl31489764.profitableratecpmnetwork.com/edbaa089425a7131a690555c571b5237/invoke.js"></script>
    <div id="container-edbaa089425a7131a690555c571b5237"></div>
</div>
'''

banner_300x250 = '''
<div style="display:flex; justify-content:center; width: 100%; margin: 25px 0; z-index: 50;">
    <script>
      atOptions = {
        'key' : '4a76cbc7130885a4435f32e7c1381c16',
        'format' : 'iframe',
        'height' : 250,
        'width' : 300,
        'params' : {}
      };
    </script>
    <script src="https://www.highrevenueformat.com/4a76cbc7130885a4435f32e7c1381c16/invoke.js"></script>
</div>
'''

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "cdc67d75d32d" not in content and "</body>" in content:
        content = content.replace("</body>", f"    {social_bar}\n</body>")
    
    if "4a76cbc7" not in content:
        if "</footer>" in content:
            content = content.replace("</footer>", f"{banner_300x250}\n</footer>")
        elif "</main>" in content:
            content = content.replace("</main>", f"{banner_300x250}\n</main>")
    
    if "edbaa089" not in content:
        if "</header>" in content:
            content = content.replace("</header>", f"</header>\n{native_banner}")
        elif "<body>" in content:
            content = content.replace("<body>", f"<body>\n{native_banner}")

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully injected Adsterra tags into {len(html_files)} HTML files!")
