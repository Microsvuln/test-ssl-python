import re

def filterScriptTags(content): 
    return re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)

if __name__ == "__main__":
    sample_html = """
        <html>
            <body>
                <h1>Welcome</h1>
                <script>alert('This is an attack');</script>
                <p>This is a paragraph.</p>
                <script>console.log('Another script');</script>
            </body>
        </html>
    """
    
    filtered_html = filterScriptTags(sample_html)
    print("Filtered HTML:")
    print(filtered_html)
