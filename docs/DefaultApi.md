# swagger_client.DefaultApi

All URIs are relative to *https://localhost/api/v2/operations*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ticket**](DefaultApi.md#get_ticket) | **GET** /tickets/{ticket_id} | 
[**get_tickets**](DefaultApi.md#get_tickets) | **GET** /tickets | 
[**post_messages**](DefaultApi.md#post_messages) | **POST** /tickets/{ticket_id}/messages | 
[**post_tickets**](DefaultApi.md#post_tickets) | **POST** /tickets | 
[**put_tickets**](DefaultApi.md#put_tickets) | **PUT** /tickets | 


# **get_ticket**
> Ticket get_ticket(ticket_id, authentication_token=authentication_token, category=category, statuses=statuses, ordered_column=ordered_column, ordered_by=ordered_by, client_id=client_id, client_secret=client_secret)



Retrievs a ticket

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ticket_id = 'ticket_id_example' # str | 
authentication_token = 'authentication_token_example' # str |  (optional)
category = 'category_example' # str |  (optional)
statuses = 'statuses_example' # str |  (optional)
ordered_column = 'ordered_column_example' # str |  (optional)
ordered_by = 'ordered_by_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)

try: 
    api_response = api_instance.get_ticket(ticket_id, authentication_token=authentication_token, category=category, statuses=statuses, ordered_column=ordered_column, ordered_by=ordered_by, client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **authentication_token** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **statuses** | **str**|  | [optional] 
 **ordered_column** | **str**|  | [optional] 
 **ordered_by** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tickets**
> list[Ticket] get_tickets(authentication_token=authentication_token, start=start, length=length, draw=draw, q=q, sort_by=sort_by, sort_by_order=sort_by_order, passed_account_id=passed_account_id, passed_user_id=passed_user_id, view_id=view_id, client_id=client_id, client_secret=client_secret)



Retrieve tickets

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authentication_token = 3.4 # float | User athentication uuid (optional)
start = 56 # int | Start query value (optional)
length = 56 # int | Number of rows query (optional)
draw = 56 # int | Number of times table has been reloaded (optional)
q = 'q_example' # str | Values provided in q are tokenized and search on columns: TICKET_ID,SUBJECT,REQUESTOR_UERNAME, REQUESTOR_EMAIL, TICKET_MESSAGES (optional)
sort_by = 'sort_by_example' # str | Column name to order table by (optional)
sort_by_order = 'sort_by_order_example' # str | Sort by ascending or descending (optional)
passed_account_id = 'passed_account_id_example' # str |  (optional)
passed_user_id = 'passed_user_id_example' # str |  (optional)
view_id = 56 # int | View Id (optional)
client_id = 'client_id_example' # str | API ID (optional)
client_secret = 'client_secret_example' # str | API Secret (optional)

try: 
    api_response = api_instance.get_tickets(authentication_token=authentication_token, start=start, length=length, draw=draw, q=q, sort_by=sort_by, sort_by_order=sort_by_order, passed_account_id=passed_account_id, passed_user_id=passed_user_id, view_id=view_id, client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_token** | **float**| User athentication uuid | [optional] 
 **start** | **int**| Start query value | [optional] 
 **length** | **int**| Number of rows query | [optional] 
 **draw** | **int**| Number of times table has been reloaded | [optional] 
 **q** | **str**| Values provided in q are tokenized and search on columns: TICKET_ID,SUBJECT,REQUESTOR_UERNAME, REQUESTOR_EMAIL, TICKET_MESSAGES | [optional] 
 **sort_by** | **str**| Column name to order table by | [optional] 
 **sort_by_order** | **str**| Sort by ascending or descending | [optional] 
 **passed_account_id** | **str**|  | [optional] 
 **passed_user_id** | **str**|  | [optional] 
 **view_id** | **int**| View Id | [optional] 
 **client_id** | **str**| API ID | [optional] 
 **client_secret** | **str**| API Secret | [optional] 

### Return type

[**list[Ticket]**](Ticket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_messages**
> post_messages(body, ticket_id, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)



Insert a messages

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Ticket() # Ticket | The request body for the operation
ticket_id = 'ticket_id_example' # str | 
authentication_token = 'authentication_token_example' # str | User athentication (optional)
client_id = 'client_id_example' # str | api client (optional)
client_secret = 'client_secret_example' # str | api secret (optional)

try: 
    api_instance.post_messages(body, ticket_id, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)
except ApiException as e:
    print("Exception when calling DefaultApi->post_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ticket**](Ticket.md)| The request body for the operation | 
 **ticket_id** | **str**|  | 
 **authentication_token** | **str**| User athentication | [optional] 
 **client_id** | **str**| api client | [optional] 
 **client_secret** | **str**| api secret | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tickets**
> Ticket post_tickets(body, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)



Insert a tickets

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = [swagger_client.TicketMessage()] # list[TicketMessage] | The request body for the operation
authentication_token = 3.4 # float | User athentication uuid (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)

try: 
    api_response = api_instance.post_tickets(body, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TicketMessage]**](TicketMessage.md)| The request body for the operation | 
 **authentication_token** | **float**| User athentication uuid | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tickets**
> list[Ticket] put_tickets(body, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)



Update tickets

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = [swagger_client.Ticket()] # list[Ticket] | The request body for the operation
authentication_token = true # bool | User athentication uuid (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)

try: 
    api_response = api_instance.put_tickets(body, authentication_token=authentication_token, client_id=client_id, client_secret=client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Ticket]**](Ticket.md)| The request body for the operation | 
 **authentication_token** | **bool**| User athentication uuid | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**list[Ticket]**](Ticket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

