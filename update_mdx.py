# Define the string you want to write
content = """---
title: Test
description: 'Test Doc'
---

# TESTING
"""

# Open a new MDX file and write the content to it
with open('test.mdx', 'w') as mdx_file:
    mdx_file.write(content)

print("Content written to example.mdx")