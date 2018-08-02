# Boostnote-notes-repo
A list of tasks and links, research completed in BoostNote

Can also write about how I tried out a lot of documentation formats, but boostnote + vuepress is a good combo.

Currently, math (katex), tasklists, chartjs and admonitions are implemented into this vuepress template.


## Why Vuepress and Boostnote-notes-repo

* They both use Markdown-it
* Plugins are similar
* Publishing a folder of boostnote notes is difficult

### How to use

Install the dependencies
```sh
pip -r requirements.txt
yarn install
```

Currently, if you have images in your boostnote notes, export the entire directory (images will be stored as attachments).

Then extract all the notes and run vuepress
```sh
python boostNote2Md.py
yarn docs:dev 
```
