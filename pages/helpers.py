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

    def get_purchases(self, raw_response):
        """
        Parses attendees from dict by name, order_id, total purchase value
        :return: List[dictionary]
        """

        order_data = []
        # Get Attendees list
        for order in raw_response[0]['orders']:
            # Get specific info for each participant
            data = {"first_name": order["first_name"],
                    "last_name": order["last_name"],
                    "order_id": order["id"],
                    "order_value": order["costs"]["base_price"]["major_value"]}
            order_data.append(data)
        return order_data


if __name__ == '__main__':
    getter = Getter('events/41440379290/orders/')  # events/41440379290/orders/ TODO add correct event id with this route once event published
    getter.get_data()
    analyzer = Analyzer()
    print(analyzer.get_purchases(getter.response))