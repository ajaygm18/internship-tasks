from fastapi import FastAPI, Query, Path, Body, Header, HTTPException, status, Depends
from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import Optional, List
from enum import Enum


# ===================== APP SETUP =====================
app = FastAPI(
    title="FastAPI Learning App",
    description="A comprehensive app to learn FastAPI concepts",
    version="1.0.0"
)


# ===================== ENUMS =====================
class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


# ===================== PYDANTIC MODELS =====================
# Request Model
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="User's full name")
    email: EmailStr = Field(..., description="User's email address")
    age: int = Field(..., gt=0, le=120, description="Age must be between 1 and 120")
    role: UserRole = Field(default=UserRole.user)
    tags: List[str] = Field(default_factory=list)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "age": 25,
                    "role": "user",
                    "tags": ["developer", "python"]
                }
            ]
        }
    }


# Response Model
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    role: UserRole

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18


# Update Model (all fields optional)
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, gt=0, le=120)


# ===================== FAKE DATABASE =====================
fake_db: dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30, "role": "admin"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 25, "role": "user"},
}


# ===================== DEPENDENCIES =====================
def get_current_user(x_token: str = Header(..., description="Authentication token")):
    """Dependency to validate user token"""
    if x_token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": "authenticated_user"}


def pagination_params(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max items to return")
):
    """Reusable pagination dependency"""
    return {"skip": skip, "limit": limit}


# ===================== ROUTES =====================

# 1. Basic GET
@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to FastAPI Learning App!"}


# 2. Path Parameters with validation
@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(
    user_id: int = Path(..., gt=0, description="The ID of the user to get")
):
    """Get a user by ID - demonstrates Path parameters"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return fake_db[user_id]


# 3. Query Parameters
@app.get("/users", response_model=List[UserResponse], tags=["Users"])
def get_users(
    pagination: dict = Depends(pagination_params),
    role: Optional[UserRole] = Query(None, description="Filter by role")
):
    """Get all users - demonstrates Query params and Dependencies"""
    users = list(fake_db.values())
    
    if role:
        users = [u for u in users if u["role"] == role]
    
    skip = pagination["skip"]
    limit = pagination["limit"]
    return users[skip : skip + limit]


# 4. POST with Request Body
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: UserCreate):
    """Create a new user - demonstrates Request Body"""
    new_id = max(fake_db.keys()) + 1 if fake_db else 1
    new_user = {"id": new_id, **user.model_dump()}
    fake_db[new_id] = new_user
    return new_user


# 5. PUT - Full Update
@app.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(
    user_id: int = Path(..., gt=0),
    user: UserCreate = Body(...)
):
    """Update a user completely - demonstrates PUT"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = {"id": user_id, **user.model_dump()}
    fake_db[user_id] = updated_user
    return updated_user


# 6. PATCH - Partial Update
@app.patch("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def partial_update_user(
    user_id: int = Path(..., gt=0),
    user: UserUpdate = Body(...)
):
    """Partially update a user - demonstrates PATCH"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored_user = fake_db[user_id]
    update_data = user.model_dump(exclude_unset=True)  # Only get provided fields
    updated_user = {**stored_user, **update_data}
    fake_db[user_id] = updated_user
    return updated_user


# 7. DELETE
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: int = Path(..., gt=0)):
    """Delete a user - demonstrates DELETE"""
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return None


# 8. Protected Route with Dependency
@app.get("/protected", tags=["Auth"])
def protected_route(current_user: dict = Depends(get_current_user)):
    """Protected endpoint - demonstrates Header auth dependency"""
    return {"message": f"Hello, {current_user['username']}!"}


# 9. Multiple Path and Query params
@app.get("/users/{user_id}/items/{item_id}", tags=["Advanced"])
def get_user_item(
    user_id: int = Path(..., gt=0),
    item_id: int = Path(..., gt=0),
    q: Optional[str] = Query(None, max_length=50),
    short: bool = Query(False, description="Short description")
):
    """Multiple path params - demonstrates complex routing"""
    return {
        "user_id": user_id,
        "item_id": item_id,
        "query": q,
        "short": short
    }


