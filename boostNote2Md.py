#!/usr/bin/env python3
# coding: utf-8
"""
Author       : grandfleet
Created Time : 2018-05-26 21:32:59
Prerequisite:
    python3 -m pip install cson arrow glob
Todo:
    Update script with logging package (!Not important)
    https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
"""
import json
import os
import sys
import datetime
import cson

# Replacing storage:\\ with proper file path
import glob
import re
import fileinput
import shutil

# Boostnote Notes constant file types
MARKDOWN_NOTE = "MARKDOWN_NOTE"
SNIPPET_NOTE = "SNIPPET_NOTE"
# Vuepress type props 
VUEPRESS_TYPES = ['tip','warn','error']
# Could have a set of boostnote tags that map to tip, warn and error, but for now don't worry about it.
try:
    import arrow
    time_aware = True
except ImportError:
    print(
        'warning: datetime information will be discarded unless you install arrow'
    )
    time_aware = False

def read_file(fp):
    with open(fp, 'r', errors='ignore') as f:
        return f.read()


def text_to_dict(text):
    """convert json or cson to dict"""
    try:
        return cson.loads(text)
    except:
        pass

    try:
        return json.loads(text)
    except:
        pass
    raise Exception("text should be in cson or json format")


def read_folder_names(fp):
    data = text_to_dict(read_file(fp))
    return {x['key']: x['name'] for x in data['folders']}


def write_boostnote_markdown(data, output, folder_map):
    """write boostnote dict to markdown"""
    target_dir = os.path.join(output, folder_map[data['folder']])
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    file_title = data['title']
    target_file = os.path.join(target_dir, '{}.md'.format(data['title'].replace('/', '-')))
    with open(target_file, 'w') as f:
        # If no data is present, skip the snippets
        boostnote_type = data['type']
        ## Write badges into the file 
        try:
            badges= data['tags']
            if badges == []:
                #print('Empty List, skipping badge printing')
                print('')
            else:
                if file_title != '':
                    print('Writing Title: ' + file_title)
                    f.write('## ' + file_title)
                    #print('ANIME OUT')
                                
                try:
                    # Add a star emoji
                    if data['isStarred']:
                        f.write('**Starred** :star: ')
                    # If in trash, shouldn't happen, but might.
                    if data['isTrashed']:
                        f.write('**Trashed** :skull_and_crossbones:')
                except: 
                    print('Unable to print emojis for: ' + target_file)
                # Adding boostnote tags as vuepress badges, a little to specific for my taste, but easy enough to comment out later.
                for badge in badges: 
                    vue_badge_string = " <Badge text=\"%s\" type=\"%s\" /> " % (badge, VUEPRESS_TYPES[1])
                    f.write(vue_badge_string)
                f.write('\n')
                ## Write the table of contents 
                # Potentially add factor for toc 
                f.write('[[toc]] \n')
        except:
            print('Writing title and/or badges failed')
        # print(boostnote_type)
        try:
            if data['type'] == MARKDOWN_NOTE:
                f.write(data['content'])
                print('Writing a boostnote markdown file at: ' + target_file)
            elif data['type'] == SNIPPET_NOTE:
                snippets = data['snippets']
                for snippet in snippets:
                #print()
                    title = snippet['name']
                    codeLanguage = snippet['mode']
                    content = snippet['content']
                    # Error conditions, fuck 
                    
                    if title == "":
                        title = "no name"
                    # Debug statements
                    print('title: ' + title + ' language: ' + codeLanguage)
                    #print(snippet['content'])
                    # Add heading 
                    if content == "":
                        print('unfortunately, the snippet has no content ')
                    else:
                        f.write('\n')
                        f.write('### ' + title + '\n\n')
                        # Add opening code block
                        f.write('```' + codeLanguage + '\n')
                        # Add Content 
                        f.write(content + '\n')
                        # Add closing block 
                        f.write('```' + '\n\n')
                        # Add horizontal rule 
                        f.write('<hr />' + '\n\n')
                        f.write('\n')
                #    print(snippet['content'])
                print('Writing boostnote snippets to file at: ' + target_file)
            else:
                print('unexpected data type: ' + data['type'])
        except:
            print('Error in writing boostnote file' + target_file)
    
    # Update date of file correctly.
    if time_aware:
        update_at = arrow.get(data['updatedAt'])
        update_at_epoch = int(update_at.timestamp)
        os.utime(target_file, (update_at_epoch, update_at_epoch))
        stat = os.stat(target_file)


def process_file(source, output, folder_map):
    data = text_to_dict(read_file(source))
    write_boostnote_markdown(data, output, folder_map)

def replaceFiles(vuepress_basepath):
    """ replace boostnote storage :\storage with the proper file path 
        :input hardcoded $withBase 
        :output proper replaced files
    """
    basePath = vuepress_basepath + 'images'
    print('writing correct file paths using: ' + basePath)
    files = glob.glob('docs/' + '/**/*.md', recursive=True)
    print(files)
    
    r = re.compile(r':storage\\')
    for file in files:
        print('Reading file: ' + file)
        for line in fileinput.input(file, inplace=1):
            match = r.match(line)
            # if there is a match replace \ with \\
            newLine = line.replace('\\','/')
            print(newLine   .replace(':storage', basePath), end='')
    print('Replaced files with text.')

def fileConfigBase(vuepress_config_path):
    """
    :input: path to vuepress config.js
    :output: base path used in config.js
    """
    p = re.compile(r'base:')  # a pattern for a number
    print('Looking at vuepress config')
    for i, line in enumerate(open(vuepress_config_path)):
        for match in re.finditer(p, line):
            print('Found on line %s: %s' % (i+1, match.groups()))
            print(line)
            vuepress_basepath = re.findall('\'(.*?)\'', line)[0]
            print(vuepress_basepath)
            break
    return vuepress_basepath

def main(boostnote_dir, output):
    """
    :input: input folder path
    :output: output folder path
    """
    folder_map = read_folder_names(os.path.join(boostnote_dir, 'boostnote.json'))
    notes_dir = os.path.join(boostnote_dir, 'notes')
    for name in os.listdir(notes_dir):
        if not name.endswith('.cson'):
            continue

        source = os.path.join(notes_dir, name)
        process_file(source, output, folder_map)


if __name__ == '__main__':
    #fileConfigBase()
    import argparse
    parser = argparse.ArgumentParser(
        description="convert boostnote cson format data to markdown")

    parser.add_argument(
        '-s',
        '--source',
        type=str,
        help="directory store the cson files",
        default=".")
    parser.add_argument(
        '-o', '--output', type=str, help="output directory", default="docs")

    args = parser.parse_args()
  
    main(args.source, args.output)

    
        
    # Global variables
    vuepress_config_path = 'docs/.vuepress/config.js'
    vuepress_basepath = fileConfigBase(vuepress_config_path)
    replaceFiles(vuepress_basepath)
    # Move copy of images folder to public vuepress resources folder          
    images_path = './docs/.vuepress/public/images'

    if os.path.isdir(images_path):
        shutil.rmtree(images_path)
    # Check if images directory exists
    if os.path.isdir('attachments'):
        shutil.copytree('attachments',images_path)
    print('images folder moved if existed')
    #shutil.copytree('images',images_path)