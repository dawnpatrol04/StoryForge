from dotenv import load_dotenv

load_dotenv()

# from characters import MainCharacterChain
from structure import get_structure
from events import get_events
from writing import write_book
from publishing import DocWriter

subject = 'The RV surf trip of 2024'
author='Bruce Brown'
genre='Adventure'

# main_character_chain = MainCharacterChain()
doc_writer = DocWriter()

title, plot, chapter_dict = get_structure(
    subject, 
    genre, 
    author
)
summaries_dict, event_dict = get_events(
    subject, 
    genre, 
    author,
    title, 
    plot, 
    chapter_dict
)

book = write_book(
    genre, 
    author, 
    title,
    plot, 
    summaries_dict, 
    event_dict
)

doc_writer.write_doc(
    book, 
    chapter_dict, 
    title
)
