
import customtkinter as ctk
import logging
from ...src.tasks.tasks_data_handler import tasks_data_handler
from ...src.tasks.tasks_frames_handler import tasks_frames_handler
from ...src.tasks import task_creator

class AllTasksFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = self.tasks_data_handler.tasks_data

        self.master = master
        self.logger = logging.getLogger(__name__)
        self.columnconfigure(0, weight=1)
        self.tasks_frames_handler = tasks_frames_handler
        self.tasks_frames = self.tasks_frames_handler.tasks_frames
        self.no_task_lb = ctk.CTkLabel(self, text="There are no tasks")

        self.logger.info("Creating tasks frames...")
        for index, task_data in enumerate(self.tasks_data): # type: ignore
            self.tasks_data = self.tasks_data
            self.task_fr = task_creator.create_task(self, task_data=task_data, user=user)
            self.tasks_frames_handler.add_task_frame(self.task_fr)
            self.rowconfigure(index, weight=1)
            self.task_fr.grid(row=index, pady=10, sticky="new")

        self.tasks_frames_count = len(self.tasks_frames)
        self.refresh()
        self.check_count = 0
        self.check_for_new_tasks()

    def check_for_new_tasks(self):
        """
        Check every 200 miliseconds for new task frames objects
        """

        if self.tasks_frames_handler.tasks_frames_count != self.tasks_frames_count:
            self.logger.info("Detected modification on tasks, refreshing screen...")
            self.refresh()

        self.check_count += 1
        
        if self.check_count % 100 == 0:
            self.logger.debug(f"Checking for new tasks {self.check_count} time")

        self.after(500, self.check_for_new_tasks)

    def refresh(self):
        """
        Update the frame for displaying new added task
        """

        if self.tasks_frames:
            self.no_task_lb.grid_forget()

            for index, task_frame in enumerate(self.tasks_frames):
                task_frame.grid(row=index, sticky="ew", padx=8, pady=10)
                self.rowconfigure(index, weight=1)

        else:
            self.no_task_lb.grid(row=0, sticky="ew")
        self.logger.info("Tasks screen refreshed")
