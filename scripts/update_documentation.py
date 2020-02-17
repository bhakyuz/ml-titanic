import pweave
# Weave a pandoc document with default options
pweave.weave('scripts/documentation.pmd', output = 'documentation.html')