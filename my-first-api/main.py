from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional, Annotated
from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, select, or_, col


class Note(SQLModel, table=True):
    __tablename__ = 'notes'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    category: str
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Many-to-many relationship with Tag (implicit link table)
    tags: list["Tag"] = Relationship(back_populates="notes")

class Tag(SQLModel, table=True):
    __tablename__ = 'tags'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)  # Unique tag name
    
    # Many-to-many relationship with Note (implicit link table)
    notes: list[Note] = Relationship(back_populates="tags")

# Create database engine
engine = create_engine("sqlite:///notes.db")

# Create tables (Note, Tag, and link table)
SQLModel.metadata.create_all(engine)


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list [str] = []

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    tags: list [str] = []
    created_at: str

    class Config:
        from_attributes = True

def get_session():
    """Create a new database session for each request"""
    with Session(engine) as session:
        yield session

# Type alias for cleaner code
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(
    title= "Applied Programming Course HS-Coburg",
    description="Simple note managment API",
    version="0.1.0"
)


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate, session: SessionDep) -> NoteResponse:
    """Create a new note in database"""
    
    # Create note
    db_note = Note(
        title=note.title,
        content=note.content,
        category=note.category
    )
    
    # Get or create tags (case-insensitive, deduplicated)
    tag_objects = []
    seen_tags = set()
    
    for tag_name in note.tags:
        tag_name_lower = tag_name.lower().strip()
        if not tag_name_lower or tag_name_lower in seen_tags:
            continue
        
        seen_tags.add(tag_name_lower)
        
        # Find existing tag or create new one
        statement = select(Tag).where(Tag.name == tag_name_lower)
        existing_tag = session.exec(statement).first()
        
        if existing_tag:
            tag_objects.append(existing_tag)
        else:
            new_tag = Tag(name=tag_name_lower)
            session.add(new_tag)
            tag_objects.append(new_tag)
    
    db_note.tags = tag_objects
    
    session.add(db_note)
    session.commit()
    session.refresh(db_note)  # Get the generated ID and load relationships
    
    # Convert to response model
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        content=db_note.content,
        category=db_note.category,
        tags=[tag.name for tag in db_note.tags],
        created_at=db_note.created_at.isoformat()
    )

@app.get("/notes")
def list_notes(
    session: SessionDep,
    category: str = None,
    search: str = None,
    tag: str = None
) -> list[NoteResponse]:
    """List notes with filters"""
    
    # Build query
    statement = select(Note)
    
    # Apply filters
    if category:
        statement = statement.where(Note.category == category)
    
    if search:
        search_lower = search.lower()
        statement = statement.where(
            or_(
                col(Note.title).ilike(f"%{search_lower}%"),
                col(Note.content).ilike(f"%{search_lower}%")
            )
        )
    
    if tag:
        tag_lower = tag.lower()
        statement = statement.join(Note.tags).where(Tag.name == tag_lower)
    
    # Execute query
    notes = session.exec(statement).all()
    
    # Convert to response models
    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            tags=[tag.name for tag in n.tags],
            created_at=n.created_at.isoformat()
        )
        for n in notes
    ]

@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, session: SessionDep):
    
    db_note = session.get(Note, note_id)
    # Not found - raise 404 error
    if not db_note:
        raise HTTPException(
            status_code=404,
            detail=f"Note with ID {note_id} not found"
        )
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        content=db_note.content,
        category=db_note.category,
        tags=[tag.name for tag in db_note.tags],
        created_at=db_note.created_at.isoformat()
    )

@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_update: NoteCreate, session: SessionDep):
    db_note = session.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    db_note.title = note_update.title
    db_note.content = note_update.content
    db_note.category = note_update.category

    # Tags aktualisieren
    tag_objects = []
    for tag_name in note_update.tags:
        tag_name_clean = tag_name.lower().strip()
        existing_tag = session.exec(select(Tag).where(Tag.name == tag_name_clean)).first()
        if existing_tag:
            tag_objects.append(existing_tag)
        else:
            new_tag = Tag(name=tag_name_clean)
            session.add(new_tag)
            tag_objects.append(new_tag)
    
    db_note.tags = tag_objects
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        content=db_note.content,
        category=db_note.category,
        tags=[tag.name for tag in db_note.tags],
        created_at=db_note.created_at.isoformat()
    )

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, session: SessionDep):
    """Delete a note"""
    
    db_note = session.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    session.delete(db_note)
    session.commit()
    return  # 204 No Content

    # Not found
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )

