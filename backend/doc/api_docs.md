# API endpoints

Die regulären Endpunkte können nur authentifiziert genutzt weden.
Das Token muss im  Authorization-Header mit dem Prefix "Bearer " gesendet werden.

## Register user
- endpoint: /register/
- method: POST
- payload: {name: "name", email: "email@test.de", password: "secret"}
- success: 201
- error: 400

## Reset password
- endpoint: /reset-password/
- method: POST
- payload: {email: "email@test.de"}
- success: 200
- error: 400

## Login/Get Token
- endpoint: /token/
- method: POST
- payload: {email: "email@test.de", password: "secret}
- response: {access: access_token, refresh: refresh_token}
- success: 200
- error: 401

## HelpType
- endpoint: /help-types/
- methods: GET

### json resource representation
- [string, string, string]

## AnimalType
- endpoint: /animal-types/
- methods: GET

### json resource representation
- [string, string, string]

## Animals
- endpoint: /animals/
- methods: GET, POST
- required payload for creation: {type: animal_type, name: ""}

- endpoint: /animals/{id}/
- methods: GET, PUT, PATCH, DELETE
- payload {}

### json resource representation
- owner: int
- name: string
- type: AnimalType
- image: string (base64 encoded)
- current_address: string
- description: string
- care_person: null/id

## HelpRequests
- endpoint: /help-requests/
- methods: GET, POST
- required payload for creation: {type: help_type, description: "", animals: [animal_id, animal_id2]}

- endpoint: /help-requests/{id}/
- methods: GET, PUT, PATCH, DELETE

### json resource representation
- user: int
- created_at: string
- type: HelpType
- description: string
- active: bool
- animals: []

## HelpOffers
- endpoint: /help-offers/
- methods: GET, POST
- required payload for creation: {type: help_type, description: ""}
- endpoint: /help-offers/{id}/
- methods: GET, PUT, PATCH, DELETE

### json resource representation
- user: int
- created_at: string
- type: HelpType
- description: string
- active: bool


## Messages
- endpoint: /messages/
- methods: GET, POST
- required payload for creation: {message: "", receiver: {user_id}, related_help_request: {help_request_id}, related_help_offer: {help_offer_id}}
- note: related_help_request or related_help_offer must be set!

### json resource representation
- sender: int
- receiver: int
- text: string
- created_at: string
- related_help_request: null/int
- related_help_offer: null/int
