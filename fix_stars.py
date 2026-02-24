import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to find:
# <div class="border-gradient-bottom"[^>]*></div>
# \s*<div class="border-gradient-top"[^>]*></div>
# And replace with:
# <div class="border-glow-wrapper">
# \g<0>
# </div>

pattern = re.compile(
    r'(<div class="border-gradient-bottom"[^>]*></div>\s*<div class="border-gradient-top"[^>]*></div>)',
    re.MULTILINE | re.DOTALL
)

new_content = pattern.sub(r'<div class="border-glow-wrapper">\n\1\n</div>', content)

# Add the CSS right before </style>
css = """
    .border-glow-wrapper {
      position: absolute;
      inset: 0;
      border-radius: inherit;
      padding: 1px;
      pointer-events: none;
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      z-index: 0;
    }
"""
new_content = new_content.replace('</style>', css + '</style>')

with open('index.html', 'w') as f:
    f.write(new_content)

print("Fixed!")
