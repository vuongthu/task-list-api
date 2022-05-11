from app import db
from sqlalchemy.sql import func

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return dict(
            id = self.task_id,
            title = self.title,
            description = self.description,
            is_complete = True if self.completed_at else False
            )


    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            description = data_dict["description"],
            completed_at = data_dict["completed_at"] if "completed_at" in data_dict else None
        )

    def replace_details(self, data_dict):
        self.title = data_dict["title"]
        self.description = data_dict["description"]
        self.completed_at = data_dict["completed_at"] if "completed_at" in data_dict else None

    def check_keys(self, data_dict):
        patch_keys = data_dict.keys()
        for key in ["title", "description", "completed_at"]:
            if key in patch_keys:
                setattr(self, key, data_dict[key])
    
    def mark_completed(self):
        self.completed_at = func.now()
    
    def mark_incompleted(self):
        self.completed_at = None