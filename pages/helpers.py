import os
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
        headers = {"Authorization": "Bearer {}".format(os.environ['TOKEN'])}
        resp = requests.get(self.url, params=package, headers=headers)


        self.response.append(resp.json())

class Analyzer:
    """This class parses an API response to get particular information"""

    def get_attendees(self, raw_response):
        """
        Gets attendees by name, order_id
        :return: dictionary
        """

        # Get Attendees list
        for order in raw_response[0]['orders']:
            # Get specific info for each participant
            print("First name: {}\
                   Last name: {}\
                   Order Id: {}\
                   Total value: {}".format(order["first_name"], order["last_name"], order["id"], order["costs"]["base_price"]["major_value"]))
            print("-----------------")

        # Orders



if __name__ == '__main__':
    getter = Getter('events/41440379290/orders/')  # events/41440379290/orders/ TODO add correct event id with this route once event published
    getter.get_data()
    analyzer = Analyzer()
    analyzer.get_attendees(getter.response)