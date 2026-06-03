from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import TaskCreate, TaskResponse
from app.models import Task, User
from app.dependencies import get_db
from app.core.debs import get_current_user

router = APIRouter()

# ---------------- CREATE TASK (JWT PROTECTED) ----------------
@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(User.username == current_user).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# ---------------- GET TASKS (ONLY USER TASKS) ----------------
@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(User.username == current_user).first()

    return db.query(Task).filter(Task.user_id == user.id).all()


# ---------------- UPDATE TASK ----------------
@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(User.username == current_user).first()

    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = task_data.title
    task.description = task_data.description

    db.commit()
    db.refresh(task)

    return task


# ---------------- DELETE TASK ----------------
@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(User.username == current_user).first()

    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}