
import customtkinter as ctk
import logging

class TaskFrame(ctk.CTkFrame):

    def __init__(self, master, user, task_data, **kwargs):
        super().__init__(master, **kwargs)

        for i in range(2):
            self.columnconfigure(i, weight=1)

        self.task_data = task_data
        self.user = user
        self.master = master
        self.logger = logging.getLogger(__name__)
        self.bg_color = "grey17"

        self.title_font = ctk.CTkFont(weight="bold")
        

        self.complete_task_cb = ctk.CTkCheckBox(self, text=self.task_data["title"], command=self.complete_task, fg_color="blue", font=self.title_font)
        self.complete_task_cb.grid(row=0, column=0, sticky="w", padx=8, pady=5)

        self.difficulty_levelename_colors = {
            "Basic":"green",
            "Normal":"yellow",
            "Hard":"dark red",
            "Very hard":"red"
        }

        self.difficulty = self.task_data["difficulty"]
        self.difficulty_lb = ctk.CTkLabel(self, text=self.difficulty, text_color=self.difficulty_levelename_colors[self.difficulty])
        self.difficulty_lb.grid(row=0, column=2, sticky="e", padx=8)
        self.description_sv = ctk.StringVar(self)
        self.description_tb = ctk.CTkTextbox(self,  height=90, fg_color=self.bg_color)
        self.description_tb.insert(0.0, self.task_data["description"])
        self.description_tb.configure(state="disabled")
        self.description_tb.grid(row=1, columnspan=2, column=0, sticky="ew", padx=8)
        self.deadline_date_lb = ctk.CTkLabel(self, text=self.task_data["deadline_date"])
        self.deadline_date_lb.grid(row=2, column=0, sticky="w", padx=8)
        self.edit_b = ctk.CTkButton(self, text="...", width=3, fg_color=self.bg_color, command=lambda: self.master.master.task_editor_fr.switch_mode(task_data = self.task_data, mode="edition", task_index=self.grid_info()["row"])) # type: ignore
        self.edit_b.grid(row=2, column=2, sticky="e", padx=8)

    def complete_task(self):
        self.logger.info("A task completion request has been received")
        self.master.master.task_editor_fr.switch_mode(mode="deletion", task_index=self.grid_info()["row"], confirm_deletion=False)  # type: ignore