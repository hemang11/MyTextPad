import tkinter as tk
from tkinter import ttk
from tkinter import font,messagebox,filedialog,colorchooser
import os # For file Handling


win=tk.Tk()
win.geometry('1200x600')
win.title('NOTEPAD_2.0')
win.wm_iconbitmap('notepad_ico.ico')
############################---Main Menu--#############################
main_menu=tk.Menu(win)

# File Icons
new_icon=tk.PhotoImage(file='icons/new.png')
open_icon=tk.PhotoImage(file='icons/open.png')
save_icon=tk.PhotoImage(file='icons/save.png')
save_as_icon=tk.PhotoImage(file='icons/save_as.png')
exit_icon=tk.PhotoImage(file='icons/exit.png')

# Edit icons
copy_icon=tk.PhotoImage(file='icons/copy.png')
paste_icon=tk.PhotoImage(file='icons/paste.png')
cut_icon=tk.PhotoImage(file='icons/cut.png')
clearall_icon=tk.PhotoImage(file='icons/clear_all.png')
find_icon=tk.PhotoImage(file='icons/find.png')

# View icons
toolbar_icon=tk.PhotoImage(file='icons/tool_bar.png')
statusbar_icon=tk.PhotoImage(file='icons/status_bar.png')

# Color theme icons
light_theme_default=tk.PhotoImage(file='icons/light_default.png')
light_theme_plus=tk.PhotoImage(file='icons/light_plus.png')
dark_theme=tk.PhotoImage(file='icons/dark.png')
red_theme=tk.PhotoImage(file='icons/red.png')
monokai_theme=tk.PhotoImage(file='icons/monokai.png')
nightblue_theme=tk.PhotoImage(file='icons/night_blue.png')

# File Menu
File=tk.Menu(main_menu,tearoff=0)

# Edit Menu
Edit=tk.Menu(main_menu,tearoff=0)

# View Menu
View=tk.Menu(main_menu,tearoff=0)

# Color Theme Menu
ColorTheme=tk.Menu(main_menu,tearoff=0)

# Color Theme Commands
theme_choice=tk.StringVar()
color_icons=(light_theme_default,light_theme_plus,dark_theme,red_theme,monokai_theme,nightblue_theme)

# Color dict contains options to choose from tuple (foreground,background) color
color_dict={
    'Light Default':('#000000', '#ffffff'),
    'Light Plus':('#474747', '#e0e0e0'),
    'Dark':('#c4c4c4', '#2d2d2d'),
    'Red':('#2d2d2d', '#ffe8e8'),
    'Monokai':('#d3b774', '#474747'),
    'Nightblue':('#ededed', '#6b9dc2')
}

#cascading menues with the main menu(win)
main_menu.add_cascade(label='File',menu=File)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=View)
main_menu.add_cascade(label='Color Theme',menu=ColorTheme)


#-----------------------------End of Main Menu-------------------------


############################---ToolBar--#############################
# Creating a label on which we will put our toolbar eg->fontfamily,font size etc... 
tool_bar=ttk.Label(win)
#tool_bar.configure(background='#e6e8e7')
tool_bar.pack(side=tk.TOP,fill=tk.X) # variable stretches in horizontal row

# Font Box By creating Combobox
fonts_tuple=tk.font.families() # tuple consisting of all font families
font_var=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_var,state='readonly') # textvariable stores the selected font
font_box['values']=fonts_tuple
font_box.current(fonts_tuple.index('Arial')) # Seleting Default Value as Arial in font_box
font_box.grid(row=0, column=0, padx=5)

# Size Box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81)) #Gap of 2
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# Bold Button Italic And Underline button
bold_icon=tk.PhotoImage(file='icons/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_icon=tk.PhotoImage(file='icons/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_icon=tk.PhotoImage(file='icons/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# Font Color Button
fontcolor_icon=tk.PhotoImage(file='icons/font_color.png')
fontcolor_btn=ttk.Button(tool_bar,image=fontcolor_icon)
fontcolor_btn.grid(row=0,column=5,padx=5)

# 3 buttons left,right,center align
align_left_icon=tk.PhotoImage(file='icons/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

align_center_icon=tk.PhotoImage(file='icons/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

align_right_icon=tk.PhotoImage(file='icons/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)



#-----------------------------End of ToolBar-------------------------


############################---Text Editor--#############################

text_editor=tk.Text(win)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font family and Font Size functionality
current_font_family='Arial'
current_font_size=16

def change_font_family(event=None):
    global current_font_family
    current_font_family=font_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

# Binding Combobox
font_box.bind('<<ComboboxSelected>>',change_font_family)
font_size.bind('<<ComboboxSelected>>',change_font_size)

##### Button Funtionality
# Bold
def bold_text():
    font_prop=tk.font.Font(font=text_editor['font']) # This will give dictionary of all font properties
    if font_prop.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if font_prop.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=bold_text)

# Italic
def italic_text():
    font_prop=tk.font.Font(font=text_editor['font']) # This will give dictionary of all font properties
    if font_prop.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if font_prop.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_btn.configure(command=italic_text)

# Underline
def Underline_text():
    font_prop=tk.font.Font(font=text_editor['font']) # This will give dictionary of all font properties
    if font_prop.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if font_prop.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=Underline_text)

# Font Color functonality
def change_fontColor():
    color_var=tk.colorchooser.askcolor() # color_var is a tuple with rgb at 0 index and hexadecimal at index 1 
    text_editor.configure(fg=color_var[1])
     
fontcolor_btn.configure(command=change_fontColor)

# Align functions

# We will store all the text in a variable and then we'll delete the text in text_editor and 
# then align the text accordingly then insert the content of the variable in the text_editor again

# Align Left
def align_left():
    text_content=text_editor.get(1.0,'end') # get all the values in the text editor
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END) # delete all the information in the text editor
    text_editor.insert(tk.INSERT,text_content,'left') # insert text_content in the text_editor again

align_left_btn.configure(command=align_left)

# Align center
def align_center():
    text_content=text_editor.get(1.0,'end') 
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END) 
    text_editor.insert(tk.INSERT,text_content,'center') 
    
align_center_btn.configure(command=align_center)

# Align Right
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END) 
    text_editor.insert(tk.INSERT,text_content,'right') 
    
