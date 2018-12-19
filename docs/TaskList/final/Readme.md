### Readme

Example test

Run the python script 
```py 
python markdownAdmontionsToTex.py
pandoc --from markdown --to latex *.md config.yaml --filter pandoc-latex-admonition -s -o coolTex.tex
```

~~~admonition
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
In ac urna condimentum, posuere nibh sit amet, blandit
nisi. Vivamus nec elementum odio. Mauris non faucibus
nulla, eget tincidunt nisl. Cras dolor augue,
condimentum in quam at, tincidunt aliquet lorem. Donec
dolor augue, rhoncus ac mauris eget, tincidunt
facilisis quam. Quisque iaculis, nibh malesuada molestie
suscipit, ligula mauris lacinia nibh, eget mollis tellus
ante ut sapien. Mauris tristique tellus vitae vestibulum
eleifend. Aliquam metus nisl, hendrerit eu pellentesque
sed, bibendum ut diam. Aliquam mollis iaculis ipsum.
Nulla blandit urna suscipit eros ullamcorper rhoncus.
~~~