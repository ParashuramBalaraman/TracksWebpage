from music.domainmodel.review import Review
from music.domainmodel.track import Track


class User:

    def __init__(self, user_name: str, password: str):
        if type(user_name) != str or user_name == "":
            self.__user_name = None
        else:
            self.__user_name = user_name.strip()

        if type(password) != str or password == "":
            self.__password = None
        else:
            self.__password = password

        self.__reviews: list[Review] = []
        self.__liked_tracks: list[Track] = []


    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def reviews(self) -> list:
        return self.__reviews

    def add_review(self, new_review: Review):
        if not isinstance(new_review, Review) or new_review in self.__reviews:
            return
        self.__reviews.append(new_review)

    def remove_review(self, review: Review):
        if not isinstance(review, Review) or review not in self.__reviews:
            return
        self.__reviews.remove(review)

    @property
    def liked_tracks(self) -> list:
        return self.__liked_tracks

    def add_liked_track(self, track: Track):
        if not isinstance(track, Track) or track in self.__liked_tracks:
            return
        self.__liked_tracks.append(track)

    def remove_liked_track(self, track: Track):
        if not isinstance(track, Track) or track not in self.__liked_tracks:
            return
        self.__liked_tracks.remove(track)

    def __repr__(self):
        return f'<User {self.user_name}, password = {self.password}>'

    # def __eq__(self, other):
    #     if not isinstance(other, self.__class__):
    #         return False
    #     return self.user_id == other.user_id

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return other.user_name == self.user_name

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.user_id < other.user_id

    def __hash__(self):
        return hash(self.user_id)
