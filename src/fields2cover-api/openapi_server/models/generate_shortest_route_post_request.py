from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.feature_collection import FeatureCollection
from openapi_server.models.point import Point
from openapi_server import util

from openapi_server.models.feature_collection import FeatureCollection  # noqa: E501
from openapi_server.models.point import Point  # noqa: E501

class GenerateShortestRoutePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, working_lanes=None, transport_lanes=None, start_point=None, end_point=None):  # noqa: E501
        """GenerateShortestRoutePostRequest - a model defined in OpenAPI

        :param working_lanes: The working_lanes of this GenerateShortestRoutePostRequest.  # noqa: E501
        :type working_lanes: FeatureCollection
        :param transport_lanes: The transport_lanes of this GenerateShortestRoutePostRequest.  # noqa: E501
        :type transport_lanes: FeatureCollection
        :param start_point: The start_point of this GenerateShortestRoutePostRequest.  # noqa: E501
        :type start_point: Point
        :param end_point: The end_point of this GenerateShortestRoutePostRequest.  # noqa: E501
        :type end_point: Point
        """
        self.openapi_types = {
            'working_lanes': FeatureCollection,
            'transport_lanes': FeatureCollection,
            'start_point': Point,
            'end_point': Point
        }

        self.attribute_map = {
            'working_lanes': 'workingLanes',
            'transport_lanes': 'transportLanes',
            'start_point': 'startPoint',
            'end_point': 'endPoint'
        }

        self._working_lanes = working_lanes
        self._transport_lanes = transport_lanes
        self._start_point = start_point
        self._end_point = end_point

    @classmethod
    def from_dict(cls, dikt) -> 'GenerateShortestRoutePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _generateShortestRoute_post_request of this GenerateShortestRoutePostRequest.  # noqa: E501
        :rtype: GenerateShortestRoutePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def working_lanes(self) -> FeatureCollection:
        """Gets the working_lanes of this GenerateShortestRoutePostRequest.


        :return: The working_lanes of this GenerateShortestRoutePostRequest.
        :rtype: FeatureCollection
        """
        return self._working_lanes

    @working_lanes.setter
    def working_lanes(self, working_lanes: FeatureCollection):
        """Sets the working_lanes of this GenerateShortestRoutePostRequest.


        :param working_lanes: The working_lanes of this GenerateShortestRoutePostRequest.
        :type working_lanes: FeatureCollection
        """
        if working_lanes is None:
            raise ValueError("Invalid value for `working_lanes`, must not be `None`")  # noqa: E501

        self._working_lanes = working_lanes

    @property
    def transport_lanes(self) -> FeatureCollection:
        """Gets the transport_lanes of this GenerateShortestRoutePostRequest.


        :return: The transport_lanes of this GenerateShortestRoutePostRequest.
        :rtype: FeatureCollection
        """
        return self._transport_lanes

    @transport_lanes.setter
    def transport_lanes(self, transport_lanes: FeatureCollection):
        """Sets the transport_lanes of this GenerateShortestRoutePostRequest.


        :param transport_lanes: The transport_lanes of this GenerateShortestRoutePostRequest.
        :type transport_lanes: FeatureCollection
        """
        if transport_lanes is None:
            raise ValueError("Invalid value for `transport_lanes`, must not be `None`")  # noqa: E501

        self._transport_lanes = transport_lanes

    @property
    def start_point(self) -> Point:
        """Gets the start_point of this GenerateShortestRoutePostRequest.


        :return: The start_point of this GenerateShortestRoutePostRequest.
        :rtype: Point
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point: Point):
        """Sets the start_point of this GenerateShortestRoutePostRequest.


        :param start_point: The start_point of this GenerateShortestRoutePostRequest.
        :type start_point: Point
        """

        self._start_point = start_point

    @property
    def end_point(self) -> Point:
        """Gets the end_point of this GenerateShortestRoutePostRequest.


        :return: The end_point of this GenerateShortestRoutePostRequest.
        :rtype: Point
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point: Point):
        """Sets the end_point of this GenerateShortestRoutePostRequest.


        :param end_point: The end_point of this GenerateShortestRoutePostRequest.
        :type end_point: Point
        """

        self._end_point = end_point
