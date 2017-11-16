# coding: utf-8

"""
    ngDesk_Operations

    ngDesk_Operations

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TicketMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ticket_message_id': 'int',
        'ticket_id': 'int',
        'body': 'str',
        'user_id': 'int',
        'date_created': 'datetime',
        'company_id': 'int',
        'ticket_attachments': 'list[Attachment]',
        'element1': 'str'
    }

    attribute_map = {
        'ticket_message_id': 'TICKET_MESSAGE_ID',
        'ticket_id': 'TICKET_ID',
        'body': 'BODY',
        'user_id': 'USER_ID',
        'date_created': 'DATE_CREATED',
        'company_id': 'COMPANY_ID',
        'ticket_attachments': 'TICKET_ATTACHMENTS',
        'element1': 'element1'
    }

    def __init__(self, ticket_message_id=None, ticket_id=None, body=None, user_id=None, date_created=None, company_id=None, ticket_attachments=None, element1=None):
        """
        TicketMessage - a model defined in Swagger
        """

        self._ticket_message_id = None
        self._ticket_id = None
        self._body = None
        self._user_id = None
        self._date_created = None
        self._company_id = None
        self._ticket_attachments = None
        self._element1 = None

        if ticket_message_id is not None:
          self.ticket_message_id = ticket_message_id
        if ticket_id is not None:
          self.ticket_id = ticket_id
        if body is not None:
          self.body = body
        if user_id is not None:
          self.user_id = user_id
        if date_created is not None:
          self.date_created = date_created
        if company_id is not None:
          self.company_id = company_id
        if ticket_attachments is not None:
          self.ticket_attachments = ticket_attachments
        if element1 is not None:
          self.element1 = element1

    @property
    def ticket_message_id(self):
        """
        Gets the ticket_message_id of this TicketMessage.

        :return: The ticket_message_id of this TicketMessage.
        :rtype: int
        """
        return self._ticket_message_id

    @ticket_message_id.setter
    def ticket_message_id(self, ticket_message_id):
        """
        Sets the ticket_message_id of this TicketMessage.

        :param ticket_message_id: The ticket_message_id of this TicketMessage.
        :type: int
        """

        self._ticket_message_id = ticket_message_id

    @property
    def ticket_id(self):
        """
        Gets the ticket_id of this TicketMessage.

        :return: The ticket_id of this TicketMessage.
        :rtype: int
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """
        Sets the ticket_id of this TicketMessage.

        :param ticket_id: The ticket_id of this TicketMessage.
        :type: int
        """

        self._ticket_id = ticket_id

    @property
    def body(self):
        """
        Gets the body of this TicketMessage.

        :return: The body of this TicketMessage.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this TicketMessage.

        :param body: The body of this TicketMessage.
        :type: str
        """

        self._body = body

    @property
    def user_id(self):
        """
        Gets the user_id of this TicketMessage.

        :return: The user_id of this TicketMessage.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this TicketMessage.

        :param user_id: The user_id of this TicketMessage.
        :type: int
        """

        self._user_id = user_id

    @property
    def date_created(self):
        """
        Gets the date_created of this TicketMessage.

        :return: The date_created of this TicketMessage.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this TicketMessage.

        :param date_created: The date_created of this TicketMessage.
        :type: datetime
        """

        self._date_created = date_created

    @property
    def company_id(self):
        """
        Gets the company_id of this TicketMessage.

        :return: The company_id of this TicketMessage.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """
        Sets the company_id of this TicketMessage.

        :param company_id: The company_id of this TicketMessage.
        :type: int
        """

        self._company_id = company_id

    @property
    def ticket_attachments(self):
        """
        Gets the ticket_attachments of this TicketMessage.

        :return: The ticket_attachments of this TicketMessage.
        :rtype: list[Attachment]
        """
        return self._ticket_attachments

    @ticket_attachments.setter
    def ticket_attachments(self, ticket_attachments):
        """
        Sets the ticket_attachments of this TicketMessage.

        :param ticket_attachments: The ticket_attachments of this TicketMessage.
        :type: list[Attachment]
        """

        self._ticket_attachments = ticket_attachments

    @property
    def element1(self):
        """
        Gets the element1 of this TicketMessage.

        :return: The element1 of this TicketMessage.
        :rtype: str
        """
        return self._element1

    @element1.setter
    def element1(self, element1):
        """
        Sets the element1 of this TicketMessage.

        :param element1: The element1 of this TicketMessage.
        :type: str
        """

        self._element1 = element1

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TicketMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
