from mcp.server.fastmcp import FastMCP
import os


mcp = FastMCP("AI-Sticky-Notes")
NOTES_FILE = "notes.txt"

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write("")


@mcp.tool()
def add_note(message:str)->str:
    """Append a new note to the sticky note file\
        Args:
        message(str): The note content to be added
        
        Returns :
        str : Confirmation message indicating the note was saved"""
    ensure_file()
    with open(NOTES_FILE, 'a') as f:
        f.write(message+'\n')
    return "Note saved"


@mcp.tool()
def get_notes():
    """Retrieve all notes from the sticky note file\
        Returns :
        list : A list of all notes"""
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    return [note.strip() for note in notes if note.strip()]


@mcp.tool()
def delete_note(index:int)->str:
    """Delete a note by its index in the list of notes\
        Args:
        index(int): The index of the note to be deleted
        
        Returns :
        str : Confirmation message indicating the note was deleted"""
    ensure_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    
    if 0 <= index < len(notes):
        del notes[index]
        with open(NOTES_FILE, 'w') as f:
            f.writelines(notes)
        return "Note deleted"
    else:
        return "Invalid index"