from local_settings import TOKEN
import requests

class Getter:
    """This class is used for making API calls to different Eventbrite endpoints, and temporarily storing the data"""
    def __init__(self, endpoint):
        self.url = 'https://www.eventbriteapi.com/v3/' + endpoint
        self.response = []

    def get_data(self, **kwargs):
        """Send API request to Strava endpoint"""
        package = {k: v for k, v in kwargs.items()}
        package = {k: ','.join(v) if isinstance(v, list) else v for k, v in package.items()}
        headers = {"Authorization": "Bearer {}".format(TOKEN)}
        resp = requests.get(self.url, params=package, headers=headers)


        self.response.append(resp.json())

class Analyzer:
    """This class parses an API response to get particular information"""

    def get_attendees(self):
        """
        Gets attendees by name, order_id
        :return: dictionary
        """

        # Attendees

        # Orders



if __name__ == '__main__':
    getter = Getter('users/me/owned_events/')  # events/41123033099/orders/ TODO add correct event id with this route once event published
    getter.get_data()
    print(getter.response)