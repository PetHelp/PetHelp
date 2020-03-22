# API endpoints

Die Animal+Message Endpunkte können nur authentifiziert genutzt weden.
HelpOffer + HelpRequest per GET ist unauthentifiziert möglich.
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
- note: listet alle verfügbaren HelpTypes

### json resource representation
- [string, string, string]

## AnimalType
- endpoint: /animal-types/
- methods: GET
- note: listet alle verfügbaren AnimalTypes

### json resource representation
- [string, string, string]

## Animals
- endpoint: /animals/
- methods: GET, POST
- required payload for creation: {type: animal_type, name: ""}
- note: rufe liste aller eigenen animals ab, erstelle neues animal

- endpoint: /animals/{id}/
- methods: GET, PUT, PATCH, DELETE
- payload {}
- note: rufe ein animals ab, update ein animal


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
- note: rufe liste aller help requests ab, erstelle ein help request

- endpoint: /help-requests/{id}/
- methods: GET, PUT, PATCH, DELETE
- note: rufe einen help request ab, update oder lösche es

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
- note: rufe liste aller help offers ab, erstelle eine help offer

- endpoint: /help-offers/{id}/
- methods: GET, PUT, PATCH, DELETE
- note: rufe eine help offer ab, update oder lösche es

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
- note: rufe messages ab oder erstelle ein

### json resource representation
- sender: int
- receiver: int
- text: string
- created_at: string
- related_help_request: null/int
- related_help_offer: null/int


# Api Erweiterung Proposal

## User

* [Register](register/post.md): `POST /register/`
* [Reset password](reset-password/post.md): `POST /reset-password/`
* [Login](token/post.md): `POST /token/`

## Animals

### GET /animals/

Liefert Liste von Tier-Ids?
Liefert Liste von Tieren?
Liefert nur ein Tier?

payload:

```
{
}
```

response:

```
```


### POST /animals/

Speichert ein neues Tier.
Aktualisiert auch ein bestehendes Tier oder separater Endpunkt gewünscht?

payload:
 
```
  {
    name: "Gamma",
    type: 1,
    image: ?,
    location: ?,
    description: "Ein ganz Lieber!",
    tags: [1, 2, 3]
  }
```

### GET /featured-help-requests/

Gibt die Liste der Hilfsgesuche für die Startseite.
Dieser Endpoint kann auch nicht authentifiziert genutzt werden.

payload: {}

response:

```
[
  {
    name: "Gamma",
    location: "Hamburg",
    emergency: true
  },
  ...
]
```

### GET /help-requests/

Liefert (gefilterte) Hilfsgesuche?

payload:

```
{
  filter?
}
```

response:
```
[
  {
    ...
  },
  ...
]
```


## HelpOffers

### GET /featured-help-offers/

Liefert die Hilfsangebote für die Startseite.
Dieser Endpoint kann auch nicht authentifiziert genutzt werden.

payload: {}

response:

```
[
  {
    id: 1,
    name: "Kathi König",
    location: "Hamburg",
    teaser: "Hier steht etwas über sie\nHier steht noch mehr über sie"
  }
]
```

### GET /help-offers/

payload:

```
{
  filter?
}
```

response:
```
[
  {
    ...
  },
  ...
]
```

### POST /help-offers/

Erstellt ein neues (sofort aktives?) Hilfsangebot.
Aktualisiert es auch ein bestehendes Hilfsangebot oder separater Endpunkt gewünscht?

payload:

```
{
  help_type: 1,
  animal_type: 1,
  description: "Biete Spaziergänge",
  activate?
}
```
