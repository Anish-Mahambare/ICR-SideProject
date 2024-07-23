import requests
import subprocess

# URL of the webpage containing the JavaScript snippet
url = 'https://quizlet.com/279055066/bace-exam-review-flash-cards/?funnelUUID=6e5a1f6b-ed38-4144-bafe-3b192f5fc09f'

# JavaScript code to execute
js_code = '''
(() => {
  const terms = document.getElementsByClassName('SetPageTerms-term');
  const csv = [];

  Array.from(terms).forEach((term) => {
    const termTexts = term.querySelectorAll('.TermText');
    const word = termTexts[0].textContent.replace(/[\n\r]+/g, '/');
    const def = termTexts[1].textContent.replace(/[\n\r]+/g, '/');
    
    csv.push(`"${word}","${def}"`);
  });

  console.log(csv.join('\\n'));
})();
'''

# Create a temporary HTML file with the JavaScript code embedded
html_content = f'''
<!DOCTYPE html>
<html>
<head><title>Terms Scraper</title></head>
<body>
<script>{js_code}</script>
</body>
</html>
'''

# Save the HTML content to a temporary file
with open('temp.html', 'w') as f:
    f.write(html_content)

# Use curl to fetch the rendered HTML content and execute the JavaScript
curl_command = f"curl -s {url} -d @temp.html"
output = subprocess.check_output(curl_command, shell=True).decode('utf-8')

# Print the output (which contains the CSV data)
print(output)

# Clean up: remove the temporary HTML file
import os
os.remove('temp.html')
