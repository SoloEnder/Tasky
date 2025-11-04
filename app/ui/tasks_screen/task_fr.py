
import customtkinter as ctk

class TaskFrame(ctk.CTkFrame):

    def __init__(self, master, player, task_data, **kwargs):
        super().__init__(master, **kwargs)
        self.task_data = task_data
        self.player = player
        self.master = master

        self.title_font = ctk.CTkFont(weight="bold")

        self.complete_task_cb = ctk.CTkCheckBox(self, text="", command=self.complete_task)
        self.complete_task_cb.grid(row=0, column=0, sticky="w", padx=8, pady=5)
        self.title_lb = ctk.CTkLabel(self, text=self.task_data["title"], font=self.title_font)
        self.title_lb.grid(row=0, column=0)
        
        self.difficulty_values = {
            "1":5,
            "2":8,
            "3":10,
            "4":15,
            "5":18,
            }
        self.difficulty = self.task_data["difficulty"]
        self.difficulty_lb = ctk.CTkLabel(self, text=f"+{self.difficulty_values[self.difficulty]}XP")
        self.difficulty_lb.grid(row=0, column=1, sticky="e", padx=8)
        self.description_lb = ctk.CTkLabel(self, text=self.formatte_text(self.task_data["description"]), justify="left")
        self.description_lb.grid(row=1, columnspan=2)
        self.deadline_date_lb = ctk.CTkLabel(self, text=self.task_data["deadline_date"])
        self.deadline_date_lb.grid(row=2, column=0, sticky="w", padx=8)
        self.edit_b = ctk.CTkButton(self, text="...", width=3, fg_color="gray17", command=lambda: self.master.master.task_editor_fr.switch_mode(task_data = self.task_data, mode="edition", task_index=self.grid_info()["row"])) # type: ignore
        self.edit_b.grid(row=2, column=1, sticky="e", padx=8)

    def formatte_text(self, text):

        if len(text) > 23:
            text = text[:20] + "..."

        return text
    
    def complete_task(self):
        self.player.add_xp(self.difficulty_values[self.difficulty])
        self.master.master.task_editor_fr.switch_mode(mode="deletion", task_index=self.grid_info()["row"], confirm_deletion=False)  # type: ignore
        