# --- STATISTICS ---

@app.get("/notes/stats")
def get_note_stats(session: SessionDep):
    """
    Get statistics about notes from the database
    """
    notes = session.exec(select(Note)).all()
    tags = session.exec(select(Tag)).all()
    
    # Notizen pro Kategorie zählen
    categories = {}
    for n in notes:
        categories[n.category] = categories.get(n.category, 0) + 1
    
    # Top 5 Tags (Häufigkeit)
    tag_counts = []
    for t in tags:
        tag_counts.append({"tag": t.name, "count": len(t.notes)})
    
    # Sortieren nach Count absteigend und die ersten 5 nehmen
    top_tags = sorted(tag_counts, key=lambda x: x["count"], reverse=True)[:5]
    
    return {
        "total_notes": len(notes),
        "by_category": categories,
        "top_tags": top_tags,
        "unique_tags_count": len(tags)
    }

# --- TAGS ---

@app.get("/tags", response_model=list[str])
def list_tags(session: SessionDep):
    """Get all unique tags from the Tag table"""
    statement = select(Tag)
    tags = session.exec(statement).all()
    return sorted([tag.name for tag in tags])

@app.get("/tags/{tag_name}/notes", response_model=list[NoteResponse])
def get_notes_by_tag(tag_name: str, session: SessionDep):
    """Get all notes with a specific tag"""
    tag_lower = tag_name.lower()
    statement = select(Tag).where(Tag.name == tag_lower)
    tag = session.exec(statement).first()
    
    if not tag:
        return []
    
    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            tags=[t.name for t in n.tags],
            created_at=n.created_at.isoformat()
        )
        for n in tag.notes
    ]

# --- CATEGORIES ---

@app.get("/categories", response_model=list[str])
def list_categories(session: SessionDep):
    """Get all unique categories from all notes"""
    statement = select(Note.category)
    results = session.exec(statement).all()
    return sorted(list(set(results)))

@app.get("/categories/{category_name}/notes", response_model=list[NoteResponse])
def get_notes_by_category(category_name: str, session: SessionDep):
    """Get all notes in a specific category"""
    statement = select(Note).where(Note.category == category_name)
    notes = session.exec(statement).all()
    
    return [
        NoteResponse(
            id=n.id,
            title=n.title,
            content=n.content,
            category=n.category,
            tags=[t.name for t in n.tags],
            created_at=n.created_at.isoformat()
        )
        for n in notes
    ]

# --- PARTIAL UPDATE (PATCH) ---

@app.patch("/notes/{note_id}", response_model=NoteResponse)
def partial_update_note(note_id: int, note_update: NoteUpdate, session: SessionDep):
    """
    Partially update a note (only provided fields)
    """
    db_note = session.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    # Nur Felder aktualisieren, die im Request gesendet wurden (nicht None)
    if note_update.title is not None:
        db_note.title = note_update.title
    if note_update.content is not None:
        db_note.content = note_update.content
    if note_update.category is not None:
        db_note.category = note_update.category

    # Falls Tags gesendet wurden, diese komplett ersetzen
    if note_update.tags is not None:
        tag_objects = []
        for tag_name in note_update.tags:
            tag_name_clean = tag_name.lower().strip()
            existing_tag = session.exec(select(Tag).where(Tag.name == tag_name_clean)).first()
            if existing_tag:
                tag_objects.append(existing_tag)
            else:
                new_tag = Tag(name=tag_name_clean)
                session.add(new_tag)
                tag_objects.append(new_tag)
        db_note.tags = tag_objects

    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        content=db_note.content,
        category=db_note.category,
        tags=[t.name for t in db_note.tags],
        created_at=db_note.created_at.isoformat()
    )