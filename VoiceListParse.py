import PySimpleGUI as sg
from subprocess import check_output
from subprocess import call
import re

def main():
    #Find our what speakers are allowed through the tool
    report_string = check_output("balcon -l", shell=True).decode()
    #print( report_string )
    intro_split = report_string.split(':')
    #print( intro_split )
    intro_removed = intro_split.pop()
    #print( intro_removed )
    separated_list = intro_removed.splitlines()
    #print( separated_list )
    final_list = [ ]
    for possible_voice in separated_list:
        print( "Possible Voice: " + possible_voice )
        if not possible_voice or not possible_voice.strip():
            continue
    #    print( "Possible Stripped Voice: " + possible_voice )
        p = re.compile('(\s*)[-,].*')
        post_strip = p.sub(' ', possible_voice)
    #    print( post_strip )
        final_list.append( post_strip.strip() )
    print( final_list )

if __name__ == '__main__':
    main()