align_right_btn.configure(command=align_right)

# Configuring text_editor
text_editor.configure(font=('Arial',16))

#-----------------------------End of Text Editor-----------------------------


############################---Status Bar--#############################

status_bar=ttk.Label(win,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None): # No event is selected
    if text_editor.edit_modified(): # chek if any modification occurs in text_editor
        global text_changed
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split()) # 1-c is used for deleting extra characters
        characters=len(text_editor.get(1.0,'end-1c')) # You can use .replace(' ','') so that spaces are replaced so no sapces is count in characters
        status_bar.config(text=f'Characters: {characters} Words: {words}')
    text_editor.edit_modified(False) # setting to false again so if modified again in the future ca be used

text_editor.bind('<<Modified>>',changed)

#-----------------------------End of Staus Bar--------------------------


###########################---Main Menu functionality--################
#<----------------- Commands are Declared here as commands require functions which should be defined above in text Editor--->

url='' # checks url of all files

## File Functionality

# New functionality
def new_file(event=None): # Event is none as we will bind this with the shortcut keys so no problem should occur
    global url
    url=''
    text_editor.delete(1.0,tk.END) # new file just deletes original data

# Open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as f:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,f.read())
    except FileNotFoundError:
        return
    except:
         return
    win.title(os.path.basename(url))

# Save Files
def save_file(event=None):
    global url
    try:
        if url: # if url is non empty or file exists
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as f:
                f.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# Save as
def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return

# Exit functionality

def exit_func(event=None):
    global url
    try:
        if text_changed:  # text changed declared above
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file')
            if mbox is True: # He wants to save the file
                if url: # if file already exists
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as f:
                        f.write(content)
                        win.destroy() # destroying the window after save
                else: # if the file do not exist
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False: # He doesn't want to save the file
                win.destroy()
        else:
            win.destroy()
    except:
        return


# File Commands
File.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
File.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
File.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
File.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=save_as)
File.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,command=exit_func)

# Find functionality
def find_func(event=None):

    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')


    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## Frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    ## Labels
    text_find_label=ttk.Label(find_frame,text='Find: ')
    text_replace_label=ttk.Label(find_frame,text='Replace: ')

    ## Entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    ## Button
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)

    ## Label Grid
    text_find_label.grid(row=0,column=0,padx=4,pady=8)
    text_replace_label.grid(row=1,column=0,padx=4,pady=8)

    ## Entry grid
    find_input.grid(row=0,column=1,padx=4,pady=8)
    replace_input.grid(row=1,column=1,padx=4,pady=8)

    ## Button Grid
    find_button.grid(row=2,column=0,padx=8,pady=8)
    replace_button.grid(row=2,column=1,padx=8,pady=8)

    find_dialogue.mainloop()

# Edit Commands
Edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
Edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
Edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
Edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
Edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

# Vew Functionality
show_tool_bar=tk.BooleanVar()
show_status_bar=tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar.set(True)

def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar=True

def hide_status_bar():
    global  show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True

# View Commands
View.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,image=toolbar_icon,variable=show_tool_bar,compound=tk.LEFT,command=hide_tool_bar)
View.add_checkbutton(label='Status Bar',onvalue=1,offvalue=0,image=statusbar_icon,variable=show_status_bar,compound=tk.LEFT,command=hide_status_bar)

# Color Theme
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)

count=0
for i in color_dict:
    ColorTheme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

#-------------------------- End of Main Menu Functionality----------------------------------------

win.config(menu=main_menu)

############### Bind ShortCut Keys ############################

win.bind('<Control-n>',new_file)
win.bind('<Control-o>',open_file)
win.bind('<Control-s>',save_file)
win.bind('<Control-Alt-s>',save_as)
win.bind('<Control-q>',exit_func)
win.bind('<Control-f>',find_func)

win.mainloop()