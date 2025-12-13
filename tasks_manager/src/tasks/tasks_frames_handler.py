
import logging

class TasksFramesHandler:

    def __init__(self, tasks_frames: list=[]):
        self.logger = logging.getLogger(__name__)
        self.tasks_frames = tasks_frames
        self.tasks_frames_count = len(tasks_frames)

    def add_task_frame(self, *frames):
        """
        Add new frame to the tasks frames list

        Args:
            - frames (tuple): a tuple containing the frames to add
        """

        for frame in frames:
            self.tasks_frames.insert(0, frame)
            self.tasks_frames_count += 1
        self.logger.info("A task frame has been added to the tasks frames list")

    def remove_task_frame(self, *tasks_indexes):
        
        for task_index in tasks_indexes:
            task_object = self.tasks_frames[task_index]
            task_object.destroy()
            del self.tasks_frames[task_index]
            self.tasks_frames_count -= 1
            
        self.logger.info("A task frame has been removed from the tasks frames list")

tasks_frames_handler = TasksFramesHandler()
