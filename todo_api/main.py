from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from schemas import TodoCreate, TodoUpdate, Todo, User, UserCreate, UserLogin, Token
from models import TodoModel, UserModel
from typing import List
from security import hash_password, verify_password, create_access_token, get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(title='To Do API', version="1.0.0")

@app.get('/')
async def root():
    return {"message": "Welcome to todo API homepage"}


@app.post('/todos', response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    db_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.get('/todos', response_model=List[Todo], status_code=status.HTTP_200_OK)
async def get_todos(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    all_todos = db.query(TodoModel).all()
    return all_todos


@app.get('/todos/{todo_id}', response_model=Todo, status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo Not Found')
    return todo


@app.put("/todos/{todo_id}", response_model=Todo, status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    todo_db = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo Not Found')
    todo_params = todo.model_dump(exclude_none=True)
    db.query(TodoModel).filter(TodoModel.id == todo_id).update(todo_params)
    db.commit()
    db.refresh(todo_db)
    return todo_db


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not found")
    db.delete(todo)
    db.commit()
    return


@app.post('/users/register', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User Already Exists')
    hashed = hash_password(user.password)
    db_user = UserModel(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post('/login', response_model=Token)
async def user_login(login: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == login.email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    is_correct = verify_password(login.password, db_user.hashed_password)
    if not is_correct:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
    token = create_access_token({'email': db_user.email})
    return {
        "access_token": token,
        "token_type": "bearer"
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
