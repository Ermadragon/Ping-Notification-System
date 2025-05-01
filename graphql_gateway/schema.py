import strawberry
import requests
from strawberry.types import Info
from .config import USER_SERVICE_URL, NOTIF_SERVICE_URL, RECOMM_SERVICE_URL

@strawberry.type
class Notification:
    id: str
    type: str
    content: str
    sent_at: str

@strawberry.type
class User:
    id: str
    name: str
    email: str
    preferences: str

@strawberry.type
class Query:
    @strawberry.field
    def me(self, info: Info) -> User:
        user_id = info.context['user_id']
        res = requests.get(f"{USER_SERVICE_URL}/users/{user_id}", headers=info.context['headers'])
        return User(**res.json())

    @strawberry.field
    def unread_notifications(self, info: Info) -> list[Notification]:
        user_id = info.context['user_id']
        res = requests.get(f"{NOTIF_SERVICE_URL}/notifications/{user_id}/unread")
        return [Notification(**n) for n in res.json()]

@strawberry.type
class Mutation:
    @strawberry.field
    def generate_recommendations(self, info: Info) -> str:
        user_id = info.context['user_id']
        res = requests.post(f"{RECOMM_SERVICE_URL}/recommendations/generate/{user_id}")
        if res.status_code == 200:
            return "Recommendations sent!"
        return "Failed to generate recommendations"

schema = strawberry.Schema(query=Query, mutation=Mutation)
