import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
# window initialization with title, name, size and configuration
window = tk.Tk()
window.title("Emad's To-Do List")
window.geometry("300x300")
window.config(bg= "#66CDAA")
user_taskList= [] 
# Load the background image
bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
# Create a label to display the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# this function updates task list as user interacts with the app
def updateTaskList():
    clearTaskList()
    for task in user_taskList:
        user_tasksBox.insert("end", task)
# this function clears any buffer before user enters any new task
def clearTaskList():
    user_tasksBox.delete(0, "end")
# this function handles entry of new task
def addNewTask():
    task= user_textInput.get() # get input 
    # handling empty input
    if task != "": 
        user_taskList.append(task) # append to task list
        updateTaskList()
        user_textInput.delete(0, tk.END) 
    else:
        messagebox.showwarning("WARNING", "Please enter a task.")
# this function handles deletion of task from list
def removeNewTask(): 
    task= user_tasksBox.get(tk.ACTIVE) # get active status of item
    if task in user_taskList:
        user_taskList.remove(task) # remove from list
        updateTaskList()
# this function handles total number of entries in tasklist at a time
def listFrequency(): 
    # calculate length of tasks and display prompt
    number_ofTasks= len(user_taskList)
    displayPrompt= "Number of tasks: %s" %number_ofTasks
    screenDisplay["text"]= displayPrompt
# set app title through Label()
screenLabel= tk.Label(window, text= "To-Do List", fg= "black", bg= "#cffdeb", font= ("Helvetica", 20))
screenLabel.pack()
# set prompt display through Label()
screenDisplay= tk.Label(window, text= None, font= "Helvetica")
screenDisplay.pack()
# set user input placeholder
user_textInput= tk.Entry(window, width= 30)
user_textInput.pack()
# set add button throug Button()
add_taskButton= tk.Button(window, text= "Add Task", fg= "black", bg= "white", width= 10, command= addNewTask)
add_taskButton.pack(pady= 5)
# set delete button throug Button()
remove_taskButton= tk.Button(window, text= "Remove Task", fg= "black", bg= "white", width= 10, command= removeNewTask)
remove_taskButton.pack(pady= 5)
# set total button throug Button()
frequencyButton= tk.Button(window, text= "Total Tasks", fg= "black", bg= "white", width= 10, command= listFrequency)
frequencyButton.pack(pady= 5)
# create a listbox to view user's tasks
user_tasksBox= tk.Listbox(window, selectbackground= "#F0F8FF", bg= "white", font= "Helvetica", height= 15, width= 30)
user_tasksBox.pack()
# set scrollbars at the right to view all tasks by scrolling up or down
scroll_up_down= tk.Scrollbar(window, orient= tk.VERTICAL)
scroll_up_down.config(command= user_tasksBox.yview)
scroll_up_down.pack(side= tk.RIGHT, fill= tk.Y)
user_tasksBox.config(yscrollcommand= scroll_up_down.set)
user_tasksBox.place(x= 420, y= 195)
# loop which runs application and processes it
tk.mainloop()
