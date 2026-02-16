from fastapi import FastAPI, Depends, status
import schema
import database


storage = {}
stg = [
    schema.Candidate(id=1, name='Ajay Gonhalmath', age=21, education='BE', previousCTC=7.5, experience=1),
    schema.Candidate(id=2, name='RTX', age=999999999, education='BE', previousCTC=800, experience=999999),
    schema.Candidate(id=3, name='GTX', age=999999999, education='BE', previousCTC=800, experience=999999)
]

stg2 = [
    schema.Admin(id=1, name='First Person', age=21),
    schema.Admin(id=2, name='Second Person', age=22),
    schema.Admin(id=3, name='Third Person', age=21),
    schema.Admin(id=4, name='Fourth Person', age=22),
    schema.Admin(id=5, name='Fifth Person', age=22)
]

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = database.sessionLocal()
    count = db.query(database.Candidate).count()
    countx = db.query(database.Admin).count()

    if count > 0 and countx > 0:
        return
    

    if count > 0:
        for candidate in stg:
            db.add(database.Candidate(**candidate.model_dump()))


    if countx > 0:
        return
    for admin in stg2:
        db.add(database.Admin(**admin.model_dump()))

    db.commit()
    db.close()

init_db()

app = FastAPI(title='Fast API test',
              version='1.0.0',
              description='This is a learning test Fast API backend server')

database.Base.metadata.create_all(bind=database.engine)

@app.get('/', status_code=status.HTTP_200_OK, response_model=list[schema.showCandidate])
def root(db: database.Session = Depends(get_db)):
    candidates = db.query(database.Candidate).all()
    return candidates


@app.post('/candidate')
def create(request: schema.Candidate, db: database.Session = Depends(get_db)):
    candidate = request.model_dump()
    db.add(database.Candidate(**candidate))
    db.commit()
    return "Create Success"
    

@app.put('/candidate/{id}')
def update(request: schema.Candidate, id: int, db: database.Session = Depends(get_db)):
    candidate = request.model_dump()
    db.query(database.Candidate).filter(database.Candidate.id == id).update(candidate)
    db.commit()
    return "Update Success"


@app.get('/candidate/{id}', response_model=schema.Candidate)
def read(id: int, db: database.Session = Depends(get_db)):
    candidate = db.query(database.Candidate).filter(database.Candidate.id == id).first()
    return candidate


@app.delete('/candidate/{id}')
def delete(id: int, db: database.Session = Depends(get_db)):
    db.query(database.Candidate).filter(database.Candidate.id == id).delete()
    db.commit()
    return 'Delete Success'


@app.post('/candidate/top')
def gettop(db: database.Session = Depends(get_db)):
    cands = db.query(database.Candidate).order_by(database.Candidate.experience, ).all()[::-1]
    return cands


@app.post('/user')
def check_admin(id: int, db: database.Session = Depends(get_db)):
    admins = db.query(database.Admin).filter(database.Admin == id)
    return admins

