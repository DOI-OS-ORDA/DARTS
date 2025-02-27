from search.repositories.repository import Repository
from search.models import Event


class EventsRepository(Repository):
    relation = Event
