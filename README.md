# ngDesk API

[ngDesk](http://www.ngdesk.com) supports 3rd - party developer integration. Simply generate an API key in the webapp and use its client_id and client_secret to make requests. 

**Format JSON payloads as illustrated in the examples below.**

## Tickets

## Overview of API Endpoints

All URIs are relative to *https://api.ngdesk.com/v2/operations*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_ticket**](docs/DefaultApi.md#get_ticket) | **GET** /tickets/{ticket_id} | 
*DefaultApi* | [**get_tickets**](docs/DefaultApi.md#get_tickets) | **GET** /tickets | 
*DefaultApi* | [**post_messages**](docs/DefaultApi.md#post_messages) | **POST** /tickets/{ticket_id}/messages | 
*DefaultApi* | [**post_tickets**](docs/DefaultApi.md#post_tickets) | **POST** /tickets | 
*DefaultApi* | [**put_tickets**](docs/DefaultApi.md#put_tickets) | **PUT** /tickets | 


### Get All Company Tickets

> GET https://api.ngdesk.com/v2/operations/tickets?client_secret=x&client_id=y

### Create Ticket

This call will create a ticket.

> POST https://api.ngdesk.com/v2/operations/tickets?client_secret=x&client_id=y

The JSON payload must be formatted like this example: 

	{
	  "TICKETS": [
	    {
	      "SUBJECT": "This is the ticket's subject",
	      "TICKET_MESSAGES": {
	  	    "BODY": "This is the initial message for the ticket",
	  	    "IS_INTERNAL": "N"
	      },
	      "DATE_REQUIRED_BY": "2017-11-30 07:30:00",
	      "SEVERITY": "Low",
	      "SOURCE": "API",
	      "STATUS": "NEW"
	    }
	  ]
	}


#### **Important** - the following fields can only take the values specified below:

##### "SEVERITY":

1. "Low"
2. "Moderate"
3. "High"
4. "Critical"


### Update Tickets

This call will update the values of a ticket.

> PUT https://api.ngdesk.com/v2/operations/tickets?client_secret=x&client_id=y

The JSON payload must be formatted like this example: 

	{
	  "TICKETS": [
	  	{
	  	  "TICKET_ID": 1087,
	  	  "STATUS":"OPEN",
	  	  "MINUTES_WORKED":2,
	  	  "SEVERITY":"Critical"
	  	}
	  ]
	}

#### **Important** - the following fields can only take the values specified below

##### "STATUS":

1. "OPEN"
2. "NEW"
3. "PENDING"
4. "CLOSED"
5. "RESOLVED"

##### "SEVERITY":

1. "Low"
2. "Moderate"
3. "High"
4. "Critical"


### Get a Ticket

This call will return one ticket with all of its ticket messages. 

> GET https://api.ngdesk.com/v2/operations/tickets/ticket_id?client_secret=x&client_id=y

Where 
- ticket_id = the id number of whichever ticket you need. 

### Reply to a ticket

This will create a ticket message for a ticket. 

> POST https://api.ngdesk.com/v2/operations/tickets/ticket_id/messages?client_secret=x&client_id=y

Where ticket_id = the id number of whichever ticket you need, and
the JSON payload must be formatted like this example: 

	{
	  "TICKETS": [
	  	{
	  	  "TICKET_MESSAGES": [
	  	  	{
	  	  	  "TICKET_ID": 1234,
	  	  	  "BODY": "This is the body of the ticket message that will be posted",
	  	  	  "IS_INTERNAL": "N"
	  	  	}
	  	  ]
	  	}
	  ]
	}

#### **Important** - the following fields can only take the values specified below

##### TICKET_ID

- Should be the same value as ticket_id in the path.

##### "IS_INTERNAL":

1. "Y"
2. "N"

