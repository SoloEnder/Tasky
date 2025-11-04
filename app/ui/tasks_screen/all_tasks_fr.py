
import customtkinter as ctk
from ...src.tasks.tasks_data_handler import tasks_data_handler
from ...src.tasks.tasks_frames_handler import tasks_frames_handler
from ...src.tasks import task_creator

class AllTasksFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, player, **kwargs):
        super().__init__(master, **kwargs)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = self.tasks_data_handler.tasks_data

        self.master = master
        self.columnconfigure(0, weight=1)
        self.tasks_frames_handler = tasks_frames_handler
        self.tasks_frames = self.tasks_frames_handler.tasks_frames
        self.no_task_lb = ctk.CTkLabel(self, text="There are no tasks")

        for index, task_data in enumerate(self.tasks_data): # type: ignore
            self.tasks_data = self.tasks_data
            self.task_fr = task_creator.create_task(self, task_data=task_data, player=player)
            self.tasks_frames_handler.add_task_frame(self.task_fr)
            self.task_fr.grid(row=index, pady=10)

        self.tasks_frames_count = len(self.tasks_frames)
        self.refresh()
        self.check_for_new_tasks()

    def check_for_new_tasks(self):
        """
        Check every 200 miliseconds for new task frames objects
        """

        if self.tasks_frames_handler.tasks_frames_count != self.tasks_frames_count:
            self.refresh()

        self.after(500, self.check_for_new_tasks)

    def refresh(self):
        """
        Update the frame for displaying new added task
        """
        self.tasks_frames_count = len(self.tasks_frames)

        if self.tasks_frames:
            self.no_task_lb.grid_forget()

            for index, task_frame in enumerate(self.tasks_frames):
                task_frame.grid(row=index, sticky="ew", padx=8, pady=10)

        else:
            self.no_task_lb.grid(sticky="nsew")
