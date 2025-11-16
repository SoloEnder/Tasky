import customtkinter as ctk
from tkinter.messagebox import showinfo
import datetime as dt
import logging
from tkinter.messagebox import askyesno
from ...src.tasks.tasks_data_handler import tasks_data_handler
from ...src.tasks.tasks_frames_handler import tasks_frames_handler
from ...src.tasks import task_creator

class TaskEditorFrame(ctk.CTkFrame):

    def __init__(self, master, user, **kwargs) :
        super().__init__(master, **kwargs)
        self.user = user
        self.logger = logging.getLogger(__name__)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = tasks_data_handler.tasks_data
        self.tasks_frames_handler = tasks_frames_handler
        self.tasks_frames = tasks_frames_handler.tasks_frames
        self.logger = logging.getLogger(__name__)

        self.mode = "creation"
        self.task_index = 0

        self.current_date = dt.datetime.today()
        self.error_window_title = "Info"
        self.error_window_msg = None
        self.button_color_1 = "gray17"

        self.cancel_b = ctk.CTkButton(self, text="X", fg_color=self.button_color_1, width=1, command=lambda: self.switch_mode(mode="creation"))

        self.title_lb = ctk.CTkLabel(self, text="Title").grid(row=1, sticky="w", pady=5)
        self.title_e = ctk.CTkEntry(self)
        self.title_e.grid(row=2, sticky="ew")

        self.difficulty_lb = ctk.CTkLabel(self, text="Difficulty").grid(row=3, sticky="w", pady=5)
        self.difficulty_om = ctk.CTkOptionMenu(self, values=["Basic", "Normal", "Hard", "Very hard"])
        self.difficulty_om.grid(row=4, sticky="ew")

        self.bad_input_b = ctk.CTkButton(self, text="!", text_color="red", command=self.show_problem_window, width=1, fg_color=self.button_color_1)

        self.description_lb = ctk.CTkLabel(self, text="Description").grid(row=5, sticky="w", pady=5)
        self.description_tb = ctk.CTkTextbox(self)
        self.description_tb.grid(row=6)

        self.confirm_b = ctk.CTkButton(self, text="Add", command=self.edit_task, width=9) #type: ignore
        self.confirm_b.grid(row=7, sticky="ew", pady=5)

        self.delete_b = ctk.CTkButton(self, text="Delete", text_color="red", fg_color=self.button_color_1, width=9, command=lambda: self.switch_mode(mode="deletion", confirm_deletion=True))

    def get_task_data(self):
        title = self.title_e.get()

        if not title:
            self.error_window_msg = "This text field can't be empty !"
            self.bad_input_b.grid(row=1, sticky="e")
            return

        if self.check_existence(title):
            self.error_window_msg = "Title already used"
            self.bad_input_b.grid(row=1, sticky="e")
            return

        difficulty = self.difficulty_om.get()

        self.bad_input_b.grid_forget()
        description = self.description_tb.get(0.0, ctk.END)
        data = {
            "title":title,
            "description":description,
            "difficulty":difficulty,
            "creation_date":str(self.current_date),
            "deadline_date":"",
            "task_index":len(self.tasks_data) # type: ignore
        }
        return data

    def check_existence(self, title):
        
        for index, task in enumerate(self.tasks_data): # type: ignore

            if task["title"] == title:

                if index == self.task_index and self.mode == "edition":
                    return
                
                return True
            
    def show_problem_window(self):
        showinfo(self.error_window_title, self.error_window_msg)

    def edit_task(self):
        self.new_task_data = self.get_task_data()

        if self.new_task_data:
            self.new_task = task_creator.create_task(self.master.all_tasks_fr, self.user, self.new_task_data) # type: ignore
            self.logger.info("A task frame has been created")

            if self.mode == "creation":
                self.tasks_data.insert(0, self.new_task_data) # type: ignore
                self.tasks_frames_handler.add_task_frame(self.new_task)
                self.logger.info("A task has been created")

            elif self.mode == "edition":
                self.tasks_frames[self.task_index].destroy()
                self.tasks_frames[self.task_index] = self.new_task
                self.tasks_data[self.task_index] = self.new_task_data # type: ignore
                self.master.all_tasks_fr.refresh() # type: ignore
                self.logger.info("A task has been edited")

    def switch_mode(self, task_index: int=0, task_data: dict={}, mode: str="creation", confirm_deletion: bool=False):
        self.logger.info(f"Switched to task {mode} mode")
        self.task_index = task_index

        if mode == "creation":
            self.mode = "creation"
            self.cancel_b.grid_remove()
            self.title_e.delete(0, ctk.END)
            self.description_tb.delete(0.0, ctk.END)
            self.confirm_b.configure(command=self.edit_task)
            self.confirm_b.configure(text="Add", command=self.edit_task)
            self.confirm_b.grid(row=7, sticky="ew")
            self.delete_b.grid_forget()

        elif mode == "edition":
            self.mode = "edition"
            self.task_index = task_index
            self.title_e.delete(0, ctk.END)
            self.description_tb.delete(0.0, ctk.END)
            self.cancel_b.grid(row=0, sticky="e")
            self.title_e.insert(0, task_data["title"])
            self.description_tb.insert(0.0, task_data["description"])
            self.confirm_b.configure(text="Apply", command=self.edit_task)
            self.confirm_b.grid(row=7, sticky="e")
            self.delete_b.grid(row=7, sticky="w")

        elif mode == "deletion":
            self.delete_task(confirm_deletion)

    def delete_task(self, confirm_deletion: bool=True):
        """
        Delete a task object and his data
        """

        self.deletion_confirmation = True

        if confirm_deletion:
            self.deletion_confirmation = askyesno(title="Tasks Gamifier | Delete Task", message="Are you sure you want to delete this task ?")
        
        if self.deletion_confirmation:
            self.tasks_frames_handler.remove_task_frame((self.task_index))
            del self.tasks_data_handler.tasks_data[self.task_index] # type: ignore
            self.logger.info("A task has been deleted")
            self.switch_mode(mode="creation")
