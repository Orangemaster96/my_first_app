import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile



root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=5)


#logo
logo = Image.open('C:\myfirstapp\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#page sel entry
page_sel = tk.Entry()
page_sel.grid(column=1, row=4)


#instructions

instructions = tk.Label(root, text = 'Select pdf file', font = 'Calibri')
instructions.grid(columnspan = 3, column=0, row=1)

#file open
def open_file():
    browse_text.set('Loading...')
    file= askopenfile(parent=root, mode='rb', title='choosefile', filetype=[('PDF File', '*.pdf')])
    
    if file:
        #pagecount display
        read_pdf = PyPDF2.PdfFileReader(file)
        
        pagecount = int(read_pdf.getNumPages())
        pagecount_display = tk.Label(root, text = f'Pagecount is: {pagecount}, choose page to convert:', font = 'Calibri')
        pagecount_display.grid(columnspan=3, column=0, row=3)
        #convert button
        convert_text = tk.StringVar()
        convert_btn = tk.Button(root, textvariable=convert_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:convert_file())
        convert_text.set('Convert')
        convert_btn.grid(column=1, row=5)
        #file conversion
        def convert_file():
            read_pdf = PyPDF2.PdfFileReader(file)
            page = read_pdf.getPage(int(page_sel.get()))
            page_content =page.extractText()
            detect_word_t = "SEO"
            #print(detect_word_t)
            #detect_word = str(page_content.find('Seo'))
            if detect_word_t:
                def substring_after(s, delim):
                    list_of_words = s.split()
                    next_word= list_of_words[list_of_words.index(delim)+1]
                    return next_word
                    #return s.partition(delim)[2:3]
                
                word = substring_after(page_content, str(detect_word_t))
                print(word)
                word_display =tk.Label(root, text = f'{word}', font = 'Calibri')
                word_display.grid(columnspan = 3, column=0, row=6)
            else:
                print('did not work')
                #detected_word = page_content.find('seo')
            #textbox
            text_box = tk.Text(root, height=15, width=50, padx=15, pady=15)
            text_box.insert(1.0, page_content)
            text_box.tag_configure('center', justify='center', font='Calibri', wrap='word')
            text_box.tag_add('center', 1.0, 'end')
            text_box.grid(column=1, row=7)
            browse_text.set('Browse')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:open_file())
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)



canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)



root.mainloop